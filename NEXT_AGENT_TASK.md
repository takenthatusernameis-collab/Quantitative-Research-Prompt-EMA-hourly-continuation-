# NEXT AGENT TASK

## Status update (2026-10-20): batch 14 COMPLETE. Universe N=147, grid 9,702/9,702 cells, 0 credible candidates. Next: batch 15 (N 147 -> 157).

## Objective
**Batch 14 grid COMPLETE.** All 660 cells (10 symbols x 66 EMA pairs) are finished;
638 rejected and 22 exploratory (all BABYDOGE), 0 cells surviving OOS + cost stress
(`results/20261020_035907_candidate_check/`). Per PROMPT.md §2.1 the program must
expand again: **N 147 -> 157** (batch 15, next 10 lower-market-cap names below
DEXE's $61.4M floor), fetch a fresh ranking snapshot, download OHLCV for the 10
new names, run the full 66-pair grid (resume `results/20261019_135940_grid`),
checkpoint per symbol, re-aggregate, re-run the candidate check, and report the
cumulative rejection rate.

**Do not stand down.** A prior rejection does not stop the program (PROMPT.md §2.1.4).

## State at handoff (2026-10-20)
- Universe: **N = 147** (`universe/mcap_rank.json`), snapshot `mcap_snapshot_20261020_030608`
  (CoinGecko `/api/v3/coins/markets`, fetched 2026-10-20T03:06:08Z). Batch 14 added
  ZETA, ALT, AXL, BABYDOGE, TFUEL, IO, SUSHI, EDU, DGB, DEXE.
- Grid: **9,702 / 9,702 cells complete** in `results/20261019_135940_grid/` (147 symbols x
  66 pairs). 0 blocked. 9,677 rejected; 25 exploratory in the scan (32 BABYDOGE cells
  with net PF > 1 + JASMY P20_200 / P21_200 + SUPER P8_200) and all **rejected** on
  robustness -> **0 credible candidates**.
- Pooled (net of costs, full sample, 10 bps taker + 2 bps slippage per side):
  mean net PF 0.4894, median 0.5098, **best net PF 2.2274** (BABYDOGE/USDT P50_55,
  rejected - 0 OOS trades), 7,998,391 trades.
- Cumulative rejection rate: **9,677 / 9,702 cells (99.74 %)**, 0 credible candidates.
  Cells with net PF > 1: 35 / 9,702 = 0.4 % against a ~50 % no-edge null. All 35
  failed OOS + cost stress: 32 BABYDOGE cells have zero OOS trades; JASMY P20_200 /
  P21_200 and SUPER P8_200 fail cost stress.
- Batch 14 alone: 660 cells, **638 rejected, 22 exploratory** (all BABYDOGE),
  pooled mean net PF 0.5222, 499,594 trades. 0 cells with net PF > 1 outside BABYDOGE.
- Per-pair pooled leaders (mean net PF over 147 symbols): P8_200 0.6750, P20_200 0.6713,
  P12_200 0.6669, P21_200 0.6653. Worst: P20_21 0.1371, P50_55 0.2094, P8_12 0.2043.
- Robustness artifact: `results/20261020_035907_candidate_check/` (script
  `scripts/candidate_check.py`). All 35 net-PF > 1 cells rejected.
- Data layer: 147 fixtures in `data/fixtures/`, provenance in
  `data/fixtures/fetch_manifest.json` (KuCoin public `/api/v1/market/candles`, 1h, UTC).
  Manifest is reconciled (147 rows); run `--reconcile-manifest` after every fetch batch.
- Tests: **46 passed** (`python -m pytest tests/ -q`).
- Note: `results/FINAL_DECISION.md` and `results/RESEARCH_CONCLUSION.md` are earlier
  artifacts covering the *narrower* single-pair OOS test (5 symbols, rr=1.5, ATR
  filter). They are not invalidated by the grid program, which is a broader scan
  under PROMPT.md §2.1 and has now covered 147 symbols x 66 pairs.

## Environment note
`python3` has pandas/numpy/pytest/requests available in the current runner image
(`pandas 3.0.6`, `numpy 2.5.4`, `pytest 9.1.1`). If a fresh image lacks them:
`python3 -m pip install --break-system-packages pandas numpy pytest`.
Always run scripts as `PYTHONPATH=. python3 scripts/...` (the scripts import `data`,
`signals`, `backtest`, `metrics`, `universe` from the repo root).

## Next batch (batch 15, N 147 -> 157) - concrete steps
1. `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 4 --batch-size 10`
   (dry run) to see the next 10 names below the DEXE floor ($61.4M), then
   `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --apply-from universe/mcap_snapshot_<TS>.json --batch-size 10 --apply`
   to write `universe/mcap_rank.json` from the reviewed snapshot.
   Use `--pages 5` only if the eligible tail runs out below DEXE.
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
   `PYTHONPATH=. python3 scripts/run_grid.py --n <N> --resume results/20261019_135940_grid --note "universe expansion batch 15: N 147 -> 157 (<SYMBOL>/USDT, 66-pair EMA grid)"`
   where `--n` is the 1-based position of that symbol in the 157-symbol ranking
   (--n 148 for the first new symbol up to --n 157 for the last; do not use a single
   `--n 157` pass, so each symbol can be checkpointed on its own).
   then `PYTHONPATH=. python3 scripts/remote_checkpoint.py --message "chore(kilo): grid batch15 <SYMBOL>/USDT (66 cells, N=157)" --paths results/20261019_135940_grid`.
   Each symbol takes ~2 min; the per-symbol checkpoint keeps every push delta
   inside the controller's 30 s budget.
4. `PYTHONPATH=. python3 scripts/aggregate_grid.py --run results/20261019_135940_grid`.
5. `PYTHONPATH=. python3 scripts/candidate_check.py --run results/20261019_135940_grid`
   (auto-discovers every cell with net PF > 1 and runs OOS + 2x cost stress on it).
6. Append the batch-15 section to `universe/mcap_expansion_log.md` (and add its row to
   the "Grid coverage per batch" table).
7. Update this handoff and `INITIAL_TASK_FOR_NEXT_AGENT.md`, then checkpoint.

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
