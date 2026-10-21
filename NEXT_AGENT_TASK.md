# NEXT AGENT TASK

## Current state (verified against saved artifacts, 2026-10-21T00:06:44Z)

**Program status: `AWAITING_NEW_ELIGIBLE_CANDIDATES`.** Batch 26 (universe N 257 -> 266) is **complete**: all 9 symbols (POKT, XAI, ANYONE, ACE, MOVR, RIO, BICO, AGLD, TAIKO) processed - 594/594 cells complete, 0 blocked. The universe snapshot band is **exhausted and audited**: `universe/last_scan.json` (snapshot `mcap_snapshot_20261020_113004`, fetched 2026-10-20T11:30:04Z) holds **0 eligible unseen names below the floor** (TAIKO/USDT at $15 436 339). A fresh CoinGecko query is needed, but not before **2026-10-21T11:30:04Z** (24h refresh bound per PROMPT.md §2.1.5).

- Universe: **N = 266**, floor **TAIKO/USDT** $15 436 339. Coverage: pages 10/10 returned, 1 000 entries, lowest covered rank 1 000 ($15 174 185) - the pass does reach below the floor. Eligible unseen below floor: **0**.
- Grid: **17 556 / 17 556 cells complete** in `results/20261019_135940_grid/` (266 symbols x 66 EMA pairs); 0 blocked. `progress.json` reports `next_cell: null`, `all_symbols_processed: true`, `n_symbols x n_pairs == completed_cells` (266 x 66 = 17 556). Re-ran `scripts/aggregate_grid.py` offline this session: numbers reproduce exactly.
- Decision count: **17 530 rejected**, 26 exploratory at aggregate scan, **0 credible candidates** after OOS + 2x-cost check.
- Pooled, full-sample net of costs (10 bps taker + 2 bps slippage per side): mean net PF **0.4993**, median **0.5205**, best in-sample PF **2.2274** (BABYDOGE/USDT P50_55; rejected, zero OOS trades), ~13.76M+ trades.
- Cells with full-sample net PF > 1: **36 / 17 556 (0.2%)**. All 36 failed OOS + 2x-cost checks (unchanged from batch 20). Batch 26 contributed **no survivors** (all 594 rejected).
- Latest candidate-check artifact: `results/20261020_233737_candidate_check/summary.md` (36 cells, 36 rejected). Gates unchanged.

**Machine-readable state:** `universe/last_scan.json` - `state=AWAITING_NEW_ELIGIBLE_CANDIDATES`, `universe_n=266`, floor `TAIKO/USDT`, `eligible_unseen_below_floor_count=0`, `next_eligible_refresh_at=2026-10-21T11:30:04.315667+00:00`. **Do not refresh before 2026-10-21T11:30:04Z** - the 24h refresh bound applies. Wakeup `wku_15bbe446b001KXX7NeqAYoB78u` scheduled for 2026-10-21T11:31:00Z.

## What this session verified (2026-10-21T00:06:44Z)

1. **Prior agent task complete.** Read handoffs and verified durable state against artifacts. Grid state internally consistent (266×66=17556/17556, all complete, next_cell=null). Repaired in prior session (`scripts/run_grid.py` `merge_symbol_lists` fix keeps a narrow `--resume` from shrinking the coverage record).
2. **Tests:** `python -m pytest tests/ -q` -> **67 passed**. No code/data changes; no CoinGecko fetch (bound closed).
3. **Results:** 36 cells above full-sample PF>1 all rejected by OOS + 2x-cost; robustness (drop-top-N, rank buckets, subperiod) shows no credible survivors (0 credible candidates). Mean net PF 0.4993, median 0.5205.

## Required next action

1. **Reconcile state first.** Read this handoff, `PROMPT.md` §2.1, `universe/mcap_rank.json`, `universe/last_scan.json`, `universe/mcap_snapshot_20261020_113004.json`, `universe/mcap_expansion_log.md`, grid `progress.json` and the latest candidate-check / robustness artifacts. Do not repeat completed scans/cells. Check that the grid state file is self-consistent (`n_symbols x n_pairs == completed_cells`, `all_symbols_processed=true`, `next_cell=null`).

2. **Before 2026-10-21T11:30:04Z:** the correct state is `AWAITING_NEW_ELIGIBLE_CANDIDATES`. Do not force expansion, do not query CoinGecko, and do not relax the gates. Use the wait for offline verification work only (e.g. more robustness legs over the existing grid).

