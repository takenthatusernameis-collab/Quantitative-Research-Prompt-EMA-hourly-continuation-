# NEXT AGENT TASK — Durable Handoff

## Current state (turn 2026-10-29T02:27Z)
- Gate re-checked offline at 2026-10-29T02:27:17Z: eligible=False (bound 2026-10-29T21:24:11.948264+00:00 not yet elapsed; ~18h 57m remaining). No provider contact made. Confirmed via `scripts/refresh_gate.gate_status(universe/last_scan.json)`.
- Resume wakeup **wku_1857e32c2001AzJRtWvOiY3SLA** due 2026-10-29T21:26:21Z (re-created this cycle). The prior recorded id wku_185763f99001qNvgczbfetweZe was not present in this session's pending-wakeup list; a new wakeup was created at the same due time. Do NOT create a second one — the bound is the same and only one pass is allowed per 24 h.
- Scan: 20-page pass mcap_snapshot_20261028_212411 (2000 entries, 20/20 pages, history_probe_failures=0). eligible_unseen_below_floor_count=0.
- State: AWAITING_NEW_ELIGIBLE_CANDIDATES; snapshot mcap_snapshot_20261028_212411; batch_selected=[]; no universe expansion.
- Universe N=275; expansion floor ALPINE/USDT $3,472,967 (last_scan.json) / $3,614,141 (mcap_rank.json, from the 2026-10-22 expansion snapshot). The floor used by the gate is the one recomputed by `fetch_mcap_snapshot.py` from the fresh snapshot at pass time — do not assume either value is authoritative without recomputing.
- next_eligible_refresh_at 2026-10-29T21:24:11.948264+00:00.
- Baseline grid results/20261019_135940_grid verified: n_cells 18150, n_symbols 275, n_pairs 66, mean net PF 0.4987; complete, 0 blocked, 0 credible candidates.

## Next action at/after bound

At/after 2026-10-29T21:24:11.948264+00:00:
1. Check gate offline. If not eligible, re-set wakeup and stop.
2. If eligible: run exactly one 20-page pass `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`.
3. Recompute floor; inspect band strictly below floor.
4. If count==0: record pass, set next bound, re-set wakeup, stop.
5. If count>0: expand per PROMPT.md §2.1, run full 66-pair grid on each new symbol.
6. Update both handoffs.

## Constraints
- No provider before bound; historical research only.
- One 20-page pass max per cycle.
- Do not trigger/cancel/rerun/dispatch GitHub Actions.
- Do not fetch new candle data; do not modify baseline grid or costs/fills/entry-exit.
- Preserve all negative/blocked results.