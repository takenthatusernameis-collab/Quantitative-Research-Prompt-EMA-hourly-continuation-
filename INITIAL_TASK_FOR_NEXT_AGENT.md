Resume the EMA hourly continuation universe-refresh gate.

**Read first:** `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md` (latest record: 2026-11-05T19:12:45Z).

**Current state (verified 2026-11-05T19:12:45Z):**
- Gate `next_eligible_refresh_at` = `2026-11-06T03:41:37.153817+00:00` (from `universe/last_scan.json`, JSON valid/unchanged). **NOT ELIGIBLE** (~8h29m remaining at check). Re-verified offline via direct file read + independent Python `datetime` derivation (eligible=false, remaining≈30510s).
- State `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot_id=`mcap_snapshot_20261105_034137` (scanned 2026-11-05T03:41:37Z, 20/20 pages, 2000 entries, lowest_rank_covered=2000, lowest_market_cap_usd=3318550, coverage_reaches_below_floor=true), universe_n=275, expansion_floor=`PIXEL/USDT` $3,351,513, `eligible_unseen_below_floor_count=0`, `eligible_unseen_below_floor=[]`, `batch_selected=[]`.
- Coverage: `data/fixtures/SUKU_USDT.csv` absent; no `SUKU` references in `results/` → no fixtures/grid coverage. **`--apply` MUST NOT run** without coverage.
- Baseline grid `results/20261019_135940_grid` complete (`all_symbols_processed=true`, `stopped=false`, `next_cell=null`). `results/FINAL_DECISION.md` records program-level rejection. `scripts/fetch_mcap_snapshot.py` and `scripts/refresh_gate.py` present.

**What to do:**
1. Re-verify gate eligibility at start from `universe/last_scan.json` (NOT ELIGIBLE until `2026-11-06T03:41:37.153817+00:00`).
2. If still not eligible: append an offline re-check record to `NEXT_AGENT_TASK.md` (source-of-truth file, independent derivation, state/coverage/baseline/git/wakeup status), update this handoff if materially changed, and await scheduler wakeup. **No provider calls.**
3. If eligible: run **at most one** 20-page snapshot pass (`PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`), recompute floor, inspect below-floor band, update `universe/last_scan.json`, then review any new candidate(s) for fixture/grid coverage **before any `--apply`**. Do NOT apply without coverage.
4. Never rerun grids, fetch candles, change EMA/cost/fill assumptions, or blur confirmatory vs exploratory. Preserve negative/blocked results.

**Constraints:** historical research only; no orders/live/paper trading; no fixtures as market evidence; free/public data and no-cost tooling only; follow `AGENTS.md` gate policy.

**Wakeup:** scheduled in this session for `2026-11-06T03:46:56Z` (5 min after gate opens). Do not re-schedule a duplicate; confirm pending wakeups with `cancel_wakeup`/session tools if available.
