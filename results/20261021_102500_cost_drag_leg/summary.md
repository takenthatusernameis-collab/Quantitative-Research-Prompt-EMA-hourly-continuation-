# Cost-Drag Decomposition — EMA Hourly Continuation

**Source run:** `results/20261019_135940_grid`
**Generated:** 2026-10-21T10:31:40.182844+00:00
**Universe:** 266 symbols, 17556 grid cells
**OOS window:** trailing 35% of each symbol's bars, entries restricted to the window
**Cost model:** 10.0 bps taker + 2.0 bps slippage per side

## The mechanism

With risk-based sizing the gross P&L of a trade is a fixed fraction of the equity (a trade exits at exactly `+-risk`), while the cost of the trade is proportional to the notional, `equity * risk_fraction / risk_pct`. So the cost of a trade as a share of its gross P&L is

```
cost / |gross P&L| = 2 * cost_per_side / risk_pct
```

The cost of the rule is therefore set by the *width of the stop*, not by the number of trades. A cell whose entries sit 1 % from the slow EMA pays ~22 % of its gross P&L in fees; a cell whose entries sit 0.25 % away pays ~96 %.

## Leg 1 — the grid-wide decomposition

| Metric | Value |
|---|---|
| Cells decomposed | 17491 |
| Trades in the window | 5128510 |
| Pooled gross profit factor | 0.8877 |
| Pooled net profit factor | 0.5298 |
| Costs paid | 17,840,159 |
| Gross P&L | -3,997,685 |
| Net P&L | -21,837,844 |
| Cost share of the gross P&L | 26.6% |
| Median risk distance | 0.912% |
| Trades whose notional is capped | 2.6% |
| Median cost per trade, share of gross P&L | 26.4% |
| Model at the median risk distance | 26.3% |

### Per-cell distributions

| Statistic | Gross PF | Net PF | Cost share of gross | Median risk | Capped trades |
|---|---|---|---|---|---|
| mean | 0.8297 | 0.4319 | 39.0% | 1.254% | 2.1% |
| median | 0.8322 | 0.4342 | 33.1% | 1.119% | 1.1% |
| p05 | 0.5545 | 0.1446 | 17.1% | 0.424% | 0.0% |
| p25 | 0.7286 | 0.3060 | 24.7% | 0.762% | 0.4% |
| p75 | 0.9317 | 0.5463 | 46.8% | 1.604% | 2.3% |
| p95 | 1.1081 | 0.7201 | 80.0% | 2.489% | 7.7% |
| max | 2.1072 | 1.9955 | 267.8% | 26.131% | 57.9% |
| min | 0.0000 | 0.0000 | 1.0% | 0.062% | 0.0% |

### What the costs decide

| Question | Answer |
|---|---|
| Cells with gross PF > 1 (no cost at all) | 2387 |
| Cells with net PF > 1 (registered cost model) | 77 |
| Cells with net PF > 1 that are gross losers | 0 |
| Cells with gross PF > 1 that are net losers | 2310 |
| Cells where costs take more than half the gross P&L | 3735 |

## Leg 2 — the sizing legs (re-run)

Cells re-run: 200 (one per symbol, market-cap order).

| Leg | Cells | Trades | Mean gross PF | Mean net PF | Mean net PF (2x costs) | Median risk |
|---|---|---|---|---|---|---|
| base | 199 | 75005 | 0.7297 | 0.2281 | 0.0826 | 0.564% |
| uncapped | 199 | 74580 | 0.7248 | 0.2091 | 0.0744 | 0.565% |
| atr_min_risk | 199 | 17929 | 0.8612 | 0.5460 | 0.3382 | 1.252% |

`uncapped` removes the `max_notional_multiple` cap (pure risk-based sizing, no leverage limit); `atr_min_risk` is the PROMPT.md §5.2 pre-registered mutation that skips trades whose risk distance is below one ATR(14). Both are diagnostics of the baseline, not candidate configurations.

Reproduction check: 200 of 200 re-run cells reproduce the stored grid summary (net profit factor and trade count) exactly.

## Verdict

- The median cell trades at a risk distance of 0.912% of the entry price, and the model `2 * cost_per_side / risk_pct` predicts a cost of 26.3% of the gross P&L against a measured 26.4% - the cost of the rule is a function of the stop width, not of the number of trades.
- Costs take 26.6% of the gross P&L of the grid, and 3735 of 17556 cells lose more than half of their gross P&L to fees and slippage.
- Without any cost, 2387 cells would show a profit factor above 1; with the registered cost model only 77 do. The grid's headline number is mostly a statement about the cost model.
- Skipping the trades with a risk distance below one ATR(14) - the PROMPT.md §5.2 mutation - moves the mean net PF of the re-run sample from 0.2281 to 0.5460 and the mean gross PF from 0.7297 to 0.8612, on 17929 trades instead of 75005. The mutation buys back the cost drag; it does not create an edge, and it leaves the sample thinner.
- Removing the notional cap moves the mean net PF of the re-run sample from 0.2281 to 0.2091; the cap binds on 2.6% of the trades, and those trades pay several times their gross P&L in costs.
