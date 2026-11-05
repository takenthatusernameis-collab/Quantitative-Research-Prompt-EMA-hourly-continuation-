Resume the EMA hourly continuation universe-refresh gate.

**Read first:** `README.md`, `AGENTS.md`, `NEXT_AGENT_TASK.md`.

**Current state (as of 2026-11-05T04:33:36Z):**
- Gate `next_eligible_refresh_at` = `2026-11-06T03:41:37.153817+00:00`. NOT ELIGIBLE until then (~23h08m remaining). Verified via direct read of `universe/last_scan.json` (26 lines, JSON valid; unchanged) and independent inline-Python time comparison. State `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261105_034137` (2000 entries, 20/20 pages, fetched 2026-11-05T03:41:37). Expansion floor `PIXEL/USDT` $3,351,513. Eligible unseen below floor: 0, batch_selected: []. No candidates to apply.
- SUKU still has NO fixture (`data/fixtures/SUKU_USDT.csv` absent) and NO grid coverage in `results/` → `--apply` must NOT run without coverage (currently no candidates anyway).
- Baseline grid `results/20261019_135940_grid` complete (n_cells=18150, n_symbols=275, n_rejected=18123, n_exploratory_signal=27, n_blocked=0); `results/FINAL_DECISION.md` records program-level rejection. Git tree clean (`git status --short` empty, `git diff --stat` empty). No modified or untracked files.
- Wakeup re-scheduled due `2026-11-06T03:47:00Z` (5 min after gate opens) — prior retained wakeup was stale/gone (`cancel_wakeup list` returned none), so a new one was created. Do not re-schedule a duplicate.

**What to do:**
1. Re-verify gate eligibility: compare current UTC time against `next_eligible_refresh_at` in `universe/last_scan.json`; confirm the file is unchanged.
2. If still not eligible: record the offline check in `NEXT_AGENT_TASK.md`, update this handoff if needed, and await the scheduler wakeup. No provider calls.
3. If eligible: run at most one 20-page snapshot pass (`PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`), recompute the floor, inspect the below-floor band, update `universe/last_scan.json`, then review any new candidate(s) for fixture/grid coverage before any `--apply`. Do NOT apply without coverage.
4. Never: rerun grids, fetch candles, change costs/fills, or blur confirmatory vs exploratory.

**Constraints:** Historical research only; no orders/live/paper trading; preserve EMA signal/fill/cost assumptions; no fixtures as market evidence; separate exploratory from confirmatory; preserve negative/blocked results; follow AGENTS.md gate policy.

**Wakeup:** due `2026-11-06T03:47:00Z`. Do not re-schedule a duplicate.