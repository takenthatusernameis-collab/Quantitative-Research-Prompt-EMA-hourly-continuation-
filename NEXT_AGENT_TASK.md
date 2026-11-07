# NEXT_AGENT_TASK.md — EMA hourly continuation universe-refresh gate

**Task:** Resume the EMA hourly continuation universe-refresh gate. Read `README.md`, `AGENTS.md`, and this file before acting.

## Current state (re-verified 2026-11-07T15:16Z)
- Source of truth `universe/last_scan.json` (JSON valid): `next_eligible_refresh_at` = `2026-11-08T15:12:00.314643+00:00`. **NOT ELIGIBLE** at `2026-11-07T15:16:57Z` (independent `date -u` cross-check): eligible=false, remaining ≈ 23h55m03s.
- State: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, recorded_at=`2026-11-07T15:15:21.048234+00:00`, snapshot_id=`mcap_snapshot_20261107_151200`, snapshot_path=`universe/mcap_snapshot_20261107_151200.json` (present), scanned_at=`2026-11-07T15:12:00.314643+00:00`, source=CoinGecko public API `/api/v3/coins/markets` (usd, market_cap_desc).
- Coverage: pages_requested=20, pages_fetched=20, all_requested_pages_returned=true, entries_count=2000, lowest_rank_covered=2000, lowest_market_cap_usd=3140232, `coverage_reaches_below_floor=true`.
- Universe: n=275, expansion_floor={PIXEL/USDT, $3,190,848} (recomputed from fresh snapshot vs included universe fixtures), eligible_unseen_below_floor_count=0, eligible_unseen_below_floor=[], batch_selected=[].
- Coverage guard: `data/fixtures/SUKU_USDT.csv` ABSENT; no `*SUKU*` files under repo root fixtures/results context relevant to guard. **`--apply` MUST NOT run** without verified fixture/grid coverage for any selected candidate.
- Baseline grid `results/20261019_135940_grid/progress.json` complete (18,150 cells, 275 symbols × 66 pairs, 0 blocked, `all_symbols_processed=true`, `next_cell=null`). `results/FINAL_DECISION.md` preserved (program-level rejection, 0 credible candidates). EMA signal/fill/cost assumptions unchanged.

## Completed this turn (2026-11-07T15:16Z)
- Re-verified gate eligibility from `universe/last_scan.json`: eligible=false, `next_eligible_refresh_at=2026-11-08T15:12:00.314643+00:00`, remaining ≈ 23h55m03s. **No provider calls** made (offline check only).
- Updated `INITIAL_TASK_FOR_NEXT_AGENT.md` and this file with the offline check record.

## Completed this turn (2026-11-07T15:22Z)
- Re-verified gate eligibility from `universe/last_scan.json` (JSON valid, re-read): eligible=false, `next_eligible_refresh_at=2026-11-08T15:12:00.314643+00:00`, now=2026-11-07T15:22:45Z (independent `date -u`), remaining ≈ 23h49m15s. Reason (PROMPT.md §2.1.5): 24h refresh bound has not elapsed. **No provider calls** made (offline check only).
- State unchanged: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot_id=`mcap_snapshot_20261107_151200`, snapshot_path present, scanned_at=2026-11-07T15:12:00.314643+00:00, coverage 20/20 pages/2000 entries/below floor, floor PIXEL/USDT $3,190,848, eligible_unseen_below_floor_count=0, batch_selected=[].
- `data/fixtures/SUKU_USDT.csv` still absent (coverage guard holds). Baseline grid `results/20261019_135940_grid` complete; `results/FINAL_DECISION.md` preserved. No grids/candles/EMA/cost/fill changes.

## Completed this turn (2026-11-07T15:25Z)
- Re-verified gate eligibility from `universe/last_scan.json` (JSON valid, re-read): eligible=false, `next_eligible_refresh_at=2026-11-08T15:12:00.314643+00:00`, now=2026-11-07T15:25:51Z (independent `date -u`), remaining ≈ 23h46m09s. Reason (PROMPT.md §2.1.5): 24h refresh bound has not elapsed. **No provider calls** made (offline check only).
- State unchanged: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot_id=`mcap_snapshot_20261107_151200`, snapshot_path present, scanned_at=2026-11-07T15:12:00.314643+00:00, coverage 20/20 pages/2000 entries/below floor, floor PIXEL/USDT $3,190,848, eligible_unseen_below_floor_count=0, batch_selected=[].
- `data/fixtures/SUKU_USDT.csv` still absent (coverage guard holds). Baseline grid `results/20261019_135940_grid` complete; `results/FINAL_DECISION.md` preserved. No grids/candles/EMA/cost/fill changes.

