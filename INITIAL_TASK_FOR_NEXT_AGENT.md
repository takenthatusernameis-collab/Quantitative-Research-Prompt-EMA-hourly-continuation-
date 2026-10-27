# Initial Task For Next Agent

Read this handoff first: `NEXT_AGENT_TASK.md` (durable state + exact next action).
Current: gate re-checked offline 2026-10-27T22:33Z; not eligible until 2026-10-28T19:29:54.929656+00:00 (~21 h remaining). Wakeup re-set for 2026-10-28T19:35:00Z (at/after bound), id `wku_17f7f8bbc001QLqYB6Y5MiSCSk`.
Universe N=275, expansion floor ALPINE/USDT $3 489 697, eligible_unseen_below_floor_count=0.
Baseline grid complete (0 credible candidates), mutations not promoted.
At/after bound: check gate offline (`PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"`); if not eligible, re-set wakeup at/after bound and stop — no provider contact; if eligible run exactly one 20-page CoinGecko pass (`PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20`), inspect band below floor, expand if eligible names exist (append + run full grid per new symbol) else record pass and set +24 h bound.
No provider before bound. One pass max/cycle. Preserve negatives. Update both handoffs on completion.