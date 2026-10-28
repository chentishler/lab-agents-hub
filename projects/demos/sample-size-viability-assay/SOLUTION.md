---
title: Sample size for a viability assay: solution
status: solved-pending-human-review
date: 2026-10-14
written_by: noa-claude
---
# Solution

## The answer

Run **3 plates**, each with **7 vehicle wells and 7 LX-7 wells** (21 per group), plus 6 positive-control and 6 blank wells per plate. Analyse with a linear model that includes plate. This gives at least 80% power to detect a 10-point drop in viability, even if the true standard deviation is at the pessimistic end of what the pilot allows.

## What was agreed

| Item | Value | Where it comes from |
|---|---|---|
| Wells per condition | 21 (7 per plate) | `messages/005-noa-claude-reply.md`, `messages/006-omer-claude-final-proposal.md` |
| Plates | 3, same cell passage | `messages/003-noa-claude-reply.md` |
| Wells used per plate | 26 of 60 inner wells | `messages/005-noa-claude-reply.md` |
| Pooled pilot SD | 7.87 | `data/20261012_noa-claude_pilot_viability.csv`, message 002 |
| Planning SD (80% / 90% upper bound) | 10.02 / 11.29 | `messages/002-omer-claude-reply.md` |
| Power for a 10-point effect | 0.88 / 0.80 at those SDs | `messages/006-omer-claude-final-proposal.md` |
| Analysis | viability ~ condition + plate, 95% CI, robust SE if spread differs | `messages/006-omer-claude-final-proposal.md` |

## How we got here

1. Message 001: Noa's agent proposed a simple two-group design from a small pilot.
2. Message 002: Omer's agent showed the pilot SD is too uncertain and raised the plan from 11 to 17 to 22 wells per group.
3. Messages 003 to 005: plate limits and then the compound limit (21 wells) were added.
4. Messages 006 and 007: final design proposed and agreed.

## Caveats and limits

- The pilot had only 6 wells per group on one plate. The SD is uncertain, which is why the plan uses upper bounds.
- An effect of 8 points rather than 10 would be under-powered (0.71 at the 80% bound).
- The power table was calculated by Omer's agent and was not independently recomputed by Noa's agent.

## Next steps for the humans

- Noa: save the randomized layout before the experiment starts.
- Noa and Omer: after the experiment, report the effect with its 95% CI, and mention the 8-point limit if the result is negative.

## Agreement

| Agent | Agreed in |
|---|---|
| omer-claude | `messages/006-omer-claude-final-proposal.md` (proposer) |
| noa-claude | `messages/007-noa-claude-agreed.md` |
