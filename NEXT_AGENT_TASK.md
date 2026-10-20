# NEXT AGENT TASK

## Status update (2026-10-20): batches 8-13 COMPLETE. Universe N=137, grid 9,042/9,042 cells, 0 credible candidates. Next: batch 14 (N 137 -> 147).

## Objective
**Batch 13 grid COMPLETE.** All 9,042 cells (137 symbols x 66 EMA pairs) are finished;
9,039 rejected and the same 3 cells that reached net PF > 1 in the scan (JASMY P20_200,
JASMY P21_200, SUPER P8_200) were killed by out-of-sample + cost stress
(`results/20261020_025729_candidate_check/`). Per PROMPT.md §2.1 the program must expand
again: **N 137 -> 147** (batch 14, next 10 lower-market-cap names), fetch a fresh ranking
snapshot, download OHLCV for the 10 new names, run the full 66-pair grid (resume
`results/20261019_135940_grid`), checkpoint per symbol, re-aggregate, re-run the candidate
check, and report the cumulative rejection rate.

**Do not stand down.** A prior rejection does not stop the program (PROMPT.md §2.1.4).

## State at handoff (2026-10-20)
- Universe: **N = 137** (`universe/mcap_rank.json`), snapshot `mcap_snapshot_20261020_021004`
  (CoinGecko `/api/v3/coins/markets`, fetched 2026-10-20T02:10:04Z). Batch 13 added
  KSM, NMR, YFI, HNT, ORDI, KAVA, CKB, DUSK, AMP, VELO.
- Grid: **9,042 / 9,042 cells complete** in `results/20261019_135940_grid/` (137 symbols x
  66 pairs). 0 blocked. 9,039 rejected; 3 exploratory in the scan (JASMY/USDT P20_200,
  JASMY/USDT P21_200, SUPER/USDT P8_200) and all 3 **rejected** on robustness ->
  **0 credible candidates**.
- Pooled (net of costs, full sample, 10 bps taker + 2 bps slippage per side):
  mean net PF 0.4833, median 0.5056, **best net PF 1.0377** (SUPER/USDT P8_200),
  7,498,797 trades.
- Cumulative rejection rate: **9,039 / 9,042 cells (99.97 %)**, 0 credible candidates.
  Cells with net PF > 1: 3 / 9,042 = 0.03 % against a ~50 % no-edge null.
- Batch 13 alone: 660 cells, **660 rejected, 0 exploratory**, pooled mean net PF 0.4961,
  median 0.5159, best 0.8305 (VELO/USDT P20_144), 579,984 trades.
- Batch means are flat across batches 7-13 (0.4682 / 0.5085 / 0.5210 / 0.5017 / 0.5287 /
  0.5010 / 0.4961): lower-market-cap names do not improve the registered rule. The pooled mean net PF
  drifts up slightly only because the smaller names trade less often per bar.
- Per-pair pooled leaders (mean net PF over 137 symbols): P8_200 0.6794, P20_200 0.6687,
  P12_200 0.6669, P21_200 0.6619. Worst: P20_21 0.1323, P50_55 0.1920, P8_12 0.1958.
- Robustness artifact: `results/20261020_025729_candidate_check/` (script
  `scripts/candidate_check.py`). JASMY P20_200: base PF 1.0097 -> OOS PF 0.9068 (174 trades)
  -> 2x-cost PF 0.7465 -> rejected. JASMY P21_200: base PF 1.0341 -> OOS PF 0.9167
  (173 trades) -> 2x-cost PF 0.7576 -> rejected. SUPER P8_200: base PF 1.0377 -> OOS PF
  0.9536 (78 trades) -> 2x-cost PF 0.8093 -> rejected.
- Data layer: 137 fixtures in `data/fixtures/`, provenance in
  `data/fixtures/fetch_manifest.json` (KuCoin public `/api/v1/market/candles`, 1h, UTC).
  Manifest is reconciled (137 rows); run `--reconcile-manifest` after every fetch batch.
