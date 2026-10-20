# NEXT AGENT TASK

## Current state (verified against the saved artifacts, 2026-10-20T23:30:00Z)

**Program status: `AWAITING_NEW_ELIGIBLE_CANDIDATES`.** Batch 26 (universe N 257 -> 266) is **complete**: all 9 symbols (POKT, XAI, ANYONE, ACE, MOVR, RIO, BICO, AGLD, TAIKO) processed - 594/594 cells complete, 0 blocked. Aggregate and OOS + 2x-cost candidate check re-run. The universe snapshot band is **exhausted**: `universe/last_scan.json` (snapshot `mcap_snapshot_20261020_113004`, fetched 2026-10-20T11:30:04Z) holds **0 eligible unseen names below the floor** (TAIKO/USDT at $15 436 339). A fresh CoinGecko snapshot is needed, but not before 2026-10-21T11:30:04Z (24h refresh bound per PROMPT.md §2.1.5).

- Universe: **N = 266**, floor **TAIKO/USDT** $15 436 339. Snapshot coverage exhausted below floor. Eligible unseen below floor: **0**.
- Grid: **17 556 / 17 556 cells complete** in `results/20261019_135940_grid/` (266 symbols × 66 EMA pairs); 0 blocked. `progress.json` reports `next_cell: null`, `all_symbols_processed: true`.
- Decision count: **17 530 rejected**, 26 exploratory at aggregate scan, **0 credible candidates** after OOS + 2x-cost check.
- Pooled, full-sample net of costs (10 bps taker + 2 bps slippage per side): mean net PF **0.4993**, median **0.5205**, best in-sample PF **2.2274** (BABYDOGE/USDT P50_55; rejected, zero OOS trades), ~13.76M+ trades.
- Cells with full-sample net PF > 1: **36 / 17 556 (0.2%)**. All 36 failed OOS + 2x-cost checks (unchanged from batch 20). Batch 26 contributed **no survivors** (all 594 rejected).
- Latest candidate-check artifact: `results/20261020_233737_candidate_check/summary.md` (36 cells, 36 rejected). Gates unchanged.

**Machine-readable state:** `universe/last_scan.json` - `state=AWAITING_NEW_ELIGIBLE_CANDIDATES`, `universe_n=266`, floor `TAIKO/USDT`, `eligible_unseen_below_floor_count=0`, `next_eligible_refresh_at=2026-10-21T11:30:04.315667+00:00`. **Do not refresh before 2026-10-21T11:30:04Z** - the 24h refresh bound applies.

## Required next action

1. **Reconcile state first.** Read this handoff, `PROMPT.md` §2.1, `universe/mcap_rank.json`, `universe/last_scan.json`, `universe/mcap_snapshot_20261020_113004.json`, `universe/mcap_expansion_log.md`, grid `progress.json` and latest candidate-check artifact. Do not repeat completed scans/cells.

2. **Wait for refresh window.** The snapshot band is exhausted (0 eligible below floor). Per PROMPT.md §2.1.5, a fresh CoinGecko query is only allowed from `next_eligible_refresh_at` (2026-10-21T11:30:04Z). Before then, the correct state is `AWAITING_NEW_ELIGIBLE_CANDIDATES` - do not force expansion or relax gates.

3. **After 2026-10-21T11:30:04Z, fetch a fresh snapshot.** Use `scripts/fetch_mcap_snapshot.py --pages 10 --batch-size 10` (dry run), inspect timestamped snapshot/exclusions, extend pages only if not below floor. Apply any eligible names strictly below the TAIKO floor in descending market-cap order.

4. **For any newly eligible names:** fetch/validate hourly OHLCV, run full 66-pair grid per symbol, resume from `results/20261019_135940_grid`, run `scripts/aggregate_grid.py` and `scripts/candidate_check.py`, update expansion log and this handoff.

## Guardrails
- Append-only, market-cap descending, only below current floor.
- No stopping on negative results.
- Never promote without OOS + 2x-cost gates.
- Keep baseline/grid unchanged unless preregistered mutation.
- Run `python -m pytest tests/ -q` after changes; report exact results.

## Environment
Use `PYTHONPATH=. python3 scripts/...` from repo root. Checkpoint durably after each symbol. ~10 min/symbol budget.

## Session update (2026-10-20T23:30:00Z)
- Batch 26 complete: N 257->266, 594 cells all done, 0 credible candidates. Expansion log updated with batch 26 section. Grid coverage table updated. Handoffs refreshed. Snapshot band exhausted (0 eligible below TAIKO floor); fresh CoinGecko needed after 2026-10-21T11:30:04Z.

## Session update (2026-10-20T23:44:08Z)
- Re-verified state against saved artifacts: `universe/last_scan.json` state=AWAITING_NEW_ELIGIBLE_CANDIDATES, universe_n=266, floor TAIKO/USDT $15 436 339, eligible_unseen_below_floor_count=0, next_eligible_refresh_at=2026-10-21T11:30:04Z. `results/20261019_135940_grid/progress.json`: 17 556/17 556 cells complete, next_cell=null, all_symbols_processed=true. Latest candidate check `results/20261020_233737_candidate_check/summary.md`: 36 cells, all rejected, 0 credible candidates. `universe/mcap_rank.json`: N=266, last 9 symbols = POKT/XAI/ANYONE/ACE/MOVR/RIO/BICO/AGLD/TAIKO. Tests: `python -m pytest tests/ -q` -> 56 passed. No change since 23:30; program remains in AWAITING_NEW_ELIGIBLE_CANDIDATES until the refresh window opens at 2026-10-21T11:30:04Z.