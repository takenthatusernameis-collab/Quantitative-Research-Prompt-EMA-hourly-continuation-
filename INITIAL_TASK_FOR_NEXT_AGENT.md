# INITIAL_TASK_FOR_NEXT_AGENT.md — EMA hourly continuation universe-refresh gate

## Status at handoff (2026-11-11T00:06Z)

Gate state: **EXPANSION_AVAILABLE** — a fresh snapshot pass has just completed and there are eligible expansion candidates, but `--apply` is BLOCKED pending fixture + baseline grid coverage.

- `universe/last_scan.json` (JSON valid): state=`EXPANSION_AVAILABLE`, snapshot_id=`mcap_snapshot_20261111_000546`, snapshot_path=`universe/mcap_snapshot_20261111_000546.json` (present, 543,959 bytes), scanned_at=`2026-11-11T00:05:46.653861+00:00`, source=CoinGecko public API `/api/v3/coins/markets` (usd, market_cap_desc).
- Coverage: pages 20/20, entries_count=2000, all_requested_pages_returned=true, lowest_rank_covered=2000, lowest_market_cap_usd=$3,008,633, `coverage_reaches_below_floor=true`.
- Expansion floor (recomputed vs included-universe fixtures): **PIXEL/USDT $3,222,550**.
- Eligible unseen names below the floor: **3** → `batch_selected=[DENT/USDT, SUKU/USDT, ESE/USDT]`:
  - #1945 DENT mcap=$3,214,122
  - #1959 SUKU mcap=$3,170,943
  - #1998 ESE mcap=$3,026,755
- `--apply` was NOT run (dry run). Blocked: `data/fixtures/DENT_USDT.csv`, `data/fixtures/SUKU_USDT.csv`, `data/fixtures/ESE_USDT.csv` all **ABSENT** (`ls` = No such file or directory). `--apply` is prohibited without verified fixture + baseline grid coverage for every selected candidate.
- `next_eligible_refresh_at` = `2026-11-12T00:05:46.653861+00:00` (24 h after the just-completed pass). No provider calls (no fresh snapshot pass) until that bound elapses.
- Preserved artifacts present: `results/FINAL_DECISION.md` (23,304 bytes), `results/20261019_135940_grid/progress.json` (1,478,918 bytes), `universe/mcap_snapshot_20261111_000546.json`. EMA signal/fill/cost assumptions unchanged. Historical research only; no orders. No duplicate wakeups scheduled.

## Your task (in order)

1. **Read first:** `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md`, this file, and `universe/last_scan.json`.

2. **Do not run a fresh snapshot pass yet.** `next_eligible_refresh_at` = `2026-11-12T00:05:46.653861+00:00` has not elapsed; making another provider pass now would violate PROMPT.md §2.1.5 (one refresh per 24 h). Recompute eligibility from `next_eligible_refresh_at` vs independent UTC (`date -u`) before any provider call.

3. **Act on the existing batch (no provider call needed):** `batch_selected=[DENT/USDT, SUKU/USDT, ESE/USDT]` below floor PIXEL/USDT $3,222,550.
   - Verify fixture + baseline grid coverage for **every** selected candidate before any `--apply`.
   - Fixtures are currently ABSENT for all three (`data/fixtures/{DENT,SUKU,ESE}_USDT.csv`). If any fixture or its baseline grid coverage is missing/unverified, **do not run `--apply`**.
   - Record the coverage check outcome (fixture present/absent, grid coverage present/absent per candidate) in this file and `NEXT_AGENT_TASK.md`.

4. **If coverage is verified for all three candidates:** you may run `--apply` (one expansion) and update `universe/last_scan.json` accordingly (`universe_n`, batch applied). If coverage is NOT verified (expected: SUKU fixture absent): **do not apply**, record the blocker, and stop cleanly.

5. **Never:** rerun grids, fetch candles, place orders, change EMA signal/fill/cost assumptions, use fixtures as market evidence, blur confirmatory vs exploratory, or make repeat provider calls inside the 24 h window. Preserve negative/blocked results and `results/FINAL_DECISION.md`. Historical research only; free public data / no-cost tooling; follow `AGENTS.md` adaptive gate policy.

## Coverage check outcome (2026-11-11T00:08:30Z, offline, no provider calls)

- Independent UTC now = `2026-11-11T00:08:30Z`; `next_eligible_refresh_at` = `2026-11-12T00:05:46.653861+00:00` → 24 h bound NOT elapsed (~23 h 57 m remaining). No provider calls made; no fresh snapshot pass.
- Re-read `universe/last_scan.json` (JSON valid): state=`EXPANSION_AVAILABLE`, snapshot_id=`mcap_snapshot_20261111_000546`, batch_selected=[DENT/USDT, SUKU/USDT, ESE/USDT], expansion_floor=PIXEL/USDT $3,222,550, next_eligible_refresh_at=`2026-11-12T00:05:46.653861+00:00`.
- Fixture check (`data/fixtures/{SYMBOL}_USDT.csv`):
  - DENT/USDT: **ABSENT** (`ls` = No such file or directory)
  - SUKU/USDT: **ABSENT** (`ls` = No such file or directory)
  - ESE/USDT: **ABSENT** (`ls` = No such file or directory)
- Baseline grid coverage (`results/20261019_135940_grid/progress.json` symbols list, grep `DENT/USDT|SUKU/USDT|ESE/USDT`): no matches → **ABSENT** for all three.
- Coverage NOT verified for every selected candidate. `--apply` NOT run (dry run preserved).
- Blocker: fixture + baseline grid coverage absent for every selected candidate (`--apply` prohibited without verified coverage). Stop cleanly. No provider calls, no `--apply`, no grid reruns, no EMA signal/fill/cost changes. Historical research only; no orders. No duplicate wakeups scheduled.

## Clear initial task for next agent (measurable)

Recompute eligibility from `next_eligible_refresh_at` vs independent UTC; if the 24 h bound has not elapsed, make no provider calls, record an offline-check record, and stop. If coverage is verified for all batch candidates, run `--apply` once and update `universe/last_scan.json`; otherwise record the blocker (fixture/grid coverage absent) and stop. Do not schedule duplicate wakeups.
