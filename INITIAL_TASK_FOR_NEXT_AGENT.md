# Initial task message for the next agent

**Task:** Resume the EMA hourly continuation universe-refresh gate. Read `README.md`, `AGENTS.md`, and `NEXT_AGENT_TASK.md` before acting.

## Current state (as of 2026-11-05T06:16:27Z)
- Gate `next_eligible_refresh_at` = `2026-11-06T03:41:37.153817+00:00`. NOT ELIGIBLE (~21h25m remaining). Verified via direct read of `universe/last_scan.json` (26 lines, JSON valid; unchanged vs prior record) and independent inline Python (`json.load` + `datetime.fromisoformat`): eligible=false, bound=`2026-11-06T03:41:37.153817+00:00`, now=`2026-11-05T06:13:36.096444+00:00`, remaining=21:28:01.057373.
- `universe/last_scan.json` unchanged: state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261105_034137` (2000 entries, 20/20 pages, fetched 2026-11-05T03:41:37). Expansion floor `PIXEL/USDT` $3,351,513. Eligible unseen below floor: 0, batch_selected: []. No candidates to apply.
- No eligible candidates remain; prior SUKU candidate (from snapshot `mcap_snapshot_20261104_024221`) superseded. SUKU has NO fixture (`data/fixtures/SUKU_USDT.csv` absent) and NO grid coverage in `results/` (no matches) → `--apply` MUST NOT run without coverage.
- Baseline grid `results/20261019_135940_grid` verified complete (progress.json present, `all_symbols_processed=true`, `stopped=false`, `stop_reason=null`, `next_cell=null`); `results/FINAL_DECISION.md` records program-level rejection. `scripts/fetch_mcap_snapshot.py` and `scripts/refresh_gate.py` present. Git tree clean.
- Wakeup retained for this session: `wku_1aa33bb0b001x1MROZ0W65t6xA` due `2026-11-06T03:46:56Z` (5 min after gate opens). Do not re-schedule a duplicate.

## What to do
1. Re-verify gate eligibility: compare current UTC time against `next_eligible_refresh_at` in `universe/last_scan.json`; confirm the file is unchanged.
2. If still not eligible: record the offline check in `NEXT_AGENT_TASK.md`, update this handoff if needed, and await the scheduler wakeup. No provider calls.
3. If eligible: run at most one 20-page snapshot pass (`PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`), recompute the floor, inspect the below-floor band, update `universe/last_scan.json`, then review any new candidate(s) for fixture/grid coverage before any `--apply`. Do NOT apply without coverage.
4. Never: rerun grids, fetch candles, change costs/fills, or blur confirmatory vs exploratory.

## Constraints
Historical research only; no orders/live/paper trading; preserve EMA signal/fill/cost assumptions; no fixtures as market evidence; separate exploratory from confirmatory; preserve negative/blocked results; follow AGENTS.md gate policy.

## Wakeup
Due `2026-11-06T03:46:56Z` (5 min after gate opens). Do not re-schedule a duplicate.
