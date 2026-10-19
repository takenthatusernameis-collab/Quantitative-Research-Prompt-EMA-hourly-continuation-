# NEXT AGENT TASK

## Objective
**Batch 5 grid (N 57) COMPLETE.** All 3,762 cells (57 symbols x 66 EMA pairs) rejected.
Per PROMPT.md §2.1 the program must expand again: **N 57 -> 67** (batch 6, next 10
lower-market-cap names), fetch a fresh ranking snapshot, download OHLCV for the 10 new
names, run the full 66-pair grid (resume `results/20261019_135940_grid`), checkpoint per
symbol, re-aggregate, and report the cumulative rejection rate.

**Do not stand down.** A prior rejection does not stop the program (PROMPT.md §2.1.4).

## State at handoff (2026-10-19)
- Universe: **N = 57** (`universe/mcap_rank.json`), snapshot `mcap_snapshot_20261019_185635`
  (CoinGecko `/api/v3/coins/markets`, fetched 2026-10-19T18:56:35Z). Batch 5 added
  ZRO, CAKE, STX, APT, ETHFI, XDC, DASH, TIA, BDX, CRV.
- Grid: **3,762 / 3,762 cells complete** in `results/20261019_135940_grid/` (57 symbols x
  66 pairs). 0 cells with net PF > 1; 3,762 rejected; 0 blocked; 0 exploratory.
- Pooled (net of costs, full sample, 10 bps taker + 2 bps slippage per side):
  mean net PF 0.4548, median 0.4697, **best net PF 0.9523** (WLD/USDT P20_200).
- Cumulative rejection rate: **3,762 / 3,762 cells (100 %)** across 57 symbols.
- Tests: **37 passed** (`python -m pytest tests/ -q`).

## Next batch (batch 6, N 57 -> 67) - concrete steps
1. `python scripts/fetch_mcap_snapshot.py --pages 4 --batch-size 10` (dry run) to see
   the next 10 names below the CRV floor, then `--apply` to write `universe/mcap_rank.json`.
   Expected candidates: PYTH, FLR, RAY, STRK, FET, SEI, PENDLE, BSV, BTT, XTZ.
2. `python scripts/fetch_kucoin.py --target-bars 22000 --symbols <the 10 new names>`
3. For each new symbol in market-cap descending order, one invocation each:
   `PYTHONPATH=. python scripts/run_grid.py --n <N> --resume results/20261019_135940_grid --note "universe expansion batch 6: N 57 -> 67 (<SYMBOL>/USDT, 66-pair EMA grid)"`
   then `PYTHONPATH=. python scripts/remote_checkpoint.py --message "chore(kilo): grid batch6 <SYMBOL>/USDT (66 cells, N=67)"`.
4. `PYTHONPATH=. python scripts/aggregate_grid.py --run results/20261019_135940_grid`.
5. Append the batch-6 section to `universe/mcap_expansion_log.md`.
6. Update this handoff and `INITIAL_TASK_FOR_NEXT_AGENT.md`, then checkpoint.

## Validation Command
`python -m pytest tests/ -q`