3. **From 2026-10-21T11:30:04Z, fetch a fresh snapshot.** Use `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 10 --batch-size 10` (dry run). The script prints a WARNING when the coverage band stops above the floor - if that happens, extend the page count until the coverage reaches below TAIKO/USDT $15 436 339, then re-run. Inspect the timestamped snapshot and the per-name exclusion reasons, then apply eligible names strictly below the floor in descending market-cap order.

4. **For any newly eligible names:** fetch/validate hourly OHLCV (`scripts/fetch_kucoin.py`), run the full 66-pair grid per symbol resuming from `results/20261019_135940_grid`, re-run `scripts/aggregate_grid.py`, `scripts/candidate_check.py` and `scripts/robustness_pooled.py`, and update `universe/mcap_expansion_log.md`, `universe/last_scan.json` and this handoff.

## Guardrails
- Append-only, market-cap descending, only below current floor.
- No stopping on negative results.
- Never promote without OOS + 2x-cost gates (plus the subperiod leg now available).
- Keep baseline/grid unchanged unless preregistered mutation.
- Run `python -m pytest tests/ -q` after changes; report exact results.

## Environment
Use `PYTHONPATH=. python3 scripts/...` from repo root. Checkpoint durably after each symbol. ~10 min/symbol budget.

## Session updates
- 2026-10-20T23:30:00Z - Batch 26 complete: N 257->266, 594 cells all done, 0 credible candidates. Expansion log updated with batch 26 section. Grid coverage table updated. Handoffs refreshed. Snapshot band exhausted (0 eligible below TAIKO floor); fresh CoinGecko needed after 2026-10-21T11:30:04Z.
- 2026-10-20T23:44:08Z - Re-verified state against saved artifacts: `universe/last_scan.json` state=AWAITING_NEW_ELIGIBLE_CANDIDATES, universe_n=266, floor TAIKO/USDT $15 436 339, eligible_unseen_below_floor_count=0, next_eligible_refresh_at=2026-10-21T11:30:04Z. `results/20261019_135940_grid/progress.json`: 17 556/17 556 cells complete, next_cell=null, all_symbols_processed=true. Latest candidate check `results/20261020_233737_candidate_check/summary.md`: 36 cells, all rejected, 0 credible candidates. `universe/mcap_rank.json`: N=266, last 9 symbols = POKT/XAI/ANYONE/ACE/MOVR/RIO/BICO/AGLD/TAIKO. Tests: `python -m pytest tests/ -q` -> 56 passed. No change since 23:30; program remains in AWAITING_NEW_ELIGIBLE_CANDIDATES until the refresh window opens at 2026-10-21T11:30:04Z.
- 2026-10-20T23:53:00Z - Offline work only, no market-cap query (bound still closed). Verified: 266/266 fixtures present with >= 17 520 hourly bars each, `fetch_manifest.json` 267 rows; aggregate re-run reproduces mean net PF 0.4993 / median 0.5205 / best 2.2274 / 36 cells above PF 1 / 26 exploratory / 17 530 rejected / 0 blocked. Added `scripts/robustness_pooled.py` and `tests/test_robustness_pooled.py`; artifact `results/20261020_235449_robustness/`. Tests: `python -m pytest tests/ -q` -> 65 passed. Refresh wakeup scheduled for 2026-10-21T11:31:00Z.
- 2026-10-21T00:02:00Z - Found and fixed durable-state defect: `scripts/run_grid.py` now merges previously recorded symbols with current selection (`merge_symbol_lists`), so a narrow resume can no longer shrink the coverage record. Repaired canonical state with `--resume ... --n 266` (no cell recomputed): 266 symbols, 17 556 completed cells, `all_symbols_processed=true`, `next_cell=null`. Added regression tests in `tests/test_grid_runner.py`. Tests: `python -m pytest tests/ -q` -> 67 passed.
- 2026-10-21T00:05:40Z - Prior agent task complete. Grid state internally consistent. Tests 67 passed. No code/data changes; no CoinGecko fetch (bound closed). Handoff updated for next agent.
- 2026-10-21T00:06:44Z - Current session verified prior agent task complete against artifacts (tests 67 passed, grid self-consistent 266×66=17556). No work possible until refresh bound opens at 2026-10-21T11:30:04Z. Handoff refreshed for the next agent.
49. - 2026-10-21T00:11:14Z - Agent read durable handoffs and completed reconciliation. Prior task confirmed complete (Batch 26 done, 0 credible candidates). State AWAITING_NEW_ELIGIBLE_CANDIDATES; refresh bound 2026-10-21T11:30:04Z. Grid self-consistent (266×66=17556/17556). Tests 67 passed. Handoffs updated. No expansion possible until bound opens.
