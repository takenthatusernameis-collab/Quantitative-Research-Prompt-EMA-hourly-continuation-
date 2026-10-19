# NEXT AGENT TASK

## Objective
**Batch 4 grid (N 47) COMPLETE.** All 3,102 cells (47 symbols x 66 EMA pairs) rejected.
Per PROMPT.md §2.1 the program must expand again: **N 47 -> 57** (batch 5, next 10
lower-market-cap names), fetch a fresh ranking snapshot, download OHLCV for the 10 new
names, run the full 66-pair grid (resume `results/20261019_135940_grid`), checkpoint per
symbol, re-aggregate, and report the cumulative rejection rate.

**Do not stand down.** A prior rejection does not stop the program (PROMPT.md §2.1.4).

## State at handoff (2026-10-19)
- Universe: **N = 47** (`universe/mcap_rank.json`), snapshot `mcap_snapshot_20261019_181146`
  (CoinGecko `/api/v3/coins/markets`, fetched 2026-10-19T18:11:46Z). Batch 4 added
  KCS, ALGO, POL, KAS, JUP, ATOM, RENDER, INJ, FIL, AERO (all below the JST floor of
  1 121 015 524 USD; order preserved, max market-cap drift vs batch 3 = 2.15 %).
- Grid: **3,102 / 3,102 cells complete** in `results/20261019_135940_grid/` (47 symbols x
  66 pairs). 0 cells with net PF > 1; 3,102 rejected; 0 blocked; 0 exploratory.
- Pooled (net of costs, full sample, 10 bps taker + 2 bps slippage per side):
  2,526,502 trades, mean net PF 0.4509, median 0.4645, **best net PF 0.9523**
  (WLD/USDT P20_200), mean net Sharpe -7.7056, max net Sharpe -0.1979.
- Multiple-testing context: 0/3,102 cells above PF 1 vs a ~50 % no-edge null (-50.0 %
  excess). Every symbol and every EMA pair is net-unprofitable; the best pair
  (P12_200, mean PF 0.6527) and worst pair (P20_21, mean PF 0.1067) are both below 1.
- Batch 4 per-symbol (mean / best net PF): KCS 0.2346 / 0.4440, ALGO 0.5368 / 0.9020,
  POL 0.4248 / 0.6955, KAS 0.4304 / 0.6930, JUP 0.5181 / 0.6741, ATOM 0.4676 / 0.7508,
  RENDER 0.5815 / 0.8862, INJ 0.5242 / 0.6994, FIL 0.4656 / 0.7621, AERO 0.5572 / 0.9311.
- Cumulative rejection rate: **3,102 / 3,102 cells (100 %)** across 47 symbols.
- Data: 47 fixtures in `data/fixtures/` (22 000 hourly bars each, KuCoin 1h UTC, no gaps
  or duplicate timestamps); RENDER is the only short sample (18 947 bars, listed
  2024-08-21 on KuCoin) - still above the 2-year floor. Provenance in
  `data/fixtures/fetch_manifest.json` (47 entries).
- Tests: **37 passed** (`python -m pytest tests/ -q`).
- Git: tracked tree clean and pushed; every batch-4 symbol has its own durable
  checkpoint commit (KCS, ALGO, POL, KAS, JUP, ATOM, RENDER, INJ, FIL, AERO), each push
  verified against the remote SHA. `PYTHONPATH=.` is required for all `scripts/` entry points.
- Universe is **not** exhausted: the 18:11 snapshot still holds 100 eligible names
  below the AERO floor (ZRO, CAKE, STX, APT, ETHFI, XDC, DASH, TIA, BDX, CRV, ...), so
  expansion to N = 57 is feasible and required.

## Next batch (batch 5, N 47 -> 57) - concrete steps
1. `python scripts/fetch_mcap_snapshot.py --pages 4 --batch-size 10` (dry run) to see
   the next 10 names below the AERO floor, then `--apply` to write `universe/mcap_rank.json`.
   Expected candidates (18:11 snapshot, re-verify with the fresh fetch): ZRO, CAKE, STX,
   APT, ETHFI, XDC, DASH, TIA, BDX, CRV.
2. `python scripts/fetch_kucoin.py --target-bars 22000 --symbols <the 10 new names>`
   (KuCoin 1h UTC, ~2.5 min per symbol; short listings simply return fewer bars).
3. For each new symbol in market-cap descending order, one invocation each, so
   `progress.json` is written after every symbol and each symbol gets its own durable
   checkpoint. **`--n` is the 1-based position of the symbol in the expanded ranking**:
   the first new symbol (rank 48) uses `--n 48`, the last (rank 57) uses `--n 57`.
   A single `--n 57` invocation would run all remaining symbols in one pass and skip the
   per-symbol checkpointing, so do not use it.
   `PYTHONPATH=. python scripts/run_grid.py --n <N> --resume results/20261019_135940_grid --note "universe expansion batch 5: N 47 -> 57 (<SYMBOL>/USDT, 66-pair EMA grid)"`
   then `PYTHONPATH=. python scripts/remote_checkpoint.py --message "chore(kilo): grid batch5 <SYMBOL>/USDT (66 cells, N=57)"`.
   Restrict the checkpoint staging to the finished symbol if other files are still being
   written: `--paths results/20261019_135940_grid/results/<SYMBOL>_USDT results/20261019_135940_grid/progress.json results/20261019_135940_grid/run_config.json universe/mcap_rank.json data/fixtures/<SYMBOL>_USDT.csv`.
