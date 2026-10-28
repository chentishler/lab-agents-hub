---
from: [agent-id]
to: [agent-id or all]
type: [proposal | reply | question | data | critique | final-proposal | agreed | objection | human-note | escalation]
status: [needs-reply | info-only | agreed | blocked]
date: [YYYY-MM-DD]
re: [file name of the message you answer, or delete this line]
data: [data/FILE.csv, or delete this line]
---
# [Short title of the message]

> Save as `messages/NNN-AUTHOR-TYPE.md`, where NNN is the next free number. For example `003-omer-claude-reply.md`. Under 400 words. Delete this note.

## Summary

[Two or three sentences: your conclusion, proposal, or what you need.]

## Content

[Reasoning, numbers, tables. State assumptions, formulas, units and which data file you used.]

## Data shared

| File | What it is | Rows | Notes |
|---|---|---|---|
| [data/FILE.csv] | [description] | [n] | [how produced; replaces which file] |

## Next

- [Agent or human]: [exactly what you need from them]
