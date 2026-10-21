# Selection Granularity Leg

**Grid:** `results/20261019_135940_grid`
**Generated:** 2026-10-21T18:52:26.798888+00:00
**Symbols:** 266 (17556 cells)
**Folds:** 5 sequential folds of the full sample of every symbol

## Leg A - the per-symbol selection (Leg 3 of the audit)

| Measure | Value |
|---|---|
| Steps scored | 1060 |
| Out-of-fold trades | 95786 |
| Pooled out-of-fold net PF | 0.6409 |
| Pooled out-of-fold net PF (2x costs) | 0.4521 |
| Out-of-fold windows with net PF > 1 | 86 |
| Share of out-of-fold windows with net PF > 1 | 8.1% |
| Median in-fold net PF of the selected cell | 0.8272 |
| Median out-of-fold net PF of the selected cell | 0.6217 |

## Leg B - the same walk-forward at a coarser granularity

One selection per market-cap family instead of one per symbol: the best EMA pair of the family is chosen on the history and scored on the fold the selection never saw.

| Family | Symbols | Steps | Out-of-fold trades | Pooled OOF net PF | Pooled OOF net PF (2x costs) | Windows with PF > 1 |
|---|---|---|---|---|---|---|
| top 5 by market cap | 5 | 4 | 1554 | 0.5401 | 0.3082 | 0 (0.0%) |
| top 10 by market cap | 10 | 4 | 3118 | 0.5816 | 0.3564 | 0 (0.0%) |
| top 25 by market cap | 25 | 4 | 7469 | 0.6312 | 0.4268 | 0 (0.0%) |
| top 50 by market cap | 50 | 4 | 14824 | 0.6354 | 0.4372 | 0 (0.0%) |
| top 100 by market cap | 100 | 4 | 29631 | 0.6546 | 0.4628 | 0 (0.0%) |

## Leg C - the random control

The same per-symbol walk-forward with a *random* eligible cell picked at every step, 200 replicates, seed 20261021.

| Measure | Value |
|---|---|
| Median pooled out-of-fold net PF | 0.5601 |
| Mean pooled out-of-fold net PF | 0.5604 |
| 5th percentile | 0.5529 |
| 95th percentile | 0.5688 |
| Min / max | 0.5462 / 0.5753 |
| Median pooled out-of-fold net PF (2x costs) | 0.3611 |
| Percentile of the per-symbol selection | 100.0% |

## Verdict

- The per-symbol selection scores 0.6409 pooled out-of-fold net PF over 95786 trades (0.4521 under 2x costs), with 8.1% of the out-of-fold windows above profit factor 1.
- The same walk-forward with one selection for the whole market-cap family of 100 symbols scores 0.6546 (0.4628 under 2x costs) on 29631 trades.
- The random control - the same walk-forward with a random eligible cell picked at every step - scores a median pooled out-of-fold net PF of 0.5601 (p05 0.5529, p95 0.5688) over 200 replicates.
- The per-symbol selection sits at the 100.0% percentile of the random control, so the selection is worth something over a random pick out of fold.
- The out-of-fold result survives the coarser selection, so it is not an artefact of the selection granularity.
- Either way the number stays below 1 out of fold: the program still has no rule that clears the PROMPT.md §3.4 gate out of sample.
