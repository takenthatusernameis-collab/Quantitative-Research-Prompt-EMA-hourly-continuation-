# Initial Task for Next Agent

Resume the EMA hourly continuation universe-refresh gate.

**Read first:** `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md`.

**Current state (as of 2026-11-04T22:25:36Z):**
- Gate `next_eligible_refresh_at` = `2026-11-05T02:42:21.634264+00:00`. NOT ELIGIBLE until then (~4h17m remaining). Verified via direct read of `universe/last_scan.json` (JSON valid, unchanged) and independent time comparison. Gate status: eligible=false.
- State `EXPANSION_AVAILABLE`, snapshot `mcap_snapshot_20261104_024221`, universe_n=275, expansion_floor=`ZKJ/USDT` $3,404,245, eligible_unseen_below_floor_count=1 (SUKU rank 1996, mcap $3,231,609), batch_selected=["SUKU/USDT"].
- SUKU has NO fixture (`data/fixtures/SUKU_USDT.csv` absent) and NO references in `results/` → no fixtures/grid coverage, so `--apply` MUST NOT run.
- Baseline grid `results/20261019_135940_grid` complete; `results/FINAL_DECISION.md` records program-level rejection. Git tree clean.
- Wakeup scheduled: due `2026-11-05T02:45:00.000Z` (5 min after gate opens). Do not re-schedule a duplicate.

**What to do:**
1. Re-verify gate eligibility at start (read `universe/last_scan.json`, compare with current UTC time).
2. If still not eligible: record offline check in `NEXT_AGENT_TASK.md`. Confirm a wakeup exists for `2026-11-05T02:45:00.000Z`; if none, schedule one. Do not re-schedule duplicates.
3. If eligible: run at most one 20-page snapshot pass (`PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`), recompute floor, inspect below-floor band, update `universe/last_scan.json`, then review new candidate(s) for fixture/grid coverage before any `--apply`. Do NOT apply without coverage.
4. Never: rerun grids, fetch candles, change costs/fills, or blur confirmatory vs exploratory.

**Constraints:** historical research only; no orders/live/paper trading; preserve EMA signal/fill/cost assumptions; no fixtures as market evidence; separate exploratory from confirmatory; preserve negative/blocked results; follow AGENTS.md gate policy.
EOF
echo done
