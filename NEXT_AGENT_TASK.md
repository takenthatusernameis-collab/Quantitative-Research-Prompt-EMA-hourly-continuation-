# NEXT AGENT TASK

## Current state (verified against the saved artifacts, 2026-10-20T23:53:00Z)

**Program status: `AWAITING_NEW_ELIGIBLE_CANDIDATES`.** Batch 26 (universe N 257 -> 266) is **complete**: all 9 symbols (POKT, XAI, ANYONE, ACE, MOVR, RIO, BICO, AGLD, TAIKO) processed - 594/594 cells complete, 0 blocked. The universe snapshot band is **exhausted and audited**: `universe/last_scan.json` (snapshot `mcap_snapshot_20261020_113004`, fetched 2026-10-20T11:30:04Z) holds **0 eligible unseen names below the floor** (TAIKO/USDT at $15 436 339). A fresh CoinGecko query is needed, but not before **2026-10-21T11:30:04Z** (24h refresh bound per PROMPT.md §2.1.5).

- Universe: **N = 266**, floor **TAIKO/USDT** $15 436 339. Coverage: pages 10/10 returned, 1 000 entries, lowest covered rank 1 000 ($15 174 185) - the pass does reach below the floor. Eligible unseen below floor: **0**.
- Grid: **17 556 / 17 556 cells complete** in `results/20261019_135940_grid/` (266 symbols x 66 EMA pairs); 0 blocked. `progress.json` reports `next_cell: null`, `all_symbols_processed: true`. Re-ran `scripts/aggregate_grid.py` offline this session: numbers reproduce exactly.
- Decision count: **17 530 rejected**, 26 exploratory at aggregate scan, **0 credible candidates** after OOS + 2x-cost check.
- Pooled, full-sample net of costs (10 bps taker + 2 bps slippage per side): mean net PF **0.4993**, median **0.5205**, best in-sample PF **2.2274** (BABYDOGE/USDT P50_55; rejected, zero OOS trades), ~13.76M+ trades.
- Cells with full-sample net PF > 1: **36 / 17 556 (0.2%)**. All 36 failed OOS + 2x-cost checks (unchanged from batch 20). Batch 26 contributed **no survivors** (all 594 rejected).
- Latest candidate-check artifact: `results/20261020_233737_candidate_check/summary.md` (36 cells, 36 rejected). Gates unchanged.

**Machine-readable state:** `universe/last_scan.json` - `state=AWAITING_NEW_ELIGIBLE_CANDIDATES`, `universe_n=266`, floor `TAIKO/USDT`, `eligible_unseen_below_floor_count=0`, `next_eligible_refresh_at=2026-10-21T11:30:04.315667+00:00`. **Do not refresh before 2026-10-21T11:30:04Z** - the 24h refresh bound applies.

### What this session added (2026-10-20T23:47Z-00:02Z)

1. **Band audit** (offline, from the stored snapshot): the 8 snapshot names below the TAIKO floor (ranks 993-1000: PIPPIN, ULT, CAW, PPC, USDO, IXS, SGB, BTY) are all excluded as `no_tradable_kucoin_spot_usdt_pair`; TUT (989) and MIRA (991) sit *above* the floor and are excluded for insufficient history. The band is genuinely exhausted, not a failed scan. Written up in `universe/mcap_expansion_log.md` ("Batch 26 post-checks").
2. **Two missing PROMPT.md §3.3 robustness legs** over the full grid, new script `scripts/robustness_pooled.py` (+ 7 tests in `tests/test_robustness_pooled.py`, artifact `results/20261020_235449_robustness/`):
   - *Drop top-N market caps*: pooled (trade-level) net PF 0.5224 (all) -> 0.5248 (minus top 5) -> 0.5263 (top 10) -> 0.5280 (top 20) -> 0.5303 (top 50) - the negative result does not depend on the largest names.
   - *Rank buckets* (§2.1.6): 1-10 0.4083, 11-50 0.5037, 51-100 0.5188, 101-200 0.5360, 201+ 0.5302 - all below 1.0.
   - *Subperiod stability* of the 36 above-PF cells (4 equal-time slices): 31 fragile, 4 insufficient, 1 stable (BABYDOGE/USDT P50_89) which still has 0 OOS trades. **No cell survives all three legs.**
   - Reproduce: `PYTHONPATH=. python3 scripts/robustness_pooled.py --run results/20261019_135940_grid`.
3. **Stale program-level reports corrected**: `results/FINAL_DECISION.md`, `results/RESEARCH_CONCLUSION.md` and `results/robustness_summary.md` still described the 5-symbol 2026-10-19 study and claimed the research was "concluded". They now carry the current N=266 program status on top, with the 5-symbol study kept as the historical record (PROMPT.md §2.1.4: a failed batch is never a program stop).
4. **Grid-state defect fixed** (`scripts/run_grid.py`): a `--resume` with a narrower `--n` used to overwrite `progress.json` with the narrower symbol list while keeping the full completed-cell set, so the durable record lost symbols (it had shrunk to 259-260 of 266). `merge_symbol_lists` now keeps the union of the previously recorded and the currently selected symbols, so a narrow resume can never shrink the coverage record. The canonical state was repaired with `--resume ... --n 266` (no cell recomputed): 266 symbols, 17 556 cells, `all_symbols_processed=true`, `next_cell=null`. Two regression tests added in `tests/test_grid_runner.py`; one of them fails if `n_symbols x n_pairs` ever stops matching `completed_cells`.
5. **Refresh wakeup scheduled** for 2026-10-21T11:31:00Z (session `wku_15bbe446b001KXX7NeqAYoB78u`) so the expansion runs as soon as the bound opens, even if no other activation happens in between.

