# Pre-registration — PROMPT.md §5.2 ATR minimum-risk mutation (full grid)

**Registered:** 2026-10-21T12:50:00Z, before the child run was started.
**ID:** `atr_min_risk_1.0_full_grid_20261021`

## The mutation

PROMPT.md §5.2 lists the optional mutations in order. This one is extension
#2: an ATR-based minimum-risk filter, i.e. skip a trade whose stop distance is
narrower than a multiple of ATR14.

It is the only optional mutation that moved the cost drag materially. The
cost-drag leg (`results/20261021_102500_cost_drag_leg`) measured, on 200
re-run cells that reproduce the stored grid summary exactly, a mean net PF of
**0.2281** on the parent and **0.5460** on the child, on 17 929 trades instead
of 75 005. The mechanism is documented there: the cost of a trade as a share of
its gross P&L is `2 * cost_per_side / risk_pct`, and the median cell's stop
distance is 0.912 % of the entry price.

## Parent

`results/20261019_135940_grid` — 266 symbols x 66 EMA pairs = 17 556 cells,
full sample, 10 bps taker + 2 bps slippage per side, RR 1:1 to EMA_slow,
conservative (adverse-first) same-bar exit, risk-based sizing at 1 % of equity
with a 10x notional cap, `min_risk_atr` off.

## Child

The same grid with one change: `min_risk_atr = true`, `atr_threshold = 1.0`.
Same symbols, same 66 pairs, same costs, same fill rule, same conflict rule,
same sizing.

```
PYTHONPATH=. python3 scripts/run_grid.py --n 266 --min-risk-atr --atr-threshold 1.0 \
  --engine fast --note 'pre-registered PROMPT.md 5.2 ATR minimum-risk mutation'
```

The child writes to its own run directory. **The baseline grid is not
replaced.**

`--engine fast` selects the array twin of the signal generator and of the
backtest engine. The twin is proved equivalent to the research path:
`results/signal_equivalence_check.json` (268 symbols, 1 360 cells, no
mismatch) and `results/20261021_130000_grid_repro_fast` (200 of 200 sampled
baseline cells re-run through the fast path reproduce their stored summaries
exactly).

## What will be measured

**Primary.** The pooled out-of-fold net PF of the selection procedure, under
the identical walk-forward protocol of the survivor selection audit
(`results/20261021_121629_survivor_selection_audit`, leg 3): the full sample
of every symbol is cut into 5 sequential folds; at step k the best cell is
chosen on the history (folds 1..k, at least 20 trades) and scored on fold
k+1, which the selection never saw. The parent's yardstick on this yardstick
is **pooled out-of-fold net PF 0.6409** (0.4521 under 2x costs) over 1060
steps and 95 786 out-of-fold trades.

**Secondary.**

- pooled full-sample net PF, gross PF and trade count, child against parent;
- the share of out-of-fold windows with net PF above 1, and above 1 under 2x
  costs;
- how many cells clear the grid-wide OOS gate (out-of-sample net PF > 1, at
  least 30 out-of-sample trades, still > 1 under 2x costs): the parent has 10
  of 17 556;
- the cost share of the gross P&L, recomputed on the child.

## Decision rule, fixed in advance

The child is promoted to a **credible candidate** only if

1. its pooled out-of-fold net PF under the identical walk-forward protocol is
   above 1.0, **and**
2. it is still above 1.0 under 2x costs, **and**
3. at least one cell clears the OOS + 2x-cost gate with at least 30
   out-of-sample trades.

If any of the three fails, the child is recorded as a **rejected mutation**,
whatever its in-sample numbers look like. A child that only narrows the gap
between gross and net without crossing those gates is a cost-drag repair, not
an edge — that distinction is the point of the leg.

No gate is relaxed to accommodate the child, and a negative result does not
stop the program.