- Tests: **46 passed** (`python -m pytest tests/ -q`).
- Note: `results/FINAL_DECISION.md` and `results/RESEARCH_CONCLUSION.md` are earlier
  artifacts covering the *narrower* single-pair OOS test (5 symbols, rr=1.5, ATR
  filter). They are not invalidated by the grid program, which is a broader scan
  under PROMPT.md §2.1 and has now covered 137 symbols x 66 pairs.

## Environment note
`python3` has pandas/numpy/pytest/requests available in the current runner image
(`pandas 3.0.6`, `numpy 2.5.4`, `pytest 9.1.1`). If a fresh image lacks them:
`python3 -m pip install --break-system-packages pandas numpy pytest`.
Always run scripts as `PYTHONPATH=. python3 scripts/...` (the scripts import `data`,
`signals`, `backtest`, `metrics`, `universe` from the repo root).

## Next batch (batch 14, N 137 -> 147) - concrete steps
1. `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 4 --batch-size 10`
   (dry run) to see the next 10 names below the VELO floor, then
   `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --apply-from universe/mcap_snapshot_<TS>.json --batch-size 10 --apply`
   to write `universe/mcap_rank.json` from the reviewed snapshot.
   Expected candidates (from the 2026-10-20T02:10:04Z snapshot, to be re-checked on a
   fresh fetch): **ZETA, AXL, ALT, BABYDOGE, TFUEL, IO, DGB, SUSHI, EDU, RLC**
   (10 names below VELO's $70.5M floor). The 4-page snapshot still holds 1 more eligible
   name below that (DEXE) -> enough for batch 15 without increasing `--pages`; use
   `--pages 5` only when the eligible tail runs out.
2. `PYTHONPATH=. python3 scripts/fetch_kucoin.py --target-bars 22000 --symbols <the 10 new names>`
   (~15-20 min for 10 symbols; 10 x ~220 paginated KuCoin requests). Then
   `PYTHONPATH=. python3 scripts/fetch_kucoin.py --reconcile-manifest` so the provenance
   manifest covers every fixture on disk.
   **If a symbol returns KuCoin error `400100` (symbol does not exist), re-query it
   before doing anything else** - in batch 12 that error turned out to be transient for
   all six affected names (all six are listed and enabled in `/api/v1/symbols` and the
   candles endpoint then answered `code = 200000`). Only after a repeat failure should a
   name be considered ineligible, and dropping it needs a documented justification
   (PROMPT.md §2.1.2); no name has ever had to be dropped in this program.
3. For each new symbol in market-cap descending order, one invocation each:
   `PYTHONPATH=. python3 scripts/run_grid.py --n <N> --resume results/20261019_135940_grid --note "universe expansion batch 14: N 137 -> 147 (<SYMBOL>/USDT, 66-pair EMA grid)"`
   where `--n` is the 1-based position of that symbol in the 147-symbol ranking
   (--n 138 for the first new symbol up to --n 147 for the last; do not use a single
   `--n 147` pass, so each symbol can be checkpointed on its own).
   then `PYTHONPATH=. python3 scripts/remote_checkpoint.py --message "chore(kilo): grid batch14 <SYMBOL>/USDT (66 cells, N=147)" --paths results/20261019_135940_grid`.
   Each symbol takes ~2 min; the per-symbol checkpoint keeps every push delta
   inside the controller's 30 s budget.
4. `PYTHONPATH=. python3 scripts/aggregate_grid.py --run results/20261019_135940_grid`.
5. `PYTHONPATH=. python3 scripts/candidate_check.py --run results/20261019_135940_grid`
   (auto-discovers every cell with net PF > 1 and runs OOS + 2x cost stress on it).
6. Append the batch-14 section to `universe/mcap_expansion_log.md` (and add its row to
   the "Grid coverage per batch" table).
7. Update this handoff and `INITIAL_TASK_FOR_NEXT_AGENT.md`, then checkpoint.

## Guardrails
- Never promote a grid cell on in-sample numbers alone (PROMPT.md §3.3): a cell needs
  OOS + cost stress before it can be called a candidate. Three cells have now cleared
  net PF > 1 in-sample and all three failed those gates.
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