## Required next action

1. **Reconcile state first.** Read this handoff, `PROMPT.md` §2.1, `universe/mcap_rank.json`, `universe/last_scan.json`, `universe/mcap_snapshot_20261020_113004.json`, `universe/mcap_expansion_log.md`, grid `progress.json` and the latest candidate-check / robustness artifacts. Do not repeat completed scans/cells. Check that the grid state file is self-consistent (`n_symbols x n_pairs == completed_cells`, `all_symbols_processed=true`, `next_cell=null`): a resume with a stale `--n` used to truncate that record, and the fix in `scripts/run_grid.py` keeps it from happening again.

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

## Session update (2026-10-20T23:30:00Z)
- Batch 26 complete: N 257->266, 594 cells all done, 0 credible candidates. Expansion log updated with batch 26 section. Grid coverage table updated. Handoffs refreshed. Snapshot band exhausted (0 eligible below TAIKO floor); fresh CoinGecko needed after 2026-10-21T11:30:04Z.

## Session update (2026-10-20T23:44:08Z)
- Re-verified state against saved artifacts: `universe/last_scan.json` state=AWAITING_NEW_ELIGIBLE_CANDIDATES, universe_n=266, floor TAIKO/USDT $15 436 339, eligible_unseen_below_floor_count=0, next_eligible_refresh_at=2026-10-21T11:30:04Z. `results/20261019_135940_grid/progress.json`: 17 556/17 556 cells complete, next_cell=null, all_symbols_processed=true. Latest candidate check `results/20261020_233737_candidate_check/summary.md`: 36 cells, all rejected, 0 credible candidates. `universe/mcap_rank.json`: N=266, last 9 symbols = POKT/XAI/ANYONE/ACE/MOVR/RIO/BICO/AGLD/TAIKO. Tests: `python -m pytest tests/ -q` -> 56 passed. No change since 23:30; program remains in AWAITING_NEW_ELIGIBLE_CANDIDATES until the refresh window opens at 2026-10-21T11:30:04Z.

## Session update (2026-10-20T23:53:00Z)
- Offline work only, no market-cap query (bound still closed). Verified: 266/266 fixtures present with >= 17 520 hourly bars each, `fetch_manifest.json` 267 rows; aggregate re-run reproduces mean net PF 0.4993 / median 0.5205 / best 2.2274 / 36 cells above PF 1 / 26 exploratory / 17 530 rejected / 0 blocked.
- Added `scripts/robustness_pooled.py` (drop-top-N, market-cap rank buckets, subperiod stability) and `tests/test_robustness_pooled.py`; artifact `results/20261020_235449_robustness/`. New: pooled trade-level net PF 0.5224 over 14 240 827 trades; drop-top-N leaves the result flat (0.5248-0.5303); every rank bucket below 1.0; of the 36 above-PF cells 31 fragile / 4 insufficient / 1 stable-but-zero-OOS-trades. Still **0 credible candidates**.
- Audited the below-floor band (8 names, all excluded for no tradable KuCoin USDT pair) and appended the audit + the robustness legs to `universe/mcap_expansion_log.md`.
- Corrected the stale program reports `results/FINAL_DECISION.md`, `results/RESEARCH_CONCLUSION.md`, `results/robustness_summary.md` (they still described the 5-symbol study and a "concluded" program).
- Tests: `python -m pytest tests/ -q` -> **65 passed**.
- Refresh wakeup scheduled for 2026-10-21T11:31:00Z to run the expansion cycle when the bound opens. State unchanged: N = 266, AWAITING_NEW_ELIGIBLE_CANDIDATES, next eligible refresh 2026-10-21T11:30:04Z.

## Session update (2026-10-21T00:02:00Z)
- Found and fixed a durable-state defect: `results/20261019_135940_grid/progress.json` had been rewritten by `--resume` invocations with a narrower `--n` (258/259/260, per `run_config.json` history) and listed only 259-260 symbols while `completed_cells` stayed 17 556. `scripts/run_grid.py` now merges the previously recorded symbols with the current selection (`merge_symbol_lists`), so a narrow resume can no longer shrink the coverage record; the invocation's own selection is kept in `progress.json:invocation_symbols` and `run_config.json:covered_symbols`.
- Repaired the canonical state with `PYTHONPATH=. python3 scripts/run_grid.py --resume results/20261019_135940_grid --n 266 --note "state repair: ..."` (no cell recomputed, 6 s): 266 symbols, 17 556 completed cells, `all_symbols_processed=true`, `next_cell=null`, `n_symbols x n_pairs == completed_cells`.
- Added regression tests `test_merge_symbol_lists_keeps_prior_coverage` and `test_canonical_grid_progress_is_internally_consistent` in `tests/test_grid_runner.py`; the latter fails if the shipped run's symbol count ever stops matching its cell count.
- Tests: `python -m pytest tests/ -q` -> **67 passed**.
- No market-cap query (the 24h bound is still closed). Program state unchanged: N = 266, AWAITING_NEW_ELIGIBLE_CANDIDATES, next eligible refresh 2026-10-21T11:30:04Z, 0 credible candidates.
