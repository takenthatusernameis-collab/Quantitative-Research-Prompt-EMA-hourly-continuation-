# NEXT AGENT TASK

## Objective
**Batch 6 grid (N 67) COMPLETE.** All 4,422 cells (67 symbols x 66 EMA pairs) rejected.
Per PROMPT.md §2.1 the program must expand again: **N 67 -> 77** (batch 7, next 10
lower-market-cap names), fetch a fresh ranking snapshot, download OHLCV for the 10 new
names, run the full 66-pair grid (resume `results/20261019_135940_grid`), checkpoint per
symbol, re-aggregate, and report the cumulative rejection rate.

**Do not stand down.** A prior rejection does not stop the program (PROMPT.md §2.1.4).

## State at handoff (2026-10-19)
- Universe: **N = 67** (`universe/mcap_rank.json`), snapshot `mcap_snapshot_20261019_200749`
  (CoinGecko `/api/v3/coins/markets`, fetched 2026-10-19T20:07:49Z). Batch 6 added
  VET, PYTH, FLR, RAY, STRK, FET, SEI, PENDLE, BSV, BTT (each 22,000 clean hourly bars
  from KuCoin, no gaps, no duplicates).
- Grid: **4,422 / 4,422 cells complete** in `results/20261019_135940_grid/` (67 symbols x
  66 pairs). 0 cells with net PF > 1; 4,422 rejected; 0 blocked; 0 exploratory.
- Pooled (net of costs, full sample, 10 bps taker + 2 bps slippage per side):
  mean net PF 0.4621, median 0.4800, **best net PF 0.9523** (WLD/USDT P20_200).
- Cumulative rejection rate: **4,422 / 4,422 cells (100 %)** across 67 symbols.
- Per-pair pooled leaders (mean net PF over 67 symbols): P8_200 0.6587, P20_200 0.6572,
  P12_200 0.6519. Worst: P20_21 0.1167, P50_55 0.1708, P8_12 0.1752.
- Tests: **37 passed** (`python -m pytest tests/ -q`).

## Next batch (batch 7, N 67 -> 77) - concrete steps
1. `python scripts/fetch_mcap_snapshot.py --pages 4 --batch-size 10` (dry run) to see
   the next 10 names below the BTT floor, then
   `python scripts/fetch_mcap_snapshot.py --apply-from universe/mcap_snapshot_<TS>.json --batch-size 10 --apply`
   to write `universe/mcap_rank.json` from the reviewed snapshot.
   Expected candidates (from the 20:07 snapshot, to be re-checked on a fresh fetch):
   XTZ, LDO, SUN, OP, BAT, CFX, GRT, DCR, BONK, LUNC.
2. `python scripts/fetch_kucoin.py --target-bars 22000 --symbols <the 10 new names>`
3. For each new symbol in market-cap descending order, one invocation each:
   `PYTHONPATH=. python scripts/run_grid.py --n <N> --resume results/20261019_135940_grid --note "universe expansion batch 7: N 67 -> 77 (<SYMBOL>/USDT, 66-pair EMA grid)"`
   where `--n` is the 1-based position of that symbol in the 77-symbol ranking
   (--n 68 for the first new symbol up to --n 77 for the last; do not use a single
   `--n 77` pass, so each symbol can be checkpointed on its own).
   then `PYTHONPATH=. python scripts/remote_checkpoint.py --message "chore(kilo): grid batch7 <SYMBOL>/USDT (66 cells, N=77)" --paths results/20261019_135940_grid`.
4. `PYTHONPATH=. python scripts/aggregate_grid.py --run results/20261019_135940_grid`.
5. Append the batch-7 section to `universe/mcap_expansion_log.md`.
6. Update this handoff and `INITIAL_TASK_FOR_NEXT_AGENT.md`, then checkpoint.

## Validation Command
`python -m pytest tests/ -q`
