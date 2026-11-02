## Initial task for next agent (handoff from this run)

Read `NEXT_AGENT_TASK.md` (current state + cycle log). Do the following:

1. Offline gate check first (compare now >= next_eligible_refresh_at; verify `universe/last_scan.json` unchanged). Use `scripts/refresh_gate.py` logic / the same check.
2. If NOT eligible: record the offline gate check in `NEXT_AGENT_TASK.md` cycle log (append with timestamp/now/bound/remaining), leave `universe/last_scan.json` unchanged, do NOT call provider, do NOT run snapshot pass, do NOT apply batch, do NOT rerun grids/candles/cost changes. Retain existing wakeup `wku_19a3b4ecd001zC5zMG7tiKdXff` due 2026-11-03T00:56:00Z if present (do not duplicate). Update handoff and stop.
3. If eligible and scan shows expansion available: run at most one 20-page pass (`PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`), recompute floor, inspect below-floor band, update `universe/last_scan.json`. Do NOT apply any batch without fixtures/grid coverage. No grid reruns/candle fetches/cost/fill changes. Keep strict confirmatory separate from exploratory.
4. Preserve all constraints in `AGENTS.md`/`README.md` (historical research only; no orders; preserve EMA/fill/cost assumptions; no fixtures as market evidence; separate exploratory from confirmatory; preserve negatives/blocked; follow gate policy).

Current known state: gate bound 2026-11-03T00:55:58.735958+00:00, snapshot `mcap_snapshot_20261102_005558`, universe N=275, eligible_unseen_below_floor_count=0, batch_selected=[] not applied. Wakeup `wku_19a3b4ecd001zC5zMG7tiKdXff` due 2026-11-03T00:56:00Z.
