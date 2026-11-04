# INITIAL_TASK_FOR_NEXT_AGENT.md — EMA hourly continuation universe-refresh gate

**Task:** Resume the EMA hourly continuation universe-refresh gate. Read `README.md`, `AGENTS.md`, and this file before acting.

## Current state (as of 2026-11-04T16:19:17Z)

- Gate `next_eligible_refresh_at` = `2026-11-05T02:42:21.634264+00:00`. NOT ELIGIBLE (~10h23m remaining).
- `universe/last_scan.json` unchanged: state `EXPANSION_AVAILABLE`, snapshot `mcap_snapshot_20261104_024221`, universe_n=275, expansion_floor `ZKJ/USDT` $3,404,245, eligible_unseen_below_floor_count=1 (SUKU rank 1996, mcap $3,231,609), batch_selected=['SUKU/USDT'].
- SUKU has NO fixture (`data/fixtures/SUKU_USDT.csv` absent) and NO grid config in `results/` (grep -rl SUKU results/ returns none) → `--apply` must NOT run without coverage.
- Baseline grid `results/20261019_135940_grid` complete; mutations NOT_PROMOTED; `FINAL_DECISION.md` records program-level rejection. Git tree clean.

## What to do

1. Re-verify gate eligibility: compare current UTC time against `next_eligible_refresh_at` in `universe/last_scan.json`; confirm the file is unchanged.
2. If still not eligible: do nothing but record the offline check in `NEXT_AGENT_TASK.md`, update this handoff if needed, and await the scheduler wakeup. No provider calls.
3. If eligible: run at most one 20-page snapshot pass (`PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`), recompute the floor, inspect the below-floor band, update `universe/last_scan.json`, then review any new candidate(s) for fixture/grid coverage before any `--apply`. Do NOT apply without coverage.
4. Never: rerun grids, fetch candles, change costs/fills, or blur confirmatory vs exploratory.

## Constraints

Historical research only; no orders/live/paper trading; preserve EMA signal/fill/cost assumptions; no fixtures as market evidence; separate exploratory from confirmatory; preserve negative/blocked results; follow AGENTS.md gate policy.

## Wakeup

Retained: `wku_1a488323b001plz6i4dUtUGZkO` due `2026-11-05T02:45:00.000Z`. Do not re-schedule a duplicate.

---

- **2026-11-04T16:19:17Z** — Prior handoff read and completed (`INITIAL_TASK_FOR_NEXT_AGENT.md`). Offline gate re-check at env time `2026-11-04T16:19:17Z` (`date -u`). Source of truth `universe/last_scan.json` (read directly, 35 lines, JSON valid; unchanged vs prior record): `next_eligible_refresh_at` `2026-11-05T02:42:21.634264+00:00`, now `2026-11-04T16:19:17Z` → NOT ELIGIBLE (~10h23m remaining). Gate status re-derived independently via inline Python (json.load + datetime.fromisoformat): eligible=false, bound=`2026-11-05T02:42:21.634264+00:00`, now=`2026-11-04T16:21:03.633864+00:00`, remaining=10:21:18. State unchanged: recorded_at=`2026-11-04T02:42:21.885606+00:00`, state=EXPANSION_AVAILABLE, snapshot_id=`mcap_snapshot_20261104_024221`, snapshot_path=`universe/mcap_snapshot_20261104_024221.json`, scanned_at=`2026-11-04T02:42:21.634264+00:00`, coverage pages_requested=20, pages_fetched=20, all_requested_pages_returned=true, entries_count=2000, lowest_rank_covered=2000, lowest_market_cap_usd=3222980, coverage_reaches_below_floor=true, universe_n=275, expansion_floor={ZKJ/USDT, $3,404,245}, eligible_unseen_below_floor_count=1 (SUKU rank 1996, mcap $3,231,609), batch_selected=["SUKU/USDT"]. Coverage re-verified: `data/fixtures/SUKU_USDT.csv` absent (`ls` exit=2, "No such file or directory"), no `SUKU` references in `results/` (grep -rl exit=1, 0 matches) — no fixtures/grid coverage, so `--apply` MUST NOT run. Baseline grid `results/20261019_135940_grid` verified complete: progress.json `run_id=20261019_135940_grid`, `all_symbols_processed=true`, `stopped=false`, `stop_reason=null`, `next_cell=null`. `results/FINAL_DECISION.md` present recording program-level rejection. `git status --short` empty, `git diff --stat` empty. No provider calls; no `--apply`; no snapshot pass; no candle fetches; no cost/fill changes. Gate remains closed; nothing actionable before `2026-11-05T02:42:21.634264+00:00`. New wakeup scheduled for this session: `wku_1a75d52c800113Uwp86obfs0Af` due `2026-11-05T02:45:00.000Z` (5 min after gate opens). Prior retained wakeup `wku_1a488323b001plz6i4dUtUGZkO` was not pending at session start (`cancel_wakeup list` returned "No pending wakeups for this session"); a fresh one-shot was scheduled at the same due time to carry the gate open.
