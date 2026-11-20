Resume the EMA hourly continuation universe-refresh gate.

**Read first:** `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md` (§3 task, §4 gate-check log).

**Current state (verified 2026-11-20T05:32:36Z):**
- Gate `next_eligible_refresh_at` = `2026-11-21T00:22:43.099527+00:00`. NOT ELIGIBLE until then (~18h50m remaining at handoff). Verified offline via `scripts.refresh_gate.gate_status` (eligible=false) against independent UTC (`date -u`=2026-11-20T05:32:36Z).
- State `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot_id=`mcap_snapshot_20261120_002243` (scanned_at `2026-11-20T00:22:43.099527+00:00`, 25/25 pages, 2500 entries, lowest rank 2500 / $1,427,461), `universe_n=279`, expansion_floor=`P2P/USDT` $1,455,079, `eligible_unseen_below_floor_count=0`, `batch_selected=["P2P/USDT"]` — already applied (fixture `data/fixtures/P2P_USDT.csv` present).
- Universe/grid: `universe/mcap_rank.json` 279 symbols (updated_at 2026-11-20T00:29:13Z); baseline grid `results/20261019_135940_grid` complete — `completed_cells=18414`, `n_symbols=279`, `all_symbols_processed=true`, `next_cell=null`, `stopped=false` (18414 == 279×66); `data/fixtures` 282 files. `results/FINAL_DECISION.md` records program-level rejection and is preserved. Git tree clean.
- Env this session: pandas NOT importable (`refresh_universe.py plan` therefore unavailable); requests 2.31.0 present; gate tooling stdlib-only and ran fine. `pip install --user pandas numpy pytest` before any grid/signal/pytest work.
- This activation appended exactly one gate-check row to `NEXT_AGENT_TASK.md` §4 and refreshed the handoff pointers; nothing else (no provider call, no fixture/candle fetch, no grid rerun, no apply, no wakeup).

**What to do:**
1. Re-verify gate eligibility at start (NOT ELIGIBLE until `2026-11-21T00:22:43.099527+00:00`).
2. If still not eligible: do nothing but record the offline check in `NEXT_AGENT_TASK.md` §4 (each activation records exactly one row and nothing else), then stop. No provider calls. Repeated activations inside the same bound stay strictly offline (no provider call, no fixture/candle fetch, no grid rerun, no apply). Do not schedule wakeups (`cron_list` must stay empty).
3. If eligible (from `2026-11-21T00:22:43.099527+00:00`): the pass is due — run at most one 25-page snapshot pass (`PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 25 --batch-size 10`, no `--apply`), recompute the floor, inspect the below-floor band, update `universe/last_scan.json`, then review any new candidate(s) for fixture/grid coverage before any `--apply`. Do NOT apply without coverage.
4. Never: rerun grids (18414/18414 complete), fetch candles, change costs/fills, or blur confirmatory vs exploratory.

**Constraints:** historical research only; no orders/live/paper trading; preserve EMA signal/fill/cost assumptions; no fixtures as market evidence; separate exploratory from confirmatory; preserve negative/blocked results; follow AGENTS.md gate policy.

**Wakeup:** None scheduled. Next gate eligibility at `2026-11-21T00:22:43.099527+00:00`. Do not schedule a wakeup — the next agent will run on its own schedule.