## Completed this turn (2026-11-07T15:33Z)
- Re-verified gate eligibility from `universe/last_scan.json` (JSON valid, re-read): eligible=false, `next_eligible_refresh_at=2026-11-08T15:12:00.314643+00:00`, now=2026-11-07T15:33:54Z (independent `date -u`), remaining ≈ 23h38m06s. Reason (PROMPT.md §2.1.5): 24h refresh bound has not elapsed. **No provider calls** made (offline check only).
- State unchanged: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot_id=`mcap_snapshot_20261107_151200`, snapshot_path present (verified on disk), scanned_at=`2026-11-07T15:12:00.314643+00:00`, coverage 20/20 pages/2000 entries/below floor, floor PIXEL/USDT $3,190,848, eligible_unseen_below_floor_count=0, batch_selected=[].
- `data/fixtures/SUKU_USDT.csv` still absent (coverage guard holds); `find -iname '*suku*'` returns nothing in repo. Baseline grid `results/20261019_135940_grid` complete; `results/FINAL_DECISION.md` preserved. No grids/candles/EMA/cost/fill changes.

## Wakeup
No wakeup scheduled by this agent (environment may not persist agent-scheduled wakeups across runs; rely on next activation). Next eligible gate opens `2026-11-08T15:12:00.314643+00:00`.

## Completed this turn (2026-11-07T15:30Z)
- Re-verified gate eligibility from `universe/last_scan.json` (JSON valid, re-read): eligible=false, `next_eligible_refresh_at=2026-11-08T15:12:00.314643+00:00`, now=2026-11-07T15:30:04Z (independent `date -u`), remaining ≈ 23h41m56s. Reason (PROMPT.md §2.1.5): 24h refresh bound has not elapsed. **No provider calls** made (offline check only).
- State unchanged: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot_id=`mcap_snapshot_20261107_151200`, snapshot_path present, scanned_at=2026-11-07T15:12:00.314643+00:00, coverage 20/20 pages/2000 entries/below floor, floor PIXEL/USDT $3,190,848, eligible_unseen_below_floor_count=0, batch_selected=[].
- `data/fixtures/SUKU_USDT.csv` still absent (coverage guard holds). Baseline grid `results/20261019_135940_grid` complete; `results/FINAL_DECISION.md` preserved. No grids/candles/EMA/cost/fill changes.

## Completed this turn (2026-11-07T15:31Z)
- Re-verified gate eligibility from `universe/last_scan.json` (JSON valid, re-read): eligible=false, `next_eligible_refresh_at=2026-11-08T15:12:00.314643+00:00`, now=2026-11-07T15:31:17Z (independent `date -u`), remaining ≈ 23h40m43s. Reason (PROMPT.md §2.1.5): 24h refresh bound has not elapsed.
- State unchanged: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot_id=`mcap_snapshot_20261107_151200`, coverage 20/20/2000/below floor, floor PIXEL/USDT $3,190,848, eligible_unseen_below_floor_count=0, batch_selected=[].
- `data/fixtures/SUKU_USDT.csv` still absent (coverage guard holds). Baseline grid `results/20261019_135940_grid` complete; `results/FINAL_DECISION.md` preserved. No grids/candles/EMA/cost/fill changes.

## Completed this turn (2026-11-07T15:35Z)
- Re-verified gate eligibility from `universe/last_scan.json` (JSON valid, re-read) + independent `date -u`: eligible=false, `next_eligible_refresh_at=2026-11-08T15:12:00.314643+00:00`, now=2026-11-07T15:34:59Z, remaining ≈ 23h37m01s. Reason (PROMPT.md §2.1.5): 24h refresh bound has not elapsed. **No provider calls** made (offline check only).
- State unchanged: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot_id=`mcap_snapshot_20261107_151200`, snapshot_path present (verified), scanned_at=`2026-11-07T15:12:00.314643+00:00`, coverage 20/20 pages/2000 entries/below floor, floor PIXEL/USDT $3,190,848, eligible_unseen_below_floor_count=0, batch_selected=[].
- `data/fixtures/SUKU_USDT.csv` still absent (coverage guard holds; `find -iname '*suku*'` returns nothing). Baseline grid `results/20261019_135940_grid` complete; `results/FINAL_DECISION.md` preserved. No grids/candles/EMA/cost/fill changes.

