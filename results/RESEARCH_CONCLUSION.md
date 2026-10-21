# Research Conclusion — EMA Hourly Continuation

## Program status (2026-10-21T01:05Z)

**The research program is NOT concluded.** It is in the waiting state
`AWAITING_NEW_ELIGIBLE_CANDIDATES`: the current market-cap snapshot
(`mcap_snapshot_20261020_113004`, CoinGecko, 2026-10-20T11:30:04Z) has no
eligible unseen name below the expansion floor (TAIKO/USDT, $15 436 339), and
PROMPT.md §2.1.5 forbids a fresh ranking query before
**2026-10-21T11:30:04Z** (24 h refresh bound).

What the evidence says so far:

- **No edge has survived the gates.** Across **17 556 grid cells** (266 symbols
  x 66 EMA pairs, 14.2 M trades, net of costs), the pooled net profit factor is
  **0.5224**; only **36 cells (0.21 %)** reach a full-sample net PF > 1 against a
  ~50 % no-edge null, and every one of them fails the out-of-sample and 2x-cost
  gates. **0 credible candidates.**
- **The out-of-sample gate now covers the whole grid, not a selected subset.**
  The pipeline used to test only the 36 in-sample winners out of sample, which
  left 17 520 cells unexamined. `scripts/oos_grid_scan.py` applies the same
  out-of-sample window to all 17 556 cells and re-verifies the survivors with
  the real backtest: pooled out-of-sample net PF **0.5299** (0.3267 under 2x
  costs), 77 cells (0.44 %) with an out-of-sample net PF > 1, and **0 credible
  candidates** among the 180 verified survivors (76 exploratory, 104 rejected).
  The 6 closest survivors all have a full-sample net PF below 1 (0.75-0.91)
  and none keeps a stressed out-of-sample PF > 1 at 20 %, 35 % and 50 %
  window lengths.
- **The rejection is not an artefact of the sample.** Dropping the 5/10/20/50
  largest market caps does not change the sign or the magnitude of the result
  (pooled net PF 0.5224 -> 0.5303), every market-cap rank bucket is below 1.0,
  and 31 of the 36 above-PF cells are fragile across time slices
  (`results/20261020_235449_robustness/`).
- **The program continues by policy.** PROMPT.md §2.1.4 is explicit: a failed
  symbol, a failed pair, or a failed batch never stops the program. The
  universe expands with the next lower market-cap names, each through the full
  66-pair grid, until expansion is impossible or the user cancels.

## What supersedes the 2026-10-19 conclusion

The 2026-10-19 note ("research concluded, no further experiments authorised")
came from the 5-symbol baseline study (BTC/ETH/SOL/BNB/XRP) and predates the
mandatory expansion rule of PROMPT.md §2.1. It is kept in
`results/FINAL_DECISION.md` as the historical record of that study. The
baseline conclusion itself has not changed: the strategy is rejected on
out-of-sample, net-of-costs evidence — with far more evidence than it had then.

## Rules that keep applying

- Never promote a cell on in-sample performance: a credible candidate needs net
  OOS PF > 1, net OOS Sharpe > 0, >= 30 OOS trades, and net PF > 1 under 2x
  costs in both the full sample and the OOS window.
- Never treat a negative batch as a program stop; expand instead.
- No live trading.
