Resume the EMA hourly continuation universe-refresh gate.

**Read first:** `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md`.

**Current state (as of 2026-11-20T00:46Z):**
- Gate `next_eligible_refresh_at` = `2026-11-21T00:22:43.099527+00:00`. NOT ELIGIBLE until then (~23h37m remaining). Verified offline via `scripts.refresh_gate.gate_status` (eligible=false) and `scripts/refresh_universe.py plan` (`refresh_allowed_now=false`) against independent UTC (`date -u` / `datetime.now(timezone.utc)`). State `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot_id=`mcap_snapshot_20261120_002243`, scanned_at=`2026-11-20T00:22:43.099527+00:00`, universe_n=279, expansion_floor=`P2P/USDT` $1,455,079, eligible_unseen_below_floor_count=0, batch_selected=["P2P/USDT"] (P2P/USDT already applied: fixture `P2P_USDT.csv` present, grid 279×66 complete).
- Baseline grid `results/20261019_135940_grid` complete (18414/18414 cells, 279 symbols × 66 pairs, all_symbols_processed=true). `results/FINAL_DECISION.md` records program-level rejection. Git tree clean.
- Env verified: pandas 3.1.1, numpy 2.5.5, pytest 9.2.0, requests 2.31.0, python 3.12.3. One gate-check row appended to `NEXT_AGENT_TASK.md` §4 this activation (nothing else: no provider call, no fixture/candle fetch, no grid rerun, no apply, no wakeup).

**What to do:**
1. Re-verify gate eligibility at start (NOT ELIGIBLE until `2026-11-21T00:22:43.099527+00:00`).
2. If still not eligible: do nothing but record the offline check in `NEXT_AGENT_TASK.md` (§4; each activation records exactly one row and nothing else), then stop. No provider calls. Repeated activations inside the same bound stay strictly offline (no provider call, no fixture/candle fetch, no grid rerun, no apply). Do not schedule wakeups (`cron_list` must stay empty).
3. If eligible: run at most one 25-page snapshot pass (`PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 25 --batch-size 10`), recompute the floor, inspect the below-floor band, update `universe/last_scan.json`, then review any new candidate(s) for fixture/grid coverage before any `--apply`. Do NOT apply without coverage.
4. Never: rerun grids, fetch candles, change costs/fills, or blur confirmatory vs exploratory.

**Constraints:** historical research only; no orders/live/paper trading; preserve EMA signal/fill/cost assumptions; no fixtures as market evidence; separate exploratory from confirmatory; preserve negative/blocked results; follow AGENTS.md gate policy.

**Wakeup:** None scheduled. Next gate eligibility at `2026-11-21T00:22:43.099527+00:00`. Do not schedule a wakeup — the next agent will run on its own schedule.
EOF