## Completed this turn (2026-11-07T19:10Z)
- Re-verified gate eligibility from `universe/last_scan.json` (JSON valid, re-read): **NOT ELIGIBLE**. `next_eligible_refresh_at=2026-11-08T15:12:00.314643+00:00`, independent `date -u` = `2026-11-07T19:10:27Z`, remaining ≈ 20h01m33s. Reason (PROMPT.md §2.1.5): 24h refresh bound has not elapsed since `scanned_at=2026-11-07T15:12:00.314643Z`.
- **No provider calls** (offline check only). State unchanged: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot_id=`mcap_snapshot_20261107_151200`, snapshot_path=`universe/mcap_snapshot_20261107_151200.json`, coverage 20/20 pages / 2000 entries / `coverage_reaches_below_floor=true` / lowest rank 2000 / lowest mcap $3,140,232, floor PIXEL/USDT $3,190,848, `eligible_unseen_below_floor_count=0`, `batch_selected=[]`.
- Coverage guard rechecked: `data/fixtures/SUKU_USDT.csv` **ABSENT** — `--apply` must not run without verified fixture + baseline grid coverage for every selected candidate. `results/FINAL_DECISION.md` present; baseline grid `results/20261019_135940_grid` preserved. No snapshot/candle fetches, no `--apply`, no grid reruns, no EMA signal/fill/cost assumption changes.

## Completed this turn (2026-11-07T19:13Z)
- Re-verified gate eligibility from `universe/last_scan.json` (JSON valid, re-read): **NOT ELIGIBLE**. `next_eligible_refresh_at=2026-11-08T15:12:00.314643+00:00`, independent `date -u` = `2026-11-07T19:13:52Z`, remaining ≈ 19h58m08s. Reason (PROMPT.md §2.1.5): 24h refresh bound has not elapsed since `scanned_at=2026-11-07T15:12:00.314643Z`.
- **No provider calls** (offline check only). State unchanged: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot_id=`mcap_snapshot_20261107_151200`, snapshot_path=`universe/mcap_snapshot_20261107_151200.json` (present), scanned_at=`2026-11-07T15:12:00.314643+00:00`, coverage 20/20 pages / 2000 entries / `coverage_reaches_below_floor=true` / lowest rank 2000 / lowest mcap $3,140,232, floor PIXEL/USDT $3,190,848, `eligible_unseen_below_floor_count=0`, `batch_selected=[]`.
- Coverage guard rechecked: `data/fixtures/SUKU_USDT.csv` **ABSENT** — `--apply` must not run without verified fixture + baseline grid coverage for every selected candidate. `results/FINAL_DECISION.md` present; baseline grid `results/20261019_135940_grid` preserved. No snapshot/candle fetches, no `--apply`, no grid reruns, no EMA signal/fill/cost assumption changes.

## Next agent — clear initial task
1. **Offline first:** read `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md`, and `universe/last_scan.json`. Recompute eligibility from `next_eligible_refresh_at` vs independent UTC time; do not guess. Gate opens **2026-11-08T15:12:00.314643Z**.
2. **If not eligible (expected until gate opens):** make **no provider calls**. Append a brief offline-check record (exact now/bound/remaining, state evidence, SUKU guard status) to `NEXT_AGENT_TASK.md` and, if useful, `INITIAL_TASK_FOR_NEXT_AGENT.md`; stop. Do not schedule duplicate wakeups.
3. **If eligible:** run **at most one** 20-page snapshot pass: `PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20` (no `--apply`). Recompute floor vs included-universe fixtures, inspect below-floor band, and update `universe/last_scan.json` (snapshot path/id, scanned_at, coverage, floor, eligible_unseen_below_floor, `next_eligible_refresh_at`). Before any `--apply`, verify fixture + baseline grid coverage for every selected candidate; **do not apply** without verified coverage (SUKU fixture absent).
4. **Never:** rerun grids, fetch candles, place orders, change EMA signal/fill/cost assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory. Preserve negative/blocked results and `results/FINAL_DECISION.md`. Historical research only; free public data/no-cost tooling; follow `AGENTS.md` adaptive gate policy.
