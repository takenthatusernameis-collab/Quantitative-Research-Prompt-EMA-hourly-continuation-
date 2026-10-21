# NEXT AGENT TASK

## Current state (verified against saved artifacts, 2026-10-21T01:05Z)

**Program status: `AWAITING_NEW_ELIGIBLE_CANDIDATES`.** Batch 26 (universe N 257 -> 266) is **complete**: all 9 symbols (POKT, XAI, ANYONE, ACE, MOVR, RIO, BICO, AGLD, TAIKO) processed - 594/594 cells complete, 0 blocked. The universe snapshot band is **exhausted and audited**: `universe/last_scan.json` (snapshot `mcap_snapshot_20261020_113004`, fetched 2026-10-20T11:30:04Z) holds **0 eligible unseen names below the floor** (TAIKO/USDT at $15 436 339). A fresh CoinGecko query is needed, but not before **2026-10-21T11:30:04Z** (24h refresh bound per PROMPT.md §2.1.5).

The 2026-10-21T00:24Z session did **not** change the universe: the refresh bound was still closed, so the window was spent on offline verification (see "New robustness leg" below).

- Universe: **N = 266**, floor **TAIKO/USDT** $15 436 339. Coverage: pages 10/10 returned, 1 000 entries, lowest covered rank 1 000 ($15 174 185) - the pass does reach below the floor. Eligible unseen below floor: **0**.
- Grid: **17 556 / 17 556 cells complete** in `results/20261019_135940_grid/` (266 symbols x 66 EMA pairs); 0 blocked. `progress.json` reports `next_cell: null`, `all_symbols_processed: true`, `n_symbols x n_pairs == completed_cells` (266 x 66 = 17 556).
- Decision count: **17 530 rejected**, 26 exploratory at aggregate scan, **0 credible candidates** after OOS + 2x-cost check.
- Pooled, full-sample net of costs (10 bps taker + 2 bps slippage per side): mean net PF **0.4993**, median **0.5205**, best in-sample PF **2.2274** (BABYDOGE/USDT P50_55; rejected, zero OOS trades), ~13.76M+ trades.
- Cells with full-sample net PF > 1: **36 / 17 556 (0.2%)**. All 36 failed OOS + 2x-cost checks. Batch 26 contributed **no survivors**.
- Latest candidate-check artifact: `results/20261020_233737_candidate_check/summary.md` (36 cells, 36 rejected). Gates unchanged.

**Machine-readable state:** `universe/last_scan.json` - `state=AWAITING_NEW_ELIGIBLE_CANDIDATES`, `universe_n=266`, floor `TAIKO/USDT`, `eligible_unseen_below_floor_count=0`, `next_eligible_refresh_at=2026-10-21T11:30:04.315667+00:00`. **Do not refresh before 2026-10-21T11:30:04Z** - the 24h refresh bound applies.

## New robustness leg (2026-10-21T01:05Z) - grid-wide out-of-sample audit

`scripts/candidate_check.py` only ever tested the 36 **in-sample** winners out of sample, leaving 17 520 cells unexamined. `scripts/oos_grid_scan.py` (new) applies the out-of-sample window to **all 17 556 cells** and re-verifies the survivors with the real backtest. Artifact: `results/20261021_005234_oos_grid_scan/`.

- Pooled out-of-sample net PF **0.5299** (0.3267 under 2x costs); per-cell mean 0.4320, median 0.4343, max 1.9955.
- **77** cells (0.44%) with out-of-sample net PF > 1; 75 with >= 30 OOS trades; **10** still > 1 under 2x costs. 180 screen survivors re-verified: **0 credible candidates**, 76 exploratory, 104 rejected.
- The 6 closest survivors (BRETT P8_200, DEXE P50_200, DEXE P55_200, GRT P20_200, MERL P8_200, ZEN P12_200) all have a **full-sample** net PF below 1 (0.75-0.91) and none keeps a stressed out-of-sample PF > 1 at 20 % / 35 % / 50 % windows.
- Selection bias closed: 0 survivors in the in-sample winners, 0 in the other 17 520 cells.

