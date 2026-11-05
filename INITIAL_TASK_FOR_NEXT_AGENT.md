# Initial task for next agent

**Task:** Resume the EMA hourly continuation universe-refresh gate. Read `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md`, and this file before acting.

**Current state (2026-11-05T18:36:36Z, offline re-check completed):**
- Gate: `next_eligible_refresh_at=2026-11-06T03:41:37.153817+00:00` (`universe/last_scan.json`, unchanged). **NOT ELIGIBLE** (~9h05m remaining at check). Verified via direct JSON read + inline Python (`json.load` + `datetime.now(timezone.utc)`): bound `2026-11-06T03:41:37.153817+00:00`, now `2026-11-05T18:36:36Z`, eligible=false.
- `state=AWAITING_NEW_ELIGIBLE_CANDIDATES`, `snapshot_id=mcap_snapshot_20261105_034137` (scanned 2026-11-05T03:41:37Z, 20/20 pages, 2000 entries, lowest_rank=2000, lowest_mcap=$3,318,550, reaches_below_floor=true), universe_n=275.
- Expansion floor `PIXEL/USDT $3,351,513`. `eligible_unseen_below_floor_count=0`, `eligible_unseen_below_floor=[]`, `batch_selected=[]`.
- Coverage: `data/fixtures/SUKU_USDT.csv` absent; no `SUKU` references in `results/` → **`--apply` MUST NOT run** without verified fixture+grid coverage.
- Baseline grid `results/20261019_135940_grid` complete (`all_symbols_processed=true`, `stopped=false`, `next_cell=null`). `results/FINAL_DECISION.md` present (program-level rejection). `scripts/fetch_mcap_snapshot.py` and `scripts/refresh_gate.py` present.
- `git status --short` clean at check. Wakeup `wku_1ad0134f7001eSs1t8cWTD6zJv` due `2026-11-06T03:46:56Z` (5 min after gate opens). Do not re-schedule a duplicate.

**What to do next:**
1. Re-verify gate eligibility from `universe/last_scan.json` vs current UTC; confirm file unchanged.
2. **If not eligible:** append a concise offline re-check record to `NEXT_AGENT_TASK.md`, update this handoff if needed, and stop. No provider calls.
3. **If eligible:** run at most one 20-page snapshot pass: `PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`. Recompute floor, inspect below-floor band, update `universe/last_scan.json`. Review any new candidate(s) for fixture/grid coverage **before** any `--apply`. Do NOT apply without coverage.
4. Never rerun grids, fetch candles, change EMA/cost/fill assumptions, or blur confirmatory vs exploratory. Historical research only; no orders/live/paper trading; fixtures are not market evidence; preserve negative/blocked results.

**Initial task message for next agent (copy/paste):**
> Read `README.md`, `AGENTS.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`, and `NEXT_AGENT_TASK.md`. Gate is closed until `2026-11-06T03:41:37.153817Z` (`universe/last_scan.json`). If `now < next_eligible_refresh_at`, perform an offline re-check only: verify `last_scan.json` unchanged, confirm no eligible candidates below floor and no candidate has fixture+grid coverage, append a concise record to `NEXT_AGENT_TASK.md`, update `INITIAL_TASK_FOR_NEXT_AGENT.md`, and stop (check `cancel_wakeup list`; do not re-schedule a duplicate — wakeup `wku_1ad0134f7001eSs1t8cWTD6zJv` due `2026-11-06T03:46:56Z`). If eligible, do exactly one 20-page snapshot pass via `PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20` (no-cost, bounded), recompute floor, record state in `last_scan.json`, and do not `--apply` any candidate without verified fixture+grid coverage. No grids, no candle fetches, no cost/fill/EMA changes, no confirmatory claims.
