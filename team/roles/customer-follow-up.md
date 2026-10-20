# Role: customer follow-up

*customers.riskmandate.ai · held by the lead for the first batch; an agent drafts · written at v0.1.0 (2026-10-20) · CC BY 4.0*

The daily contact with each customer. Asks three things, as often as daily if that helps: what they did, what got in the way, what is next. Records the answers on the customer page in summary and keeps the rest with the lead. The pattern is the newsroom's: an agent drafts, a person reads and sends, and nothing goes out that a person has not seen.

## Rules this role enforces, and the mistake behind each

| Rule | The mistake it came from |
|---|---|
| Three questions, a line each is plenty; "nothing, I was busy" is a fine answer and goes in the log. | A follow-up that reads as a form gets no reply; Paul Graham's attentiveness is a person asking, not a survey. |
| The log on the customer page is the summary; names of systems, the contents of a grant or a mandate, and anything the customer did not want public stay with the lead. | The brief: nothing is published without their yes, and the default is no. |
| The second answer, what got in the way, is read against the three questions on the learning page, and a pattern across customers becomes a finding with its count. | A finding typed before it was counted is a guess; the learning page's table starts empty on purpose. |
| A customer who has not replied is asked again, not marked. | A status that says "stalled" is a judgement; the log records dates and the ladder records steps. |
| The follow-up names the step the customer is on and links their page, so they can see what the site says about them. | A page about a person that the person has not seen is a page they cannot correct. |

## The message

The template is on [the follow-up page](../../follow-up/index.md). An agent fills `{first name}`, `{step}` and `{id}` from the private list and the customer record; a person sends it from agent@riskmandate.ai.

## Starting prompt

"For each customer in data/customers.json whose status is not example, draft today's follow-up from the template, with the step they are on and the link to their page, and put the drafts where the lead reads them. Do not send."
