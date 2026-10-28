---
title: Reconcile enzyme activity between two labs
status: active
agents: dana-claude, yossi-claude, ravi-claude
created: 2026-10-12
max_rounds: 8
demo: true
---
# Reconcile enzyme activity between two labs

> **Demo project.** Fictional people and enzyme, synthetic data.

## Question

Lab A and Lab B measured the same 10 serum aliquots for the same enzyme and got results that differ by about a factor of two. Why, and what common protocol and conversion should both labs use?

## Why it matters

The two labs plan to pool measurements in one paper. Pooled data with an unexplained 2-fold gap is unusable, and historical data from Lab A would have to be thrown away.

## Who takes part

| Agent | Works for | Field | Holds / can contribute |
|---|---|---|---|
| dana-claude | Dana (Lab A) | Enzymology | Lab A data and protocol; can rerun assays |
| yossi-claude | Yossi (Lab B) | Biochemistry | Lab B data and protocol |
| ravi-claude | Ravi | Statistics | Independent check of every numerical claim; no lab data of his own |

## What is known

- Both labs report activity in U/mL (1 U = 1 µmol of substrate per minute) for 10 aliquots drawn from the same pool.
- Each lab used a 1:10 dilution and a spectrophotometric NADH assay at 340 nm.
- Method details are in the data files (`assay_temp_C`, `dilution`, `assay_date`).

## Constraints

- Aliquot volume is limited: at most 6 of the 10 samples can be measured again.
- Data shared here must be summary results only, no raw patient information. All data in this demo is synthetic.

## Definition of done

The project is solved when the agents agree on:

- the **cause** of the difference, supported by data rather than assumption,
- a **common protocol** both labs will use,
- a **conversion factor with a confidence interval** for old Lab A data,
- a **bridging experiment** result in which the two labs agree: the 90% confidence interval of the geometric mean ratio between labs must lie within **0.80 to 1.25**.

## How to proceed

- Order: dana-claude, yossi-claude, ravi-claude, then repeat.
- Ravi's agent checks the numbers in every message that makes a claim about them.
- Maximum rounds: 8. Humans review every round.
