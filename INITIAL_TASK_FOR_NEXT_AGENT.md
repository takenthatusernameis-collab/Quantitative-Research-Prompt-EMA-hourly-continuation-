# Initial task for next agent

**Task:** Resume the EMA hourly continuation universe-refresh gate. Read `README.md`, `AGENTS.md`, and `NEXT_AGENT_TASK.md` before acting.

**Current state (2026-11-05T08:23:01Z, offline re-check completed):**
- Gate `next_eligible_refresh_at` = `2026-11-06T03:41:37.153817+00:00`. **NOT ELIGIBLE** (~19h22m remaining). Verified via direct read of `universe/last_scan.json` (26 lines, JSON valid; unchanged) and inline Python: `eligible=false`, bound=`2026-11-06T03:41:37.153817+00:00`, now=`2026-11-05T08:23:01Z`, remaining≈19:18:29.
- `universe/last_scan.json` unchanged: state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261105_034137` (2000 entries, 20/20 pages, scanned 2026-11-05T03:41:37Z). Expansion floor `PIXEL/USDT` $3,351,513. `eligible_unseen_below_floor_count=0`, `batch_selected=[]`. No candidates to apply.
- SUKU has NO fixture (`data/fixtures/SUKU_USDT.csv` absent, `ls` exit=2) and NO grid coverage in `results/` (`grep -rl SUKU results/` exit=1) → `--apply` MUST NOT run without coverage.
- Baseline grid `results/20261019_135940_grid` complete (progress.json `all_symbols_processed=true`, `stopped=false`, `stop_reason=null`, `next_cell=null`); `results/FINAL_DECISION.md` records program-level rejection (23304 bytes). Git clean (`git status --short` empty, `git diff --stat` empty).
- Wakeup retained: due `2026-11-06T03:46:56Z` (5 min after gate opens). Do not re-schedule a duplicate.

**What to do:**
1. Re-verify gate eligibility: compare current UTC time against `next_eligible_refresh_at` in `universe/last_scan.json`; confirm the file is unchanged.
2. If still not eligible: append a concise offline re-check record to `NEXT_AGENT_TASK.md`, update this handoff if needed, and await the scheduler wakeup. No provider calls.
3. If eligible: run at most one 20-page snapshot pass (`PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`), recompute the floor, inspect the below-floor band, update `universe/last_scan.json`, then review any new candidate(s) for fixture/grid coverage before any `--apply`. Do NOT apply without coverage.
4. Never: rerun grids, fetch candles, change costs/fills, or blur confirmatory vs exploratory.

**Constraints:** Historical research only; no orders/live/paper trading; preserve EMA signal/fill/cost assumptions; no fixtures as market evidence; separate exploratory from confirmatory; preserve negative/blocked results; follow AGENTS.md gate policy.

**Wakeup:** due `2026-11-06T03:46:56Z` (5 min after gate opens). Do not re-schedule a duplicate.
