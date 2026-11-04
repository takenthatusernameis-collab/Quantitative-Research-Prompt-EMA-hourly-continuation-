Resume the EMA hourly continuation universe-refresh gate.

**Read first:** `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md`.

**Current state (as of 2026-11-04T08:33:48Z):**
- Gate `next_eligible_refresh_at` = `2026-11-05T02:42:21.634264+00:00`. NOT ELIGIBLE until then (~18h09m remaining). Verified via direct read of `universe/last_scan.json` (JSON valid, unchanged) and independent time comparison at env time `2026-11-04T08:33:48Z`. Gate status re-derived via `scripts.refresh_gate.gate_status(state)` (PYTHONPATH=.): eligible=false, bound=`2026-11-05T02:42:21.634264+00:00`, now=`2026-11-04T08:33:49.366854+00:00`, reason="the 24 h refresh bound 2026-11-05T02:42:21.634264+00:00 has not elapsed yet". State unchanged (snapshot_id=`mcap_snapshot_20261104_024221`, universe_n=275, expansion_floor ZKJ/USDT $3,404,245, eligible_unseen_below_floor_count=1 SUKU rank 1996, mcap $3,231,609). SUKU has no fixture (`data/fixtures/SUKU_USDT.csv` absent, ls exit=2) and no grid coverage in `results/` (grep -rl exit=1, 0 matches) → no fixtures/grid coverage, so `--apply` MUST NOT run. Baseline grid `results/20261019_135940_grid` complete; `results/FINAL_DECISION.md` records program-level rejection. Git tree clean (`git status --short` empty, `git diff --stat` empty).

**What to do:**
1. Re-verify gate eligibility at start (NOT ELIGIBLE until `2026-11-05T02:42:21.634264+00:00`).
2. If still not eligible: do nothing but record the offline check in `NEXT_AGENT_TASK.md`, update this handoff if needed, and await the scheduler wakeup. No provider calls.
3. If eligible: run at most one 20-page snapshot pass (`PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`), recompute the floor, inspect the below-floor band, update `universe/last_scan.json`, then review any new candidate(s) for fixture/grid coverage before any `--apply`. Do NOT apply without coverage.
4. Never: rerun grids, fetch candles, change costs/fills, or blur confirmatory vs exploratory.

**Constraints:** historical research only; no orders/live/paper trading; preserve EMA signal/fill/cost assumptions; no fixtures as market evidence; separate exploratory from confirmatory; preserve negative/blocked results; follow AGENTS.md gate policy.

**Wakeup:** `wku_1a5b579950012NwH6abkt0DK4c` due `2026-11-05T02:45:00.000Z` (5 min after gate opens). Gate closed for ~18h09m from 2026-11-04T08:33:48Z. Retained — do not re-schedule a duplicate.