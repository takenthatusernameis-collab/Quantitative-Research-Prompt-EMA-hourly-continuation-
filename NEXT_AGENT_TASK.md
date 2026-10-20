# NEXT AGENT TASK

## Status update (2026-10-20): batches 8-12 COMPLETE. Universe N=127, grid 8,382/8,382
## cells, 0 credible candidates. Next: batch 13 (N 127 -> 137).

## Objective
**Batch 12 grid COMPLETE.** All 8,382 cells (127 symbols x 66 EMA pairs) are finished;
8,379 rejected and the same 3 cells that reached net PF > 1 in the scan (JASMY P20_200,
JASMY P21_200, SUPER P8_200) were killed by out-of-sample + cost stress
(`results/20261020_020152_candidate_check/`). Per PROMPT.md §2.1 the program must expand
again: **N 127 -> 137** (batch 13, next 10 lower-market-cap names), fetch a fresh ranking
snapshot, download OHLCV for the 10 new names, run the full 66-pair grid (resume
`results/20261019_135940_grid`), checkpoint per symbol, re-aggregate, re-run the candidate
check, and report the cumulative rejection rate.

**Do not stand down.** A prior rejection does not stop the program (PROMPT.md §2.1.4).

## State at handoff (2026-10-20)
- Universe: **N = 127** (`universe/mcap_rank.json`), snapshot `mcap_snapshot_20261020_011116`
  (CoinGecko `/api/v3/coins/markets`, fetched 2026-10-20T01:11:16Z). Batch 12 added
  DYDX, MINA, ZRX, WEMIX, GMX, PROM, W, ARKM, LPT, SAFE.
- Grid: **8,382 / 8,382 cells complete** in `results/20261019_135940_grid/` (127 symbols x
  66 pairs). 0 blocked. 8,379 rejected; 3 exploratory in the scan (JASMY/USDT P20_200,
  JASMY/USDT P21_200, SUPER/USDT P8_200) and all 3 **rejected** on robustness ->
  **0 credible candidates**.
- Pooled (net of costs, full sample, 10 bps taker + 2 bps slippage per side):
  mean net PF 0.4823, median 0.5037, **best net PF 1.0377** (SUPER/USDT P8_200),
  6,918,813 trades.
- Cumulative rejection rate: **8,379 / 8,382 cells (99.96 %)**, 0 credible candidates.
  Cells with net PF > 1: 3 / 8,382 = 0.04 % against a ~50 % no-edge null.
- Batch 12 alone: 660 cells, **660 rejected, 0 exploratory**, pooled mean net PF 0.5010,
  median 0.5248, best 0.9717 (W/USDT P8_200), 565,589 trades.
- Batch means are flat across batches 7-12 (0.4682 / 0.5085 / 0.5210 / 0.5017 / 0.5287 /
  0.5010): lower-market-cap names do not improve the registered rule. The pooled mean net PF
  drifts up slightly only because the smaller names trade less often per bar.
- Per-pair pooled leaders (mean net PF over 127 symbols): P8_200 0.6778, P20_200 0.6672,
  P12_200 0.6653, P21_200 0.6604. Worst: P20_21 0.1316, P50_55 0.1913, P8_12 0.1950.
- Robustness artifact: `results/20261020_020152_candidate_check/` (script
  `scripts/candidate_check.py`). JASMY P20_200: base PF 1.0097 -> OOS PF 0.9068 (174 trades)
  -> 2x-cost PF 0.7465 -> rejected. JASMY P21_200: base PF 1.0341 -> OOS PF 0.9167
  (173 trades) -> 2x-cost PF 0.7576 -> rejected. SUPER P8_200: base PF 1.0377 -> OOS PF
  0.9536 (78 trades) -> 2x-cost PF 0.8093 -> rejected.
- Data layer: 127 fixtures in `data/fixtures/`, provenance in
  `data/fixtures/fetch_manifest.json` (KuCoin public `/api/v1/market/candles`, 1h, UTC).
  Manifest is reconciled (127 rows); run `--reconcile-manifest` after every fetch batch.
- Tests: **46 passed** (`python -m pytest tests/ -q`).
- Note: `results/FINAL_DECISION.md` and `results/RESEARCH_CONCLUSION.md` are earlier
  artifacts covering the *narrower* single-pair OOS test (5 symbols, rr=1.5, ATR
  filter). They are not invalidated by the grid program, which is a broader scan
  under PROMPT.md §2.1 and has now covered 127 symbols x 66 pairs.

## Environment note
`python3` has pandas/numpy/pytest/requests available in the current runner image
(`pandas 3.0.6`, `numpy 2.5.4`, `pytest 9.1.1`). If a fresh image lacks them:
`python3 -m pip install --break-system-packages pandas numpy pytest`.
Always run scripts as `PYTHONPATH=. python3 scripts/...` (the scripts import `data`,
`signals`, `backtest`, `metrics`, `universe` from the repo root).

## Next batch (batch 13, N 127 -> 137) - concrete steps
1. `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 4 --batch-size 10`
   (dry run) to see the next 10 names below the SAFE floor, then
   `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --apply-from universe/mcap_snapshot_<TS>.json --batch-size 10 --apply`
   to write `universe/mcap_rank.json` from the reviewed snapshot.
   Expected candidates (from the 2026-10-20T01:23:01Z snapshot, to be re-checked on a
   fresh fetch): **KSM, NMR, YFI, HNT, ORDI, KAVA, AMP, DUSK, CKB, VELO**
   (Kusama, Numeraire, yearn.finance, Helium, ORDI, Kava, Amp, DUSK, Nervos Network, Velo).
   The 4-page snapshot still holds 11 more eligible names below that (ZETA, AXL, ALT,
   BABYDOGE, TFUEL, IO, DGB, SUSHI, EDU, RLC, DEXE) -> that is enough for batch 14 without
   increasing `--pages`; use `--pages 5` only when the eligible tail runs out.
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
   `PYTHONPATH=. python3 scripts/run_grid.py --n <N> --resume results/20261019_135940_grid --note "universe expansion batch 13: N 127 -> 137 (<SYMBOL>/USDT, 66-pair EMA grid)"`
   where `--n` is the 1-based position of that symbol in the 137-symbol ranking
   (--n 128 for the first new symbol up to --n 137 for the last; do not use a single
   `--n 137` pass, so each symbol can be checkpointed on its own).
   then `PYTHONPATH=. python3 scripts/remote_checkpoint.py --message "chore(kilo): grid batch13 <SYMBOL>/USDT (66 cells, N=137)" --paths results/20261019_135940_grid`.
   Each symbol takes ~2 min; the per-symbol checkpoint keeps every push delta
   inside the controller's 30 s budget.
4. `PYTHONPATH=. python3 scripts/aggregate_grid.py --run results/20261019_135940_grid`.
5. `PYTHONPATH=. python3 scripts/candidate_check.py --run results/20261019_135940_grid`
   (auto-discovers every cell with net PF > 1 and runs OOS + 2x cost stress on it).
6. Append the batch-13 section to `universe/mcap_expansion_log.md` (and add its row to
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