## Defect note for whoever writes the next tooling

The artifact layout is **not uniform**: the grid runner writes `trades.csv.gz`, but the five largest market-cap names (BTC, ETH, SOL, BNB, XRP - ranks 1-5) still carry the legacy baseline-study layout `trades.csv` (uncompressed). Their configs are identical and their cells reproduce exactly, but **any tool that assumes the gzip layout silently skips 330 cells - the whole top of the universe.** `scripts/oos_grid_scan.py:read_trades` handles both; reuse it.

## Required next action

1. **Reconcile state first.** Read this handoff, `PROMPT.md` §2.1, `universe/mcap_rank.json`, `universe/last_scan.json`, grid `progress.json` and latest candidate-check/robustness artifacts. Do not repeat completed scans/cells. Verify grid state is self-consistent (`n_symbols x n_pairs == completed_cells`, `all_symbols_processed=true`, `next_cell=null`).

2. **Before 2026-10-21T11:30:04Z:** State is `AWAITING_NEW_ELIGIBLE_CANDIDATES`. Do not force expansion, do not query CoinGecko, and do not relax the gates. Use the wait for offline verification work only (e.g. more robustness legs over the existing grid).

3. **From 2026-10-21T11:30:04Z, fetch a fresh snapshot.** Use `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 10 --batch-size 10` (dry run). The script prints a WARNING when the coverage band stops above the floor - if that happens, extend the page count until the coverage reaches below TAIKO/USDT $15 436 339, then re-run. Inspect the timestamped snapshot and the per-name exclusion reasons, then apply eligible names strictly below the floor in descending market-cap order.

4. **For any newly eligible names:** fetch/validate hourly OHLCV (`scripts/fetch_kucoin.py`), run the full 66-pair grid per symbol resuming from `results/20261019_135940_grid`, re-run `scripts/aggregate_grid.py`, `scripts/candidate_check.py` and `scripts/robustness_pooled.py`, re-run `scripts/oos_grid_scan.py` over the whole grid (it must be re-run after every expansion, not just once), and update `universe/mcap_expansion_log.md`, `universe/last_scan.json` and this handoff.

## Guardrails
- Append-only, market-cap descending, only below current floor.
- No stopping on negative results.
- Never promote without OOS + 2x-cost gates (plus subperiod leg).
- Keep baseline/grid unchanged unless preregistered mutation.
- Run `python -m pytest tests/ -q` after changes; report exact results.

## Environment
Use `PYTHONPATH=. python3 scripts/...` from repo root. Checkpoint durably after each symbol. ~10 min/symbol budget.

## Session updates
52: - 2026-10-21T01:05Z - Prior agent task completed by current session. Reconciled state (grid self-consistent, 12/12 sampled cells reproduce exactly), found the legacy-vs-gzip artifact layout split, added the grid-wide out-of-sample audit (`scripts/oos_grid_scan.py` + `tests/test_oos_grid_scan.py`), which closes the selection bias of the OOS gate: 17 556 cells evaluated out of sample, 0 credible candidates. State still AWAITING_NEW_ELIGIBLE_CANDIDATES; refresh bound 2026-10-21T11:30:04Z. Tests: `python -m pytest tests/ -q` -> 77 passed. Handoffs updated for next agent. No expansion possible until the bound opens.
53: - 2026-10-21T02:08Z - Prior agent task completed by current session. Reconciled state (refresh bound still closed, no CoinGecko query), re-ran full test suite -> 95 passed. No code/data changes. State remains AWAITING_NEW_ELIGIBLE_CANDIDATES; refresh bound 2026-10-21T11:30:04Z. Handoffs updated for next agent.
54: - 2026-10-21T00:17:50Z - Prior agent task completed by current session. Verified Batch 26 done (N=266, 17556/17556 cells, 0 credible candidates). State AWAITING_NEW_ELIGIBLE_CANDIDATES; refresh bound 2026-10-21T11:30:04Z. Grid self-consistent. Tests: `python -m pytest tests/ -q` -> 67 passed. Handoffs updated for next agent. No expansion possible until bound opens.