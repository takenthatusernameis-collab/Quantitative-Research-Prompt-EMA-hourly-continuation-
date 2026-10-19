# NEXT AGENT TASK

## Objective
**Batch 3 grid (N 37) COMPLETE.** All 2,442 cells (37 symbols x 66 EMA pairs) rejected.
Per PROMPT.md §2.1 the program must expand again: **N 37 -> 47** (batch 4, next 10
lower-market-cap names), fetch a fresh ranking snapshot, download OHLCV for the 10 new
names, run the full 66-pair grid (resume `results/20261019_135940_grid`), checkpoint per
symbol, re-aggregate, and report the cumulative rejection rate.

**Do not stand down.** A prior rejection does not stop the program (PROMPT.md §2.1.4).

## State at handoff (2026-10-19)
- Universe: **N = 37** (`universe/mcap_rank.json`), snapshot `mcap_snapshot_20261019_163400`
  (CoinGecko `/api/v3/coins/markets`, fetched 2026-10-19T16:34:00Z). Batch 3 added
  DOT, WLD, MNT, PEPE, SKY, ICP, HTX, ARB, ETC, JST (all below the ONDO floor of
  2 122 015 803 USD; order preserved, max rank drift vs batch 2 = 2.33 %).
- Grid: **2,442 / 2,442 cells complete** in `results/20261019_135940_grid/` (37 symbols x
  66 pairs). 0 cells with net PF > 1; 2,442 rejected; 0 blocked; 0 exploratory.
- Pooled (net of costs, full sample, 10 bps taker + 2 bps slippage per side):
  1,999,202 trades, mean net PF 0.4446, median 0.4544, **best net PF 0.9523**
  (WLD/USDT P20_200), mean net Sharpe -7.8763, max net Sharpe -0.1979.
- Multiple-testing context: 0/2,442 cells above PF 1 vs a ~50 % no-edge null (-50.0 %
  excess). Every symbol and every EMA pair is net-unprofitable; the best pair
  (P12_200, mean PF 0.6440) and worst pair (P20_21, mean PF 0.1028) are both below 1.
- Batch 3 per-symbol (mean / best net PF): DOT 0.4953 / 0.7386, WLD 0.6452 / 0.9523,
  MNT 0.3993 / 0.7686, PEPE 0.5425 / 0.7397, SKY 0.5268 / 0.7684, ICP 0.4902 / 0.7261,
  HTX 0.2378 / 0.4204, ARB 0.5229 / 0.8707, ETC 0.4216 / 0.6404, JST 0.3207 / 0.6388.
- Cumulative rejection rate: **2,442 / 2,442 cells (100 %)** across 37 symbols.
- Data: 37 fixtures in `data/fixtures/` (22k hourly bars each, KuCoin 1h UTC);
  provenance in `data/fixtures/fetch_manifest.json`. SKY has 17,934 bars (listed
  2024-10-02 on KuCoin) - the only short sample; still above the 2-year floor.
- Tests: **37 passed** (`python -m pytest tests/ -q`).
- Git: tracked tree clean and pushed; every batch-3 symbol has its own durable
  checkpoint commit (DOT, WLD, MNT, PEPE, SKY, ICP, HTX, ARB, ETC, JST, then the
  aggregate). `PYTHONPATH=.` is required for all `scripts/` entry points.
- Universe is **not** exhausted: the 16:34 snapshot still holds 110 eligible names
  below JST (KCS, ALGO, KAS, POL, JUP, ATOM, RENDER, INJ, FIL, AERO, ...), so
  expansion to N = 47 is feasible and required.

## Next batch (batch 4, N 37 -> 47) - concrete steps
1. `python scripts/fetch_mcap_snapshot.py --pages 4 --batch-size 10` (dry run) to see
   the next 10 names below the JST floor, then `--apply` to write `universe/mcap_rank.json`.
   Expected candidates (16:34 snapshot, re-verify with the fresh fetch): KCS, ALGO, KAS,
   POL, JUP, ATOM, RENDER, INJ, FIL, AERO.
