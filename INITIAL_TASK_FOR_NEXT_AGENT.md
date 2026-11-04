# INITIAL_TASK_FOR_NEXT_AGENT.md — EMA hourly continuation universe-refresh gate

**Task:** Offline gate re-check for EMA hourly continuation universe-refresh gate. Read `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md` before acting.

## Current state (as of 2026-11-04T12:22:30Z)

- Gate `next_eligible_refresh_at` = `2026-11-05T02:42:21.634264+00:00`. NOT ELIGIBLE (~14h19m remaining).
- `universe/last_scan.json` unchanged: state `EXPANSION_AVAILABLE`, snapshot `mcap_snapshot_20261104_024221`, universe_n=275, expansion_floor `ZKJ/USDT` $3,404,245, eligible_unseen_below_floor_count=1 (SUKU rank 1996, mcap $3,231,609), batch_selected=["SUKU/USDT"].
- SUKU has NO fixture (`data/fixtures/SUKU_USDT.csv` absent) and NO grid coverage in `results/` → `--apply` MUST NOT run.
- Baseline grid `results/20261019_135940_grid` complete (progress.json `all_symbols_processed=true`, `stopped=false`, `next_cell=null`). `results/FINAL_DECISION.md` present recording program-level rejection. Git tree clean.

## What to do (next agent)

1. Re-verify gate eligibility: compare current UTC time vs `next_eligible_refresh_at` in `universe/last_scan.json`.
2. If still not eligible: record offline check in `NEXT_AGENT_TASK.md` with evidence (gate status derivation, coverage checks, git state), await wakeup due `2026-11-05T02:45:00.000Z`. No provider calls.
3. If eligible: run at most one 20-page snapshot pass, recompute floor, inspect below-floor band, update `last_scan.json`, review candidate coverage before any `--apply`. Do NOT apply without coverage.
4. Never rerun grids, fetch candles, change costs/fills, or blur confirmatory vs exploratory.

## Constraints

Historical research only; no orders/live/paper trading; preserve EMA signal/fill/cost assumptions; separate exploratory from confirmatory; preserve negative/blocked results.

## Wakeup

Retained: `wku_1a685b185001GRw3WbrBvgL426` due `2026-11-05T02:45:00.000Z`. Do not re-schedule a duplicate.