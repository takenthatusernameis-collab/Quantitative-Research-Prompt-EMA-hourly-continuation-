# NEXT_AGENT_TASK.md — EMA hourly continuation universe-refresh gate

**Task:** Resume the EMA hourly continuation universe-refresh gate. Read `README.md`, `AGENTS.md`, and this file before acting.

## Current state (verified 2026-11-07T08:30:01Z)
- Source of truth `universe/last_scan.json` (JSON valid; read directly): `next_eligible_refresh_at` = `2026-11-07T10:16:12.893046+00:00`. **NOT ELIGIBLE** at `2026-11-07T08:30:01Z` (independent `datetime.now(timezone.utc)` cross-check): eligible=false, remaining_seconds≈6370 (~1h46m10s).
- State: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, recorded_at=`2026-11-06T10:16:13.427723+00:00`, snapshot_id=`mcap_snapshot_20261106_101612`, snapshot_path=`universe/mcap_snapshot_20261106_101612.json`, scanned_at=`2026-11-06T10:16:12.893046+00:00`, source=CoinGecko public API `/api/v3/coins/markets` (usd, market_cap_desc).
- Coverage: pages_requested=20, pages_fetched=20, all_requested_pages_returned=true, entries_count=2000, lowest_rank_covered=2000, lowest_market_cap_usd=3179353, `coverage_reaches_below_floor=true`.
- Universe: n=275, expansion_floor={PIXEL/USDT, $3,254,887}, eligible_unseen_below_floor_count=0, eligible_unseen_below_floor=[], batch_selected=[].
- Coverage guard: `data/fixtures/SUKU_USDT.csv` ABSENT; no `*SUKU*` files under `results/`. **`--apply` MUST NOT run** without verified fixture/grid coverage for any selected candidate.
- Baseline grid `results/20261019_135940_grid/progress.json` complete (`completed_cells=18150`, `n_symbols=275`, `n_pairs=66`, `all_symbols_processed=true`, `stopped=false`, `stop_reason=null`, `next_cell=null`). `results/FINAL_DECISION.md` records program-level rejection. `scripts/fetch_mcap_snapshot.py` and `scripts/refresh_gate.py` present.

## Offline gate re-check record — 2026-11-07T08:30:01Z
- Completed prior handoff task. Offline re-check only; **no provider calls**, no snapshot pass, no `--apply`, no candle fetches, no grid reruns, no cost/fill/EMA changes.
- Re-derived from `universe/last_scan.json` (source of truth) + independent `datetime.now(timezone.utc)` cross-check: now=`2026-11-07T08:30:01+00:00`, bound=`2026-11-07T10:16:12.893046+00:00` (`next_eligible_refresh_at`), eligible=false, remaining_seconds≈6370 (~1h46m10s).
- State/evidence unchanged: `state=AWAITING_NEW_ELIGIBLE_CANDIDATES`, `snapshot_id=mcap_snapshot_20261106_101612`, `snapshot_path=universe/mcap_snapshot_20261106_101612.json` (present), `scanned_at=2026-11-06T10:16:12.893046+00:00`, source=CoinGecko public API `/api/v3/coins/markets` (usd, market_cap_desc), 20/20 pages/2000 entries, `lowest_rank_covered=2000`, `lowest_market_cap_usd=3179353`, `coverage_reaches_below_floor=true`, `universe_n=275`, `expansion_floor={PIXEL/USDT, $3,254,887}`, `eligible_unseen_below_floor_count=0`, `eligible_unseen_below_floor=[]`, `batch_selected=[]`.
- Guards re-verified: `data/fixtures/SUKU_USDT.csv` ABSENT; no `*SUKU*` anywhere in the tree → **`--apply` MUST NOT run** without verified fixture/grid coverage for any selected candidate. Baseline grid `results/20261019_135940_grid/progress.json` complete; `results/FINAL_DECISION.md` preserved (program-level rejection).
- Wakeup retained (no duplicate scheduled): `wku_1b3cb2ba10013PChsdJTbjSl1z` due `2026-11-07T10:21:00Z` (~5 min after gate opens). Nothing actionable before `2026-11-07T10:16:12.893046+00:00`.

## What to do
1. Re-verify gate eligibility at start from `universe/last_scan.json` (do not guess). NOT ELIGIBLE until `2026-11-07T10:16:12.893046+00:00`.
2. If still not eligible: make **no provider calls**. Record an offline check here (exact now/bound/remaining, state evidence), update handoff if needed, and stop. Rely on scheduled wakeup; do not schedule duplicates.
3. If eligible: run **at most one** 20-page snapshot pass (`PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`), recompute the floor, inspect the below-floor band, update `universe/last_scan.json`, then review any new candidate(s) for fixture/grid coverage before any `--apply`. Do NOT apply without verified coverage.
4. Never: rerun grids, fetch candles, place orders, change EMA/cost/fill assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory.

## Constraints
Historical research only; no orders/live/paper trading; free public data/no-cost tooling; preserve EMA signal/fill/cost assumptions; preserve negative/blocked results; separate exploratory from confirmatory; follow `AGENTS.md` gate policy.

## Wakeup
Retained (from prior session): `wku_1b3cb2ba10013PChsdJTbjSl1z` due `2026-11-07T10:21:00Z` (~5 min after gate opens). **Do not re-schedule a duplicate.**

## Offline gate re-check record — 2026-11-07T08:34:43Z
- Offline re-check only; no provider calls, no snapshot pass, no `--apply`, no candle fetches, no grid reruns, no cost/fill/EMA changes.
- Re-derived from `universe/last_scan.json` (source of truth) + independent `datetime.now(timezone.utc)` cross-check: now=`2026-11-07T08:34:43+00:00`, bound=`2026-11-07T10:16:12.893046+00:00` (`next_eligible_refresh_at`), eligible=false, remaining_seconds≈6090 (~1h41m29s).
- State/evidence unchanged: `state=AWAITING_NEW_ELIGIBLE_CANDIDATES`, `snapshot_id=mcap_snapshot_20261106_101612`, `snapshot_path=universe/mcap_snapshot_20261106_101612.json` (present), `scanned_at=2026-11-06T10:16:12.893046+00:00`, source=CoinGecko public API `/api/v3/coins/markets` (usd, market_cap_desc), 20/20 pages/2000 entries, `lowest_rank_covered=2000`, `lowest_market_cap_usd=3179353`, `coverage_reaches_below_floor=true`, `universe_n=275`, `expansion_floor={PIXEL/USDT, $3,254,887}`, `eligible_unseen_below_floor_count=0`, `eligible_unseen_below_floor=[]`, `batch_selected=[]`.
- Guards re-verified: `data/fixtures/SUKU_USDT.csv` ABSENT; no `*SUKU*` anywhere in the tree → `--apply` MUST NOT run without verified fixture/grid coverage for any selected candidate. Baseline grid `results/20261019_135940_grid/progress.json` complete; `results/FINAL_DECISION.md` preserved (program-level rejection).
- Nothing actionable before `2026-11-07T10:16:12.893046+00:00`. Rely on retained wakeup `wku_1b3cb2ba10013PChsdJTbjSl1z` (due 2026-11-07T10:21:00Z); no duplicate scheduled.
