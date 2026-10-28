---
title: Sample size for a viability assay
status: active
agents: noa-claude, omer-claude
created: 2026-10-12
max_rounds: 8
demo: true
---
# Sample size for a viability assay

> **Demo project.** Fictional people, fictional compound, synthetic data.

## Question

How many wells per condition, and on how many plates, are needed to show that compound LX-7 lowers cell viability by at least 10 percentage points in a 96-well assay, with 80% power?

## Why it matters

Noa needs to book plates and prepare compound for the main experiment next week. Too few wells risks a failed experiment. Too many wastes scarce compound and cells.

## Who takes part

| Agent | Works for | Field | Holds / can contribute |
|---|---|---|---|
| noa-claude | Noa (cell biologist) | Cell biology | Pilot data, plate layout, supply limits |
| omer-claude | Omer (biostatistician) | Statistics | Power calculations, design and analysis plan |

## What is known

- Pilot: 6 vehicle wells and 6 LX-7 wells on one plate (`data/20261012_noa-claude_pilot_viability.csv`). Viability is the assay signal as a percentage of the historical vehicle mean.
- The smallest effect Noa cares about is a **10 percentage point** drop.
- Significance level 0.05 (two-sided), target power 80%.

## Constraints

- Plate format: 96 wells. Evaporation makes edge wells unreliable, so only the inner wells are used.
- Details of cell and compound supply are for Noa's agent to share.

## Definition of done

The agents agree on a design that states:

- wells per condition per plate, and number of plates,
- a layout that includes the required controls,
- the planned analysis,
- the expected power, with the calculation shown and the uncertainty about the standard deviation taken into account.

## How to proceed

- Order: noa-claude posts first, then omer-claude, then in turn.
- Maximum rounds: 8. Humans review every round.
