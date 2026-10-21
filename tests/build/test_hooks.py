# ═══════════════════════════════════════════════════════════════════════════════
# customers.riskmandate.ai — Test__Hooks
# The four hooks this site hands customers, driven as Claude Code drives them:
# a tool call as JSON on stdin, the decision as JSON on stdout. Every refusal has
# an allowed twin, so a hook that refused everything fails as surely as one that
# refused nothing. Each hook runs as its own process, the way it will run.
# ═══════════════════════════════════════════════════════════════════════════════

import json
import subprocess
import sys

from pathlib  import Path
from unittest import TestCase

ROOT  = Path(__file__).resolve().parents[2]
HOOKS = ROOT / 'policies' / 'hooks'
CWD   = '/home/user/my-project'


def run(hook, tool, **tool_input):
    call   = {'session_id': 'test', 'cwd': CWD, 'hook_event_name': 'PreToolUse', 'permission_mode': 'default',
              'tool_name': tool, 'tool_input': tool_input}
    result = subprocess.run([sys.executable, str(HOOKS / hook)], input=json.dumps(call), capture_output=True, text=True, timeout=10)
    assert result.returncode == 0, result.stderr
    if not result.stdout.strip():
        return None, ''
    out = json.loads(result.stdout)['hookSpecificOutput']
    assert out['hookEventName'] == 'PreToolUse'
    return out['permissionDecision'], out['permissionDecisionReason']


class Test__Hooks(TestCase):

    def check(self, hook, cases):
        for expected, tool, tool_input in cases:
            with self.subTest(hook=hook, tool=tool, input=tool_input):
                decision, reason = run(hook, tool, **tool_input)
                self.assertEqual(decision, expected, reason)
                if decision:
                    self.assertIn('Behaviour policy RM-R', reason)

    def test_touch_your_secrets(self):
        self.check('touch_your_secrets.py', [
            ('deny', 'Read'     , {'file_path': f'{CWD}/.env'}),
            (None  , 'Read'     , {'file_path': f'{CWD}/.env.example'}),                    # the twin: the template is fine
            ('deny', 'Read'     , {'file_path': f'{CWD}/.env.production'}),
            (None  , 'Read'     , {'file_path': f'{CWD}/src/environment.ts'}),
            ('deny', 'Read'     , {'file_path': '/home/user/.ssh/id_ed25519'}),
            ('deny', 'Read'     , {'file_path': '/home/user/.aws/credentials'}),
            ('deny', 'Edit'     , {'file_path': f'{CWD}/config/secrets/api.yaml', 'old_string': 'a', 'new_string': 'b'}),
            ('deny', 'Grep'     , {'pattern': 'TOKEN', 'path': f'{CWD}/.env'}),
            (None  , 'Grep'     , {'pattern': 'TOKEN', 'path': f'{CWD}/src'}),
            ('deny', 'Bash'     , {'command': 'cat .env'}),
            ('deny', 'Bash'     , {'command': 'grep DATABASE_URL .env.local'}),
            (None  , 'Bash'     , {'command': 'cat .env.example'}),
            ('deny', 'Bash'     , {'command': 'printenv'}),
            (None  , 'Bash'     , {'command': 'printenv PATH'}),                            # one named, harmless variable
            ('deny', 'Bash'     , {'command': 'cp ~/.ssh/id_rsa /tmp/k'}),
            (None  , 'Bash'     , {'command': 'npm test'}),
            (None  , 'Write'    , {'file_path': f'{CWD}/README.md', 'content': 'x'}),
        ])

    def test_push_anywhere(self):
        self.check('push_anywhere.py', [
            ('deny', 'Bash', {'command': 'git push origin main'}),
            ('deny', 'Bash', {'command': 'git push --force origin feature/x'}),
            ('deny', 'Bash', {'command': 'git push -f'}),
            ('deny', 'Bash', {'command': 'git push origin +feature/x'}),
            ('deny', 'Bash', {'command': 'git push origin HEAD:master'}),
            ('deny', 'Bash', {'command': 'git push origin --delete old-branch'}),
            ('deny', 'Bash', {'command': 'git add . && git commit -m x && git push origin main'}),
            ('ask' , 'Bash', {'command': 'git push origin feature/login'}),                     # the twin: any other push asks
            ('ask' , 'Bash', {'command': 'git push -u origin claude/fix-123'}),
            ('ask' , 'Bash', {'command': 'gh pr create --fill'}),
            (None  , 'Bash', {'command': 'git status && git log --oneline -3'}),
            (None  , 'Bash', {'command': 'git pull origin main'}),
            (None  , 'Read', {'file_path': f'{CWD}/README.md'}),
        ])

    def test_delete_files(self):
        self.check('delete_files.py', [
            ('deny', 'Bash', {'command': 'rm -rf build'}),
            ('deny', 'Bash', {'command': 'rm -fr node_modules'}),
            ('deny', 'Bash', {'command': 'rm -r -f dist'}),
            ('deny', 'Bash', {'command': 'rm ~/notes.txt'}),
            ('deny', 'Bash', {'command': 'rm /etc/hosts'}),
            ('deny', 'Bash', {'command': 'rm ../other-project/file.txt'}),
            ('ask' , 'Bash', {'command': 'rm build/output.log'}),                               # the twin: inside the project, it asks
            ('ask' , 'Bash', {'command': 'rm -r tmp'}),
            ('ask' , 'Bash', {'command': 'git clean -fd'}),
            ('ask' , 'Bash', {'command': 'find . -name "*.pyc" -delete'}),
            (None  , 'Bash', {'command': 'ls -la && npm run build'}),
            (None  , 'Bash', {'command': 'echo "remove the old rows" > notes.txt'}),           # the word, not the command
        ])

    def test_change_its_own_permissions(self):
        self.check('change_its_own_permissions.py', [
            ('ask', 'Edit'     , {'file_path': f'{CWD}/.claude/settings.json', 'old_string': 'a', 'new_string': 'b'}),
            ('ask', 'Write'    , {'file_path': f'{CWD}/.claude/settings.local.json', 'content': '{}'}),
            ('ask', 'Write'    , {'file_path': f'{CWD}/.claude/hooks/push_anywhere.py', 'content': ''}),
            ('ask', 'Edit'     , {'file_path': '/home/user/.claude/settings.json', 'old_string': 'a', 'new_string': 'b'}),
            ('ask', 'Bash'     , {'command': "sed -i 's/deny/allow/' .claude/settings.json"}),
            ('ask', 'Bash'     , {'command': 'rm .claude/hooks/delete_files.py'}),
            ('ask', 'Bash'     , {'command': 'echo {} > .claude/settings.local.json'}),
            (None , 'Read'     , {'file_path': f'{CWD}/.claude/settings.json'}),                 # the twin: reading its settings is fine
            (None , 'Bash'     , {'command': 'cat .claude/settings.json'}),
            (None , 'Edit'     , {'file_path': f'{CWD}/src/settings.json', 'old_string': 'a', 'new_string': 'b'}),
            (None , 'Edit'     , {'file_path': f'{CWD}/CLAUDE.md', 'old_string': 'a', 'new_string': 'b'}),
        ])

    def test_not_a_tool_call_is_no_answer(self):
        for hook in sorted(HOOKS.glob('*.py')):
            with self.subTest(hook=hook.name):
                result = subprocess.run([sys.executable, str(hook)], input='not json', capture_output=True, text=True, timeout=10)
                self.assertEqual((result.returncode, result.stdout), (0, ''))
