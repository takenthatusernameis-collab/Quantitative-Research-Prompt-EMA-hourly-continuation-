# NEXT AGENT TASK

## Objective
**Batch 7 grid (N 77) COMPLETE.** All 5,082 cells (77 symbols x 66 EMA pairs) rejected.
Per PROMPT.md §2.1 the program must expand again: **N 77 -> 87** (batch 8, next 10
lower-market-cap names), fetch a fresh ranking snapshot, download OHLCV for the 10 new
names, run the full 66-pair grid (resume `results/20261019_135940_grid`), checkpoint per
symbol, re-aggregate, and report the cumulative rejection rate.

**Do not stand down.** A prior rejection does not stop the program (PROMPT.md §2.1.4).

## State at handoff (2026-10-19)
- Universe: **N = 77** (`universe/mcap_rank.json`), snapshot `mcap_snapshot_20261019_204714`
  (CoinGecko `/api/v3/coins/markets`, fetched 2026-10-19T20:47:14Z). Batch 7 added
  XTZ, LDO, SUN, BAT, OP, CFX, GRT, DCR, BONK, LUNC (each ~22,000 clean hourly bars
  from KuCoin, no gaps, no duplicates).
- Grid: **5,082 / 5,082 cells complete** in `results/20261019_135940_grid/` (77 symbols x
  66 pairs). 0 cells with net PF > 1; 5,082 rejected; 0 blocked; 0 exploratory.
- Pooled (net of costs, full sample, 10 bps taker + 2 bps slippage per side):
  mean net PF 0.4629, median 0.4806, **best net PF 0.9523** (WLD/USDT P20_200).
- Cumulative rejection rate: **5,082 / 5,082 cells (100 %)** across 77 symbols.
- Batch 7 alone: 660 / 660 rejected, pooled mean net PF 0.4682, best 0.9087
  (GRT/USDT P20_200).
- Per-pair pooled leaders (mean net PF over 77 symbols): P8_200 0.6605, P20_200 0.6579,
  P12_200 0.6502. Worst: P20_21 0.1177, P50_55 0.1739, P8_12 0.1762.
- Tests: **37 passed** (`python -m pytest tests/ -q`).

## Next batch (batch 8, N 77 -> 87) - concrete steps
1. `python scripts/fetch_mcap_snapshot.py --pages 4 --batch-size 10` (dry run) to see
   the next 10 names below the LUNC floor, then
   `python scripts/fetch_mcap_snapshot.py --apply-from universe/mcap_snapshot_<TS>.json --batch-size 10 --apply`
   to write `universe/mcap_rank.json` from the reviewed snapshot.
   Expected candidates (from the 20:47 snapshot, to be re-checked on a fresh fetch):
   AR, NFT, JTO, JASMY, ENS, EIGEN, KMNO, FLOKI, COMP, RUNE.
   (Note: AR = Arweave, not ARB; RUNE = THORChain.)
2. `python scripts/fetch_kucoin.py --target-bars 22000 --symbols <the 10 new names>`
   (takes ~35 min; 10 symbols x ~220 paginated KuCoin requests).
3. For each new symbol in market-cap descending order, one invocation each:
   `PYTHONPATH=. python scripts/run_grid.py --n <N> --resume results/20261019_135940_grid --note "universe expansion batch 8: N 77 -> 87 (<SYMBOL>/USDT, 66-pair EMA grid)"`
   where `--n` is the 1-based position of that symbol in the 87-symbol ranking
   (--n 78 for the first new symbol up to --n 87 for the last; do not use a single
   `--n 87` pass, so each symbol can be checkpointed on its own).
   then `PYTHONPATH=. python scripts/remote_checkpoint.py --message "chore(kilo): grid batch8 <SYMBOL>/USDT (66 cells, N=87)" --paths results/20261019_135940_grid`.
   Each symbol takes ~2.5 min; the per-symbol checkpoint keeps every push delta
   inside the controller's 30 s budget.
4. `PYTHONPATH=. python scripts/aggregate_grid.py --run results/20261019_135940_grid`.
5. Append the batch-8 section to `universe/mcap_expansion_log.md`.
6. Update this handoff and `INITIAL_TASK_FOR_NEXT_AGENT.md`, then checkpoint.

## Validation Command
`python -m pytest tests/ -q`
