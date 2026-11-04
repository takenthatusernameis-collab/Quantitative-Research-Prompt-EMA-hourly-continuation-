# Initial task for next agent

Read `NEXT_AGENT_TASK.md` (tail) and `universe/last_scan.json`. Offline gate check only: next_eligible_refresh_at is `2026-11-04T01:35:03.192568+00:00`.

1. Get current UTC time (`date -u`). If now < next_eligible_refresh_at: record offline check in `NEXT_AGENT_TASK.md`, do NOT make provider calls, do NOT run `--apply`, do NOT rerun grid. Retain wakeup `wku_19fbd8c47001bdVTRQ36qHnW8N` (due 2026-11-04T01:40:00Z). Gate stays closed; nothing actionable.
2. If eligible: run at most one 20-page pass `PYTHONPATH=. timeout 900 python3 scripts/fetch_mcap_snapshot.py --pages 20`, then reconciliation per prior handoff; apply only if eligible unseen below floor and no fixture coverage conflict.
3. Update `NEXT_AGENT_TASK.md` and this file with outcome; keep git clean.
