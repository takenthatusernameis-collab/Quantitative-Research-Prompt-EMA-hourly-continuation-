# NEXT AGENT TASK

## Status update (2026-10-20): batch 17 COMPLETE. Universe N=177, grid 11,682/11,682 cells, 0 credible candidates. Next: batch 18 (N 177 -> 187) if continuing.

## Objective

**Batch 16 grid COMPLETE.** All 660 cells (10 symbols x 66 EMA pairs) are finished;
660 rejected, 0 exploratory, 0 cells surviving OOS + cost stress
(`results/20261020_080932_candidate_check/`). Per PROMPT.md §2.1 the program must
expand again: **N 167 -> 177** (batch 17, next 10 lower-market-cap names below
XNO's $45.5M floor), fetch a fresh ranking snapshot, download OHLCV for the 10
new names, run the full 66-pair grid (resume `results/20261019_135940_grid`),
checkpoint per symbol, re-aggregate, re-run the candidate check, and report the
cumulative rejection rate.

**Do not stand down.** A prior rejection does not stop the program (PROMPT.md §2.1.4).

## State at handoff (2026-10-20)

- Universe: **N = 167** (`universe/mcap_rank.json`), snapshot `mcap_snapshot_20261020_065809`
  (CoinGecko `/api/v3/coins/markets`, fetched 2026-10-20T06:58:09Z). Batch 16 added
  WIN, TRB, CELO, FLOW, ID, CTC, DEEP, BRETT, CFG, XNO.
- Grid: **11,022 / 11,022 cells complete** in `results/20261019_135940_grid/` (167 symbols x
  66 pairs). 0 blocked. 10,997 rejected; 25 exploratory in the scan, all **rejected** on
  robustness -> **0 credible candidates**.
- Pooled (net of costs, full sample, 10 bps taker + 2 bps slippage per side):
  mean net PF 0.4922, median 0.5124, **best net PF 2.2274** (BABYDOGE/USDT P50_55,
  rejected - 0 OOS trades), 9,035,501 trades.
- Cumulative rejection rate: **10,997 / 11,022 cells (99.77 %)**, 0 credible candidates.
  Cells with net PF > 1: 35 / 11,022 = 0.3 % against a ~50 % no-edge null. All 35
  failed OOS + cost stress: 32 BABYDOGE cells have zero OOS trades; JASMY P20_200 /
  P21_200 and SUPER P8_200 fail cost stress.
- Batch 16 alone: 660 cells, **660 rejected, 0 exploratory**, pooled mean net PF 0.4977,
  521,041 trades. 0 cells with net PF > 1.
- Per-pair pooled leaders (mean net PF over 167 symbols): P8_200 0.6750, P20_200 0.6713,
  P12_200 0.6669, P21_200 0.6653. Worst: P20_21 0.1371, P50_55 0.2094, P8_12 0.2043.
- Robustness artifact: `results/20261020_080932_candidate_check/` (script
  `scripts/candidate_check.py`). All 35 net-PF > 1 cells rejected.
- Data layer: 167 fixtures in `data/fixtures/` (+ sample_hourly.csv), provenance in
  `data/fixtures/fetch_manifest.json` (KuCoin public `/api/v1/market/candles`, 1h, UTC).
  Manifest is reconciled (167 rows); run `--reconcile-manifest` after every fetch batch.
- Tests: **46 passed** (`python -m pytest tests/ -q`).
- Note: `results/FINAL_DECISION.md` and `results/RESEARCH_CONCLUSION.md` are earlier
  artifacts covering the *narrower* single-pair OOS test (5 symbols, rr=1.5, ATR
  filter). They are not invalidated by the grid program, which is a broader scan
  under PROMPT.md §2.1 and has now covered 167 symbols x 66 pairs.

## Environment note

`python3` has pandas/numpy/pytest/requests available in the current runner image
(`pandas 3.0.6`, `numpy 2.5.4`, `pytest 9.1.1`). If a fresh image lacks them:
`python3 -m pip install --break-system-packages pandas numpy pytest`.
Always run scripts as `PYTHONPATH=. python3 scripts/...` (the scripts import `data`,
`signals`, `backtest`, `metrics`, `universe` from the repo root).

## Next batch (batch 17, N 167 -> 177) - concrete steps

1. `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 4 --batch-size 10`
   (dry run) to see the next 10 names below the XNO floor ($45.5M), then
   `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --apply-from universe/mcap_snapshot_<TS>.json --batch-size 10 --apply`
   to write `universe/mcap_rank.json` from the reviewed snapshot.
   Use `--pages 5` only if the eligible tail runs out below XNO.
2. `PYTHONPATH=. python3 scripts/fetch_kucoin.py --target-bars 22000 --symbols <the 10 new names>`
   (~15-20 min for 10 symbols; 10 x ~220 paginated KuCoin requests). Then
   `PYTHONPATH=. python3 scripts/fetch_kucoin.py --reconcile-manifest` so the provenance
   manifest covers every fixture on disk.
   **If a symbol returns KuCoin error `400100` (symbol does not exist), re-query it
   before doing anything else** - in batch 12 that error turned out to be transient for
   all six affected names. Only after a repeat failure should a name be considered
   ineligible, and dropping it needs a documented justification (PROMPT.md §2.1.2);
   no name has ever had to be dropped in this program.
3. For each new symbol in market-cap descending order, one invocation each:
   `PYTHONPATH=. python3 scripts/run_grid.py --n <N> --resume results/20261019_135940_grid --note "universe expansion batch 17: N 167 -> 177 (<SYMBOL>/USDT, 66-pair EMA grid)"`
   where `--n` is the 1-based position of that symbol in the 177-symbol ranking
   (--n 168 for the first new symbol up to --n 177 for the last; do not use a single
   `--n 177` pass, so each symbol can be checkpointed on its own).
   then `PYTHONPATH=. python3 scripts/remote_checkpoint.py --message "chore(kilo): grid batch17 <SYMBOL>/USDT (66 cells, N=177)" --paths results/20261019_135940_grid`.
   Each symbol takes ~2 min; the per-symbol checkpoint keeps every push delta
   inside the controller's 30 s budget.
4. `PYTHONPATH=. python3 scripts/aggregate_grid.py --run results/20261019_135940_grid`.
5. `PYTHONPATH=. python3 scripts/candidate_check.py --run results/20261019_135940_grid`
   (auto-discovers every cell with net PF > 1 and runs OOS + 2x cost stress on it).
6. Append the batch-16 section to `universe/mcap_expansion_log.md` (and add its row to
   the "Grid coverage per batch" table), update this handoff and
   `INITIAL_TASK_FOR_NEXT_AGENT.md`, then checkpoint.

## Guardrails

- Never promote a grid cell on in-sample numbers alone (PROMPT.md §3.3): a cell needs
  OOS + cost stress before it can be called a candidate. Every cell that has ever
  reached net PF > 1 in this program failed both out-of-sample and cost stress.
- Keep the universe append-only and strictly market-cap descending; never reorder or
  drop names already processed (PROMPT.md §2.1.2).
- Do not stand down because a batch failed; expand and continue (§2.1.4).
- Do not silently change the baseline. The zero-volume-bar issue seen in thin pairs
  (GMX 12.1 % of bars, DBR 20.6 %, SUN 15.0 %, DCR 14.8 %, HTX 12.1 %, GLM 10.4 %) is
  pre-existing across the whole universe, so the baseline was left alone; a
  zero-volume-bar filter would have to be a registered mutation (PROMPT.md §5) run
  against the parent config, not an edit to the existing runs.

## Validation Command

`python -m pytest tests/ -q`
