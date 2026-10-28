---
title: Reconcile enzyme activity between two labs: solution
status: solved-pending-human-review
date: 2026-10-18
written_by: yossi-claude
---
# Solution

## The answer

The 2-fold gap between the labs is caused by the **assay temperature**: Lab A measured at 25 °C and Lab B at 37 °C. When Lab A repeated six aliquots at 37 °C, it agreed with Lab B (ratio 1.01, 90% CI 0.94 to 1.08, inside the required 0.80 to 1.25). Both labs will use 37 °C, and old Lab A data at 25 °C are converted by a factor of 2.24.

## What was agreed

| Item | Value | Where it comes from |
|---|---|---|
| Original gap (Lab B / Lab A) | 2.25, 95% CI 2.18 to 2.32 | `messages/003-ravi-claude-critique.md` |
| Cause | Assay temperature, 25 °C vs 37 °C | `data/20261012_dana-claude_labA_25C.csv`, `data/20261013_yossi-claude_labB_37C.csv` |
| Bridging agreement (Lab A at 37 °C / Lab B) | 1.01, 90% CI 0.94 to 1.08 | `messages/006-ravi-claude-final-proposal.md`, `data/20261016_dana-claude_labA_37C_bridge.csv` |
| Common protocol | 37 °C for both labs | `messages/006-ravi-claude-final-proposal.md` |
| Conversion for old 25 °C Lab A data | multiply by 2.24 (95% CI 2.14 to 2.34); keep original values in a separate column | `messages/006-ravi-claude-final-proposal.md`, `messages/007-dana-claude-agreed.md` |

## How we got here

1. Messages 001 and 002: both labs shared results for the same 10 aliquots and Yossi's agent listed four possible causes.
2. Message 003: Ravi's agent tested them on the data. The gap is a constant factor, not units, dilution or offset. Temperature fits.
3. Message 004: Lab A reran six aliquots at 37 °C.
4. Messages 005 and 006: Yossi raised historical data and the limits of six samples; Ravi's agent ran the equivalence check and proposed the solution.
5. Messages 007 and 008: Dana's and Yossi's agents agreed.

## Caveats and limits

- Only six aliquots were rerun, and the two highest-activity ones were not. The factor is untested above about 35 U/mL (Lab A at 25 °C).
- One enzyme and one serum pool. Do not apply the factor to other assays or use it to extrapolate to other temperatures.
- The aliquots had one earlier freeze and thaw.

## Next steps for the humans

- Dana: switch Lab A's reader to 37 °C and relabel historical data as converted.
- Dana and Yossi: when new aliquots are available, run S02 and S06 to cover the top of the range.
- Ravi: re-check the factor if either lab changes substrate lot or reader.

## Agreement

| Agent | Agreed in |
|---|---|
| ravi-claude | `messages/006-ravi-claude-final-proposal.md` (proposer) |
| dana-claude | `messages/007-dana-claude-agreed.md` |
| yossi-claude | `messages/008-yossi-claude-agreed.md` |
