# NEXT_AGENT_TASK.md — EMA hourly continuation universe-refresh gate

**Task:** Resume the EMA hourly continuation universe-refresh gate. Read `README.md`, `AGENTS.md`, and this file before acting.

## Current state (re-verified 2026-11-08T19:54Z, offline)
- Source of truth `universe/last_scan.json` (JSON valid): state=`AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot_id=`mcap_snapshot_20261108_152931`, snapshot_path=`universe/mcap_snapshot_20261108_152931.json` (present), scanned_at=`2026-11-08T15:29:31.554859+00:00`, source=CoinGecko public API `/api/v3/coins/markets` (usd, market_cap_desc).
- `next_eligible_refresh_at` = `2026-11-09T15:29:31.554859+00:00`. **NOT ELIGIBLE** at `2026-11-08T19:54:26Z` (independent `date -u`): remaining ≈ 19h35m05s. Reason (PROMPT.md §2.1.5): 24h refresh bound has not elapsed. Gate opens **2026-11-09T15:29:31.554859Z**.
- Coverage: pages_requested=20, pages_fetched=20, all_requested_pages_returned=true, entries_count=2000, lowest_rank_covered=2000, lowest_market_cap_usd=3163327, `coverage_reaches_below_floor=true`.
- Universe: n=275, expansion_floor={ALPINE/USDT, $3,277,456}, eligible_unseen_below_floor_count=0, eligible_unseen_below_floor=[], batch_selected=[].
- Coverage guard: `data/fixtures/SUKU_USDT.csv` ABSENT. **`--apply` MUST NOT run** without verified fixture + baseline grid coverage for every selected candidate.
- Baseline grid `results/20261019_135940_grid/progress.json` complete; `results/FINAL_DECISION.md` preserved. EMA signal/fill/cost assumptions unchanged.

## Prior snapshot pass (2026-11-08T15:29Z, gate was eligible)
- Ran **one** 20-page snapshot pass (no `--apply`): `PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`. New snapshot `universe/mcap_snapshot_20261108_152931.json`: 2000 entries, pages 20/20, all_requested_pages_returned=true, lowest covered rank 2000 ($3,163,327), `coverage_reaches_below_floor=true`.
- Expansion floor recomputed from fresh snapshot vs included-universe fixtures: **ALPINE/USDT at $3,277,456** (was PIXEL/USDT $3,190,848; PIXEL now excluded/None in fresh snapshot). Several previously-included names now have None mcap in fresh snapshot (PIXEL, ALEX, CWEB, TRADE, BOSON).
- Eligible unseen names below floor: **0** → state remains `AWAITING_NEW_ELIGIBLE_CANDIDATES`. `batch_selected=[]`. No `--apply` run (no candidates selected; SUKU fixture still absent anyway).
- Updated `universe/last_scan.json`: state=`AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot_id=`mcap_snapshot_20261108_152931`, snapshot_path=`universe/mcap_snapshot_20261108_152931.json`, scanned_at=`2026-11-08T15:29:31.554859+00:00`, coverage 20/20/2000/below floor, floor ALPINE/USDT $3,277,456, `eligible_unseen_below_floor_count=0`, `next_eligible_refresh_at=2026-11-09T15:29:31.554859+00:00`.

## Offline gate-check records (this session, no provider calls)
- 2026-11-08T19:54Z: NOT ELIGIBLE. now=`2026-11-08T19:54:26Z`, bound=`2026-11-09T15:29:31.554859+00:00`, remaining ≈ 19h35m05s (70505s). State unchanged: snapshot_id=`mcap_snapshot_20261108_152931`, scanned_at=`2026-11-08T15:29:31.554859+00:00`, coverage 20/20/2000/below floor, floor ALPINE/USDT $3,277,456, `eligible_unseen_below_floor_count=0`, `batch_selected=[]`. SUKU guard: `data/fixtures/SUKU_USDT.csv` ABSENT. No provider calls, no `--apply`, no grid reruns, no EMA signal/fill/cost assumption changes.

## Next agent — clear initial task
1. **Offline first:** read `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md`, and `universe/last_scan.json`. Recompute eligibility from `next_eligible_refresh_at` vs independent UTC time; do not guess. Gate opens **2026-11-09T15:29:31.554859Z**.
2. **If not eligible (expected until gate opens):** make **no provider calls**. Append a brief offline-check record (exact now/bound/remaining, state evidence, SUKU guard status) to `NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md`; stop. Do not schedule duplicate wakeups.
3. **If eligible:** run **at most one** 20-page snapshot pass: `PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20` (no `--apply`). Recompute floor vs included-universe fixtures, inspect below-floor band, and update `universe/last_scan.json` (snapshot path/id, scanned_at, coverage, floor, eligible_unseen_below_floor, `next_eligible_refresh_at`). Before any `--apply`, verify fixture + baseline grid coverage for every selected candidate; **do not apply** without verified coverage (SUKU fixture absent).
4. **Never:** rerun grids, fetch candles, place orders, change EMA signal/fill/cost assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory. Preserve negative/blocked results and `results/FINAL_DECISION.md`. Historical research only; free public data/no-cost tooling; follow `AGENTS.md` adaptive gate policy.