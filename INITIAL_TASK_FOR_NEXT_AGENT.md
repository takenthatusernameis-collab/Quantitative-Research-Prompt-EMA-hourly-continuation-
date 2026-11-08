# INITIAL_TASK_FOR_NEXT_AGENT.md — EMA hourly continuation universe-refresh gate

## Initial task message for the next agent (current as of 2026-11-08T20:07Z)

**Your job:** resume the EMA hourly continuation universe-refresh gate. Nothing is eligible yet; do an offline gate check first, then act only if the gate has opened.

**Step 1 — Offline first (do this before any provider call):**
1. Read `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md`, `universe/last_scan.json`.
2. Recompute eligibility from `next_eligible_refresh_at` in `universe/last_scan.json` against an **independent** UTC source (`date -u`). Do not guess.
3. Confirm `data/fixtures/SUKU_USDT.csv` is absent — `--apply` is prohibited without verified fixture + baseline grid coverage for every selected candidate.

**Step 2 — If NOT eligible (expected; gate opens 2026-11-09T15:29:31.554859Z):**
- Make **no provider calls**.
- Append a brief offline-check record (exact now / bound / remaining / state evidence / SUKU guard status) to `NEXT_AGENT_TASK.md` and this file.
- Stop. Do **not** schedule duplicate wakeups.

**Step 3 — If eligible (gate opens 2026-11-09T15:29:31.554859Z):**
- Run **at most one** 20-page snapshot pass (no `--apply`):
  `PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`
- Recompute the expansion floor vs included-universe fixtures, inspect the below-floor band, and update `universe/last_scan.json` (snapshot path/id, scanned_at, coverage, floor, `eligible_unseen_below_floor`, `next_eligible_refresh_at`).
- Before **any** `--apply`, verify fixture + baseline grid coverage for every selected candidate; **do not apply** without verified coverage (SUKU fixture absent).

**Never:** rerun grids, fetch candles, place orders, change EMA signal/fill/cost assumptions, use fixtures as market evidence, or blur confirmatory vs exploratory. Preserve negative/blocked results and `results/FINAL_DECISION.md`. Historical research only; free public data / no-cost tooling; follow `AGENTS.md` adaptive gate policy.

