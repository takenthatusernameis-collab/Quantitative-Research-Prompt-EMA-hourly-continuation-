# INITIAL TASK FOR NEXT AGENT

Read `NEXT_AGENT_TASK.md` (updated 2026-10-30T03:11:58Z) and act at/after `2026-10-30T22:20:37.246523+00:00` when wakeup fires.

Immediate action on wakeup:
1. Run offline gate check:
   ```bash
   PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"
   ```
2. Follow the exact branch in `NEXT_AGENT_TASK.md` (if not eligible -> single wakeup just after bound; if eligible -> exactly one 20-page pass, inspect below-floor band, act per rules). No provider before bound. Single wakeup only. Preserve all constraints in AGENTS.md/README.md/PROMPT.md.

Do not start exploratory pilots or modify baseline grid/costs/fills/entry-exit semantics. Keep strict confirmatory separate. Update `NEXT_AGENT_TASK.md` and this file with concrete evidence after acting.

## Evidence gathered this cycle (2026-10-30T03:11:58Z)

- Offline gate check re-run: `{'eligible': False, 'bound': '2026-10-30T22:20:37.246523+00:00', 'now': '2026-10-30T03:11:58.086393+00:00', 'reason': 'the 24 h refresh bound 2026-10-30T22:20:37.246523+00:00 has not elapsed yet'}` (~19h 9m remaining). No provider contact.
- Set single wakeup `wku_18accf43c001hEzsnHrSWBCQ05` due `2026-10-30T23:14:10Z`. No code changes.
- Working tree clean.
- Prior cycle evidence preserved: snapshot `universe/mcap_snapshot_20261029_222037.json`, `eligible_unseen_below_floor_count = 0`, state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, `next_eligible_refresh_at = 2026-10-30T22:20:37.246523+00:00`. Universe unchanged (N=275).
