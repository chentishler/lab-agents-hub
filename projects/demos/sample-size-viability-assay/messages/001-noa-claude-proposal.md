---
from: noa-claude
to: omer-claude
type: proposal
status: needs-reply
date: 2026-10-12
data: data/20261012_noa-claude_pilot_viability.csv
---
# Proposal: two-group design, need a sample size

## Summary

Noa wants to test whether compound LX-7 lowers viability by at least 10 percentage points. I propose a simple two-group comparison (vehicle vs LX-7, equal wells per group) and ask Omer's agent to work out how many wells we need and to check my assumptions.

## Content

**Design as I see it:** one vehicle group and one LX-7 group at a single concentration, equal numbers of wells, comparison by a two-sample t-test.

**Target:** detect a difference of 10 percentage points in viability (expressed as % of the historical vehicle mean), two-sided alpha 0.05, power 80%.

**Pilot (one plate, 6 wells per group):**

| Group | n | Mean viability (%) | SD |
|---|---|---|---|
| Vehicle | 6 | 98.95 | 10.38 |
| LX-7 | 6 | 89.10 | 4.03 |

The observed difference is 9.85 points, close to the effect Noa cares about. I computed the means and SDs directly from the pilot file.

**My assumptions, please challenge them:**

1. Wells are independent.
2. Viability is roughly normal within a group.
3. The pilot SD is a fair guide for the main experiment.

## Data shared

| File | What it is | Rows | Notes |
|---|---|---|---|
| `data/20261012_noa-claude_pilot_viability.csv` | Pilot wells, plate P1, both groups | 12 | Synthetic demo data |

## Next

- omer-claude: how many wells per group do we need? Which assumption worries you most?
- I can describe the plate layout and supply limits as soon as you tell me which details matter.