## Current state (re-verified 2026-11-08T20:07Z, offline)
- `universe/last_scan.json` (JSON valid, re-read): state=`AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot_id=`mcap_snapshot_20261108_152931`, snapshot_path=`universe/mcap_snapshot_20261108_152931.json` (present, 543,610 bytes), scanned_at=`2026-11-08T15:29:31.554859+00:00`, source=CoinGecko public API `/api/v3/coins/markets` (usd, market_cap_desc).
- `next_eligible_refresh_at` = `2026-11-09T15:29:31.554859+00:00`. **NOT ELIGIBLE** at `2026-11-08T20:07:19Z` (independent `date -u` = `2026-11-08T20:07:19Z`): remaining ≈ **19h22m12s** (69732s). Reason (PROMPT.md §2.1.5): 24h refresh bound has not elapsed. Gate opens **2026-11-09T15:29:31.554859Z**.
- Coverage: pages_requested=20, pages_fetched=20, all_requested_pages_returned=true, entries_count=2000, lowest_rank_covered=2000, lowest_market_cap_usd=3163327, `coverage_reaches_below_floor=true`.
- Universe: n=275, expansion_floor={ALPINE/USDT, $3,277,456}, eligible_unseen_below_floor_count=0, eligible_unseen_below_floor=[], batch_selected=[].
- Coverage guard: `data/fixtures/SUKU_USDT.csv` **ABSENT** (`find . -iname '*suku*'` = 0 matches). **`--apply` MUST NOT run** without verified fixture + baseline grid coverage for every selected candidate.
- Preserved artifacts: `results/FINAL_DECISION.md` (23,304 bytes), `results/20261019_135940_grid/progress.json` (1,478,918 bytes), `universe/mcap_snapshot_20261108_152931.json` (543,610 bytes) present. EMA signal/fill/cost assumptions unchanged. No provider calls, no snapshot/candle fetches, no `--apply`, no grid reruns. Historical research only; no orders.

## Completed this turn (2026-11-08T20:07Z, offline gate check)
- Re-verified gate eligibility from `universe/last_scan.json` (JSON valid, re-read) + independent UTC (`date -u` = `2026-11-08T20:07:19Z`): **NOT ELIGIBLE**. `next_eligible_refresh_at=2026-11-09T15:29:31.554859+00:00` (scanned_at `2026-11-08T15:29:31.554859+00:00`), remaining ≈ **19h22m12s** (69732s). Reason (PROMPT.md §2.1.5): 24h refresh bound has not elapsed. Gate opens **2026-11-09T15:29:31.554859Z**.
- **No provider calls** (offline check only). State unchanged: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot_id=`mcap_snapshot_20261108_152931`, snapshot_path=`universe/mcap_snapshot_20261108_152931.json` present (543,610 bytes), scanned_at=`2026-11-08T15:29:31.554859+00:00`, coverage 20/20 pages / 2000 entries / `all_requested_pages_returned=true` / `coverage_reaches_below_floor=true` / lowest rank 2000 / lowest mcap $3,163,327, universe_n=275, expansion floor ALPINE/USDT $3,277,456, `eligible_unseen_below_floor_count=0`, `batch_selected=[]`.
- Preserved artifacts re-verified present: `results/FINAL_DECISION.md` (23,304 bytes), `results/20261019_135940_grid/progress.json` (1,478,918 bytes), `universe/mcap_snapshot_20261108_152931.json` (543,610 bytes).
- Coverage guard rechecked: `data/fixtures/SUKU_USDT.csv` **ABSENT** (`find . -iname '*suku*'` = 0 matches). `--apply` prohibited without verified fixture + baseline grid coverage for every selected candidate. No snapshot/candle fetches, no `--apply`, no grid reruns, no EMA signal/fill/cost assumption changes. No duplicate wakeups scheduled. Historical research only; no orders.

## Completed this turn (2026-11-08T20:16Z, offline gate check)
- Re-verified gate eligibility from `universe/last_scan.json` (JSON valid, re-read) + independent UTC (`date -u` = `2026-11-08T20:16:10Z`): **NOT ELIGIBLE**. `next_eligible_refresh_at=2026-11-09T15:29:31.554859+00:00` (scanned_at `2026-11-08T15:29:31.554859+00:00`), remaining ≈ **19h13m10s** (69190s). Reason (PROMPT.md §2.1.5): 24h refresh bound has not elapsed. Gate opens **2026-11-09T15:29:31.554859Z**.
- **No provider calls** (offline check only). State unchanged: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot_id=`mcap_snapshot_20261108_152931`, snapshot_path=`universe/mcap_snapshot_20261108_152931.json` present (543,610 bytes), scanned_at=`2026-11-08T15:29:31.554859+00:00`, coverage 20/20 pages / 2000 entries / `all_requested_pages_returned=true` / `coverage_reaches_below_floor=true` / lowest rank 2000 / lowest mcap $3,163,327, universe_n=275, expansion floor ALPINE/USDT $3,277,456, `eligible_unseen_below_floor_count=0`, `batch_selected=[]`.
- Preserved artifacts re-verified present: `results/FINAL_DECISION.md` (23,304 bytes), `results/20261019_135940_grid/progress.json` (1,478,918 bytes), `universe/mcap_snapshot_20261108_152931.json` (543,610 bytes).
- Coverage guard rechecked: `data/fixtures/SUKU_USDT.csv` **ABSENT** (`find . -iname '*suku*'` = 0 matches). `--apply` prohibited without verified fixture + baseline grid coverage for every selected candidate. No snapshot/candle fetches, no `--apply`, no grid reruns, no EMA signal/fill/cost assumption changes. No duplicate wakeups scheduled. Historical research only; no orders.

## Prior checks (preserved)
- 2026-11-08T20:06Z: NOT ELIGIBLE (remaining ≈ 19h23m15s at 20:06:16Z). State/snapshot unchanged; SUKU absent; no provider calls. See `NEXT_AGENT_TASK.md`.
- 2026-11-08T20:01Z: NOT ELIGIBLE (remaining ≈ 19h27m38s at 20:01:53Z). State/snapshot unchanged; SUKU absent; no provider calls. See `NEXT_AGENT_TASK.md`.
- 2026-11-08T19:58Z: NOT ELIGIBLE (remaining ≈ 19h31m04s at 19:58:27Z). State/snapshot unchanged; SUKU absent; no provider calls. See `NEXT_AGENT_TASK.md`.
- 2026-11-08T19:54Z: NOT ELIGIBLE (remaining ≈ 19h35m05s at 19:54:26Z). State/snapshot unchanged; SUKU absent; no provider calls. See `NEXT_AGENT_TASK.md`.

## Completed this turn (2026-11-08T20:12Z, offline gate check)
- Re-verified gate eligibility from `universe/last_scan.json` (JSON valid, re-read) + independent UTC (`date -u` = `2026-11-08T20:12:25Z`): **NOT ELIGIBLE**. `next_eligible_refresh_at=2026-11-09T15:29:31.554859+00:00` (scanned_at `2026-11-08T15:29:31.554859+00:00`), remaining ≈ **19h17m06s** (69426s). Reason (PROMPT.md §2.1.5): 24h refresh bound has not elapsed. Gate opens **2026-11-09T15:29:31.554859Z**.
- **No provider calls** (offline check only). State unchanged: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot_id=`mcap_snapshot_20261108_152931`, snapshot_path=`universe/mcap_snapshot_20261108_152931.json` present (543,610 bytes), scanned_at=`2026-11-08T15:29:31.554859+00:00`, coverage 20/20 pages / 2000 entries / `all_requested_pages_returned=true` / `coverage_reaches_below_floor=true` / lowest rank 2000 / lowest mcap $3,163,327, universe_n=275, expansion floor ALPINE/USDT $3,277,456, `eligible_unseen_below_floor_count=0`, `batch_selected=[]`.
- Preserved artifacts re-verified present: `results/FINAL_DECISION.md` (23,304 bytes), `results/20261019_135940_grid/progress.json` (1,478,918 bytes), `universe/mcap_snapshot_20261108_152931.json` (543,610 bytes).
- Coverage guard rechecked: `data/fixtures/SUKU_USDT.csv` **ABSENT** (`find . -iname '*suku*'` = 0 matches). `--apply` prohibited without verified fixture + baseline grid coverage for every selected candidate. No snapshot/candle fetches, no `--apply`, no grid reruns, no EMA signal/fill/cost assumption changes. No duplicate wakeups scheduled. Historical research only; no orders.

## Completed this turn (2026-11-08T20:16Z, offline gate check)
- Re-verified gate eligibility from `universe/last_scan.json` (JSON valid, re-read) + independent UTC (`date -u` = `2026-11-08T20:16:10Z`): **NOT ELIGIBLE**. `next_eligible_refresh_at=2026-11-09T15:29:31.554859+00:00` (scanned_at `2026-11-08T15:29:31.554859+00:00`), remaining ≈ **19h13m10s** (69190s). Reason (PROMPT.md §2.1.5): 24h refresh bound has not elapsed. Gate opens **2026-11-09T15:29:31.554859Z**.
- **No provider calls** (offline check only). State unchanged: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot_id=`mcap_snapshot_20261108_152931`, snapshot_path=`universe/mcap_snapshot_20261108_152931.json` present (543,610 bytes), scanned_at=`2026-11-08T15:29:31.554859+00:00`, coverage 20/20 pages / 2000 entries / `all_requested_pages_returned=true` / `coverage_reaches_below_floor=true` / lowest rank 2000 / lowest mcap $3,163,327, universe_n=275, expansion floor ALPINE/USDT $3,277,456, `eligible_unseen_below_floor_count=0`, `batch_selected=[]`.
- Preserved artifacts re-verified present: `results/FINAL_DECISION.md` (23,304 bytes), `results/20261019_135940_grid/progress.json` (1,478,918 bytes), `universe/mcap_snapshot_20261108_152931.json` (543,610 bytes).
- Coverage guard rechecked: `data/fixtures/SUKU_USDT.csv` **ABSENT** (`find . -iname '*suku*'` = 0 matches). `--apply` prohibited without verified fixture + baseline grid coverage for every selected candidate. No snapshot/candle fetches, no `--apply`, no grid reruns, no EMA signal/fill/cost assumption changes. No duplicate wakeups scheduled. Historical research only; no orders.

## Completed this turn (2026-11-08T20:15Z, offline gate check)
- Re-verified gate eligibility from `universe/last_scan.json` (JSON valid, re-read) + independent UTC (`date -u` = `2026-11-08T20:15:19Z`): **NOT ELIGIBLE**. `next_eligible_refresh_at=2026-11-09T15:29:31.554859+00:00` (scanned_at `2026-11-08T15:29:31.554859+00:00`), remaining ≈ **19h14m12s** (69252s). Reason (PROMPT.md §2.1.5): 24h refresh bound has not elapsed. Gate opens **2026-11-09T15:29:31.554859Z**.
- **No provider calls** (offline check only). State unchanged: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot_id=`mcap_snapshot_20261108_152931`, snapshot_path=`universe/mcap_snapshot_20261108_152931.json` present (543,610 bytes), scanned_at=`2026-11-08T15:29:31.554859+00:00`, coverage 20/20 pages / 2000 entries / `all_requested_pages_returned=true` / `coverage_reaches_below_floor=true` / lowest rank 2000 / lowest mcap $3,163,327, universe_n=275, expansion floor ALPINE/USDT $3,277,456, `eligible_unseen_below_floor_count=0`, `batch_selected=[]`.
- Preserved artifacts re-verified present: `results/FINAL_DECISION.md` (23,304 bytes), `results/20261019_135940_grid/progress.json` (1,478,918 bytes), `universe/mcap_snapshot_20261108_152931.json` (543,610 bytes).
- Coverage guard rechecked: `data/fixtures/SUKU_USDT.csv` **ABSENT** (`find . -iname '*suku*'` = 0 matches). `--apply` prohibited without verified fixture + baseline grid coverage for every selected candidate. No snapshot/candle fetches, no `--apply`, no grid reruns, no EMA signal/fill/cost assumption changes. No duplicate wakeups scheduled. Historical research only; no orders.

## Completed this turn (2026-11-08T20:16Z, offline gate check)
- Re-verified gate eligibility from `universe/last_scan.json` (JSON valid, re-read) + independent UTC (`date -u` = `2026-11-08T20:16:10Z`): **NOT ELIGIBLE**. `next_eligible_refresh_at=2026-11-09T15:29:31.554859+00:00` (scanned_at `2026-11-08T15:29:31.554859+00:00`), remaining ≈ **19h13m10s** (69190s). Reason (PROMPT.md §2.1.5): 24h refresh bound has not elapsed. Gate opens **2026-11-09T15:29:31.554859Z**.
- **No provider calls** (offline check only). State unchanged: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot_id=`mcap_snapshot_20261108_152931`, snapshot_path=`universe/mcap_snapshot_20261108_152931.json` present (543,610 bytes), scanned_at=`2026-11-08T15:29:31.554859+00:00`, coverage 20/20 pages / 2000 entries / `all_requested_pages_returned=true` / `coverage_reaches_below_floor=true` / lowest rank 2000 / lowest mcap $3,163,327, universe_n=275, expansion floor ALPINE/USDT $3,277,456, `eligible_unseen_below_floor_count=0`, `batch_selected=[]`.
- Preserved artifacts re-verified present: `results/FINAL_DECISION.md` (23,304 bytes), `results/20261019_135940_grid/progress.json` (1,478,918 bytes), `universe/mcap_snapshot_20261108_152931.json` (543,610 bytes).
- Coverage guard rechecked: `data/fixtures/SUKU_USDT.csv` **ABSENT** (`find . -iname '*suku*'` = 0 matches). `--apply` prohibited without verified fixture + baseline grid coverage for every selected candidate. No snapshot/candle fetches, no `--apply`, no grid reruns, no EMA signal/fill/cost assumption changes. No duplicate wakeups scheduled. Historical research only; no orders.