2. `python scripts/fetch_kucoin.py --target-bars 22000 --symbols <the 10 new names>`
   (KuCoin 1h UTC, ~2 min per symbol; SKY-class short listings simply return fewer bars).
3. For each new symbol in market-cap descending order, one invocation each, so
   `progress.json` is written after every symbol and each symbol gets its own
   durable checkpoint:
   `PYTHONPATH=. python scripts/run_grid.py --n <N> --resume results/20261019_135940_grid --note "universe expansion batch 4: N 37 -> 47 (<SYMBOL>/USDT)"`
   then `PYTHONPATH=. python scripts/remote_checkpoint.py --message "chore(kilo): grid batch4 <SYMBOL>/USDT (66 cells, N=47)"`.
4. `PYTHONPATH=. python scripts/aggregate_grid.py --run results/20261019_135940_grid`.
5. Append the batch-4 section to `universe/mcap_expansion_log.md` (previous N -> new N,
   rank range added, source/date, market caps, rank drift, grid coverage row).
6. Update this handoff and `INITIAL_TASK_FOR_NEXT_AGENT.md`, then checkpoint.

## Ground Truth
- `results/20261019_135940_grid/summary.json`, `pooled.md`, `per_symbol.json`,
  `per_pair.json` are the current aggregate truth (2,442 cells, 0 with net PF > 1).
- `universe/mcap_rank.json` + `universe/mcap_expansion_log.md` are the universe truth (N = 37).
- The earlier single-pair conclusion (`results/FINAL_DECISION.md`, `results/RESEARCH_CONCLUSION.md`)
  is unchanged: EMA hourly continuation is **rejected**, no live trading. The grid program
  continues because PROMPT.md §2.1 requires the expanding-universe search to continue;
  it does not re-open the rejected baseline decision.
- Research artifacts are immutable: do not modify or re-run the scripts that produced
  the final artifacts unless a new pre-registered hypothesis requires it.

## Handoff Notes
- Handoff completed by this session (2026-10-19, batch 3 done end-to-end: snapshot fetch,
  10 x 22k-bar OHLCV download, 10 x 66-cell grid runs, per-symbol durable checkpoints,
  re-aggregation, expansion log). Grid completeness re-verified: 2,442/2,442 cells,
  `progress.json` `all_symbols_processed = true`, `next_cell = null`.
- Environment note: this session's runner had no pandas/numpy/pytest preinstalled;
  `pip install pandas numpy pytest` was needed before the grid and the test suite could run.

## Initial Task for Next Agent (copy-ready)
> "Batch 3 (N 37) grid is COMPLETE: 2,442/2,442 cells (37 symbols x 66 EMA pairs) in results/20261019_135940_grid/, all rejected, 0 cells with net PF > 1, best net PF 0.9523 (WLD/USDT P20_200), pooled mean net PF 0.4446 over 1,999,202 trades, cumulative rejection rate 100%. Universe is N=37 (universe/mcap_rank.json, snapshot mcap_snapshot_20261019_163400); 110 eligible names remain below the JST floor, so per PROMPT.md §2.1 continue, do not stand down. NEXT: expand to N=47 (batch 4): fetch a fresh snapshot (python scripts/fetch_mcap_snapshot.py --pages 4 --batch-size 10, then --apply; expected next names KCS, ALGO, KAS, POL, JUP, ATOM, RENDER, INJ, FIL, AERO), download OHLCV (python scripts/fetch_kucoin.py --target-bars 22000 --symbols ...), run the full 66-pair grid one symbol at a time with PYTHONPATH=. python scripts/run_grid.py --n <N> --resume results/20261019_135940_grid, checkpoint each symbol with scripts/remote_checkpoint.py, re-aggregate with PYTHONPATH=. python scripts/aggregate_grid.py --run results/20261019_135940_grid, log the expansion in universe/mcap_expansion_log.md, and report the cumulative rejection rate. Validation: python -m pytest tests/ -q (37 passed)"

## Validation Command
`python -m pytest tests/ -q`