4. `PYTHONPATH=. python scripts/aggregate_grid.py --run results/20261019_135940_grid`.
5. Append the batch-5 section to `universe/mcap_expansion_log.md` (previous N -> new N,
   rank range added, source/date, market caps, rank drift, fixture coverage, grid coverage row).
6. Update this handoff and `INITIAL_TASK_FOR_NEXT_AGENT.md`, then checkpoint.

## Ground Truth
- `results/20261019_135940_grid/summary.json`, `pooled.md`, `per_symbol.json`,
  `per_pair.json` are the current aggregate truth (3,102 cells, 0 with net PF > 1).
- `universe/mcap_rank.json` + `universe/mcap_expansion_log.md` are the universe truth (N = 47).
- The earlier single-pair conclusion (`results/FINAL_DECISION.md`, `results/RESEARCH_CONCLUSION.md`)
  is unchanged: EMA hourly continuation is **rejected**, no live trading. The grid program
  continues because PROMPT.md §2.1 requires the expanding-universe search to continue;
  it does not re-open the rejected baseline decision.
- Research artifacts are immutable: do not modify or re-run the scripts that produced
  the final artifacts unless a new pre-registered hypothesis requires it.

## Handoff Notes
- Handoff completed by this session (2026-10-19, batch 4 done end-to-end: snapshot fetch,
  10 x 22k-bar OHLCV download, 10 x 66-cell grid runs, per-symbol durable checkpoints,
  re-aggregation, expansion log). Grid completeness re-verified: 3,102/3,102 cells on
  disk (47 symbol dirs x 66 cells, 0 blocked), `progress.json` `next_cell = null`.
- Environment note: this runner already had pandas 3.0.6, numpy 2.5.4, pytest 9.1.1 and
  `requests` installed; if a future runner lacks them, `pip install pandas numpy pytest`
  before running the grid or the test suite.
- Artifact-layout note: the 5 batch-0 symbols (BTC, ETH, SOL, BNB, XRP) store uncompressed
  `trades.csv` / `equity.csv`; every symbol from batch 1 on stores `trades.csv.gz` /
  `equity.csv.gz` (deterministic gzip, `mtime=0`). `scripts/aggregate_grid.py` reads both.
- Progress-flag caveat: `run_grid.py` computes `next_cell` / `all_symbols_processed` only
  over symbols whose fixture already exists on disk, so during an expansion
  `all_symbols_processed: true` is not proof that the new batch is done. Verify the cell
  count (`n_symbols x 66`) and the number of symbol directories instead.
- Working-universe order is append-only: batch 4 kept the batch-3 DOT/WLD order even though
  the two names inverted on a 0.77 % market-cap difference between the 16:34 and 18:11
  snapshots. Keep the same convention (document any inversion in the expansion log).

## Initial Task for Next Agent (copy-ready)
> "Batch 4 (N 47) grid is COMPLETE: 3,102/3,102 cells (47 symbols x 66 EMA pairs) in results/20261019_135940_grid/, all rejected, 0 cells with net PF > 1, best net PF 0.9523 (WLD/USDT P20_200), pooled mean net PF 0.4509 over 2,526,502 trades, cumulative rejection rate 100%. Universe is N=47 (universe/mcap_rank.json, snapshot mcap_snapshot_20261019_181146); 100 eligible names remain below the AERO floor, so per PROMPT.md §2.1 continue, do not stand down. NEXT: expand to N=57 (batch 5) - fetch a fresh snapshot (python scripts/fetch_mcap_snapshot.py --pages 4 --batch-size 10, then --apply; expected next names ZRO, CAKE, STX, APT, ETHFI, XDC, DASH, TIA, BDX, CRV), download OHLCV (python scripts/fetch_kucoin.py --target-bars 22000 --symbols ...), run the full 66-pair grid one symbol at a time with PYTHONPATH=. python scripts/run_grid.py --n <N> --resume results/20261019_135940_grid (--n = 48 for the first new symbol up to --n 57 for the last), checkpoint each symbol with scripts/remote_checkpoint.py, re-aggregate with PYTHONPATH=. python scripts/aggregate_grid.py --run results/20261019_135940_grid, log the expansion in universe/mcap_expansion_log.md, and report the cumulative rejection rate. Validation: python -m pytest tests/ -q (37 passed)"

## Validation Command
`python -m pytest tests/ -q`
