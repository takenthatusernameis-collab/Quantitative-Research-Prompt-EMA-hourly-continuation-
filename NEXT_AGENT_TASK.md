# NEXT_AGENT_TASK.md — EMA hourly continuation universe-refresh gate

**Task:** Resume the EMA hourly continuation universe-refresh gate. Read `README.md`, `AGENTS.md`, and this file before acting.

## Current state (verified 2026-11-07T15:15Z)
- Source of truth `universe/last_scan.json` (JSON valid): `next_eligible_refresh_at` = `2026-11-08T15:12:00.314643+00:00`. **NOT ELIGIBLE** at `2026-11-07T15:15:12Z` (independent `datetime.now(timezone.utc)` cross-check): eligible=false, remaining ≈ 23h56m48s.
- State: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, recorded_at=`2026-11-07T15:15:12.465157+00:00`, snapshot_id=`mcap_snapshot_20261107_151200`, snapshot_path=`universe/mcap_snapshot_20261107_151200.json` (present), scanned_at=`2026-11-07T15:12:00.314643+00:00`, source=CoinGecko public API `/api/v3/coins/markets` (usd, market_cap_desc).
- Coverage: pages_requested=20, pages_fetched=20, all_requested_pages_returned=true, entries_count=2000, lowest_rank_covered=2000, lowest_market_cap_usd=3140232, `coverage_reaches_below_floor=true`.
- Universe: n=275, expansion_floor={PIXEL/USDT, $3,190,848} (recomputed from fresh snapshot vs included universe fixtures), eligible_unseen_below_floor_count=0, eligible_unseen_below_floor=[], batch_selected=[].
- Coverage guard: `data/fixtures/SUKU_USDT.csv` ABSENT; no `*SUKU*` files under repo root fixtures/results context relevant to guard. **`--apply` MUST NOT run** without verified fixture/grid coverage for any selected candidate.
- Baseline grid `results/20261019_135940_grid/progress.json` complete (18,150 cells, 275 symbols × 66 pairs, 0 blocked, `all_symbols_processed=true`, `next_cell=null`). `results/FINAL_DECISION.md` preserved (program-level rejection, 0 credible candidates). EMA signal/fill/cost assumptions unchanged.

## Completed this turn (2026-11-07T14:57Z–15:15Z)
- Completed prior handoff task: gate was eligible at 2026-11-07T14:55Z (`now=2026-11-07T14:55:13.797829+00:00` >= bound `2026-11-07T10:16:12.893046+00:00`), so ran **exactly one** 20-page snapshot pass: `PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`. The provider pass completed and produced `universe/mcap_snapshot_20261107_151200.json` (fetched_at 2026-11-07T15:12:00.314643Z, 20/20 pages, 2000 entries, lowest_rank_covered=2000, lowest_market_cap_usd=$3,140,232). No `--apply`, no candle fetches, no grid reruns, no EMA/cost/fill changes.
- Recomputed floor/below-floor band from the new snapshot using `fetch_mcap_snapshot` helpers (fixture-aware ambiguity resolution): expansion floor PIXEL/USDT $3,190,848, `coverage_reaches_below_floor=true`, `eligible_unseen_below_floor_count=0`. Band genuinely inspected (coverage reached below floor); empty result is a temporary waiting state per PROMPT §2.1.5, not a stop.
- Updated `universe/last_scan.json` from new snapshot (`state=AWAITING_NEW_ELIGIBLE_CANDIDATES`, `next_eligible_refresh_at=2026-11-08T15:12:00.314643+00:00` = scanned_at + 24h). Updated `INITIAL_TASK_FOR_NEXT_AGENT.md`. No duplicate wakeup scheduled.

## What to do
1. Re-verify gate eligibility at start from `universe/last_scan.json` (do not guess). NOT ELIGIBLE until `2026-11-08T15:12:00.314643+00:00`.
2. If still not eligible: make **no provider calls**. Record an offline check here (exact now/bound/remaining, state evidence), update handoff if needed, and stop. Do not schedule duplicate wakeups.
3. If eligible: run **at most one** 20-page snapshot pass (`PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`), recompute the floor, inspect the below-floor band, update `universe/last_scan.json`, then review any new candidate(s) for fixture/grid coverage before any `--apply`. Do NOT apply without verified coverage.
4. Never: rerun grids, fetch candles, place orders, change EMA/cost/fill assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory.

## Constraints
Historical research only; no orders/live/paper trading; free public data/no-cost tooling; preserve EMA signal/fill/cost assumptions; preserve negative/blocked results; separate exploratory from confirmatory; follow `AGENTS.md` gate policy.

## Wakeup
No wakeup scheduled by this agent (environment may not persist agent-scheduled wakeups across runs; rely on next activation). Next eligible gate opens `2026-11-08T15:12:00.314643+00:00`.
