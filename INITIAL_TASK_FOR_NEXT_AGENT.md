# INITIAL TASK FOR NEXT AGENT

## Context (from durable handoff)
- Repo: Quantitative-Research-Prompt-EMA-hourly-continuation-
- Current turn: 2026-10-29T14:12:40Z
- Gate (offline): `{'eligible': False, 'bound': '2026-10-29T21:24:11.948264+00:00', 'now': '2026-10-29T14:13:08.140143+00:00', 'reason': 'the 24 h refresh bound 2026-10-29T21:24:11.948264+00:00 has not elapsed yet'}` (~7h 11m remaining)
- State: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261028_212411`, universe N=275, floor `ALPINE/USDT` $3,472,967, `eligible_unseen_below_floor_count: 0`, `batch_selected: []`, `next_eligible_refresh_at: 2026-10-29T21:24:11.948264+00:00`
- Baseline grid `results/20261019_135940_grid`: complete (18150/18150), 0 credible candidates, pooled mean net PF 0.49869497744821545
- Child mutation grid `results/20261022_134500_grid`: complete, `C_min_risk_atr` not applied; child == parent; NOT_PROMOTED
- Tests: 248 passed, 1 failed (pre-existing clock bug in `tests/test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible` — not a regression)
- Wakeup: resume wakeup set for 2026-10-29T21:27:15Z (cross-session, not visible here). Do **not** create a second one; let it fire.
- Working tree clean.

## Task (do this next)
At/after `2026-10-29T21:24:11.948264+00:00`:

1. **Check gate offline first** (no provider before bound):
   ```bash
   PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"
   ```
   If not eligible: stop (no provider), re-set wakeup per 24h policy and update both `NEXT_AGENT_TASK.md` and this file with evidence.

2. **If eligible, run exactly one 20-page pass**:
   ```bash
   PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20
   ```

3. **Recompute expansion floor** from the fresh snapshot; inspect the band strictly below the floor.

4. **If `eligible_unseen_below_floor_count == 0`**: record the pass (snapshot_id/counts), set `next_eligible_refresh_at` (24h from bound/now as per policy), re-set wakeup, stop (no expand). Update both handoffs.

5. **If `eligible_unseen_below_floor_count > 0`**: expand per `PROMPT.md §2.1`, run full 66-pair grid on each new symbol via `scripts/run_grid.py` (or tested resume path), re-aggregate. Update both handoffs with evidence (snapshot_id, counts, results paths) and preserve all negative/blocked results.

## Constraints
- Historical research only. Never place orders/deploy live/paper trading.
- One 20-page pass max per cycle. Do not hit provider on every activation.
- Do not trigger/cancel/rerun GitHub Actions or edit workflows.
- Do not fetch new candle data. Do not modify baseline grid/costs/fills/entry-exit semantics.
- Preserve all negative and blocked results. Negative batch is not a stop; expand if eligible unseen below floor exist.
- Do not create a second wakeup if one is already scheduled (cross-session) — let it fire.
