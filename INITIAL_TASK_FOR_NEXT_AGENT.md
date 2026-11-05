# Initial task for next agent

**Task:** Resume the EMA hourly continuation universe-refresh gate. Read `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md`, and this file before acting.

**Current state (2026-11-05T09:24:49Z, offline re-check completed):**
- Gate: `next_eligible_refresh_at=2026-11-06T03:41:37.153817+00:00` (`universe/last_scan.json`, unchanged). **NOT ELIGIBLE** at 2026-11-05T09:24:49Z (~18h17m remaining). Verified via direct JSON read and inline Python (`json.load` + `datetime.fromisoformat`): eligible=false.
- `universe/last_scan.json`: `state=AWAITING_NEW_ELIGIBLE_CANDIDATES`, `snapshot_id=mcap_snapshot_20261105_034137` (20/20 pages, 2000 entries, scanned 2026-11-05T03:41:37Z), universe_n=275, expansion floor `PIXEL/USDT $3,351,513`, `eligible_unseen_below_floor_count=0`, `batch_selected=[]`, coverage reaches below floor.
- `data/fixtures/SUKU_USDT.csv` absent; no `SUKU` references in `results/` → **`--apply` MUST NOT run** without fixture/grid coverage.
- Baseline grid `results/20261019_135940_grid` complete (`all_symbols_processed=true`, `stopped=false`, `next_cell=null`). `results/FINAL_DECISION.md` present (program-level rejection). Git clean.
- Session wakeup scheduled: `wku_1ab02a78a001XBn1CVxYTrPKZT` due `2026-11-06T03:46:56Z` (5 min after gate opens). Do not duplicate.

**What to do next:**
1. Re-verify gate eligibility from `universe/last_scan.json` against current UTC; confirm file unchanged.
2. **If not eligible:** append a concise offline re-check record to `NEXT_AGENT_TASK.md`, update this handoff if needed, and await scheduled wakeup. No provider calls.
3. **If eligible:** run at most one 20-page snapshot pass: `PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`. Recompute floor, inspect below-floor band, update `universe/last_scan.json`. Review any new candidate(s) for fixture/grid coverage **before** any `--apply`. Do NOT apply without coverage.
4. Never rerun grids, fetch candles, change EMA/cost/fill assumptions, or blur confirmatory vs exploratory. Historical research only; no orders/live/paper trading; fixtures are not market evidence; preserve negative/blocked results.

**Initial task message for next agent (copy/paste):**
> Read `README.md`, `AGENTS.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`, and `NEXT_AGENT_TASK.md`. Gate is closed until `2026-11-06T03:41:37.153817Z` (`universe/last_scan.json`). If `now < next_eligible_refresh_at`, perform an offline re-check only: verify `last_scan.json` unchanged, confirm SUKU still lacks fixture/grid coverage, append a concise record to `NEXT_AGENT_TASK.md`, and stop (await wakeup `wku_1ab02a78a001XBn1CVxYTrPKZT` 2026-11-06T03:46:56Z if present). If eligible, do exactly one 20-page snapshot pass via `scripts/fetch_mcap_snapshot.py --pages 20` (no-cost, bounded), recompute floor, record state in `last_scan.json`, and do not `--apply` any candidate without verified fixture+grid coverage. No grids, no candle fetches, no cost/fill changes, no confirmatory claims.