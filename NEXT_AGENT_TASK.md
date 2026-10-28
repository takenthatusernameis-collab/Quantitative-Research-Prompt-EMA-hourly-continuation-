# NEXT AGENT TASK — Durable Handoff

## Current state (turn 2026-10-28T23:46Z)
- Gate checked **offline** at 2026-10-28T23:46:29Z: **eligible=False** (bound
  2026-10-29T21:24:11.948264+00:00 not yet elapsed). No provider contact made.
- Scan: 20-page pass `mcap_snapshot_20261028_212411` (2000 entries, 20/20 pages,
  history_probe_failures=0). Coverage reaches below expansion floor;
  eligible_unseen_below_floor_count=0.
- State: AWAITING_NEW_ELIGIBLE_CANDIDATES; snapshot mcap_snapshot_20261028_212411;
  batch_selected=[]; no universe expansion.
- Universe N=275; expansion floor ALPINE/USDT $3,472,967.
- next_eligible_refresh_at 2026-10-29T21:24:11.948264+00:00.
- Wakeup: **wku_184e9e49e001vu9KPDPuESUm1x**, due 2026-10-29T21:25:00Z (after the bound).
  Previous wku_184e8fe03001u6X9gat5VPBPnO was gone on arrival; this is
  the single resume wakeup. Do **not** re-schedule a duplicate.

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