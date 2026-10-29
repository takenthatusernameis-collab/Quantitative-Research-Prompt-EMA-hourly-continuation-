# INITIAL TASK FOR NEXT AGENT

Read `NEXT_AGENT_TASK.md` (updated 2026-10-29T23:11Z) and act at/after `2026-10-30T22:20:37.246523+00:00` when wakeup `wku_189eec1b7001oCXFbK3MWZhOae` fires (due 2026-10-30T22:21:00Z). If no wakeup exists, re-set a single wakeup just after the bound.

Immediate action on wakeup:
1. Run offline gate check:
   ```bash
   PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"
   ```
2. Follow the exact branch in `NEXT_AGENT_TASK.md` (if not eligible -> single wakeup just after bound; if eligible -> exactly one 20-page pass, inspect below-floor band, act per rules). No provider before bound. Single wakeup only. Preserve all constraints in AGENTS.md/README.md/PROMPT.md.

Do not start exploratory pilots or modify baseline grid/costs/fills/entry-exit semantics. Keep strict confirmatory separate. Update `NEXT_AGENT_TASK.md` and this file with concrete evidence after acting.

## Evidence gathered this cycle (2026-10-29T22:43Z)

- Read prior durable handoff, gate/status, `README.md`, `AGENTS.md`. Confirmed bound not elapsed (`2026-10-30T22:20:37.246523+00:00`); gate not eligible yet (state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, `next_eligible_refresh_at` set). Live check: `{'eligible': False, 'bound': '2026-10-30T22:20:37.246523+00:00', 'now': '2026-10-29T22:43:45.961498+00:00', 'reason': 'the 24 h refresh bound ... has not elapsed yet'}`
- Prior wakeup expired; re-set single wakeup `wku_189eec1b7001oCXFbK3MWZhOae` due `2026-10-30T22:21:00Z`. No provider calls. No code changes.
- Prior cycle evidence preserved: snapshot `universe/mcap_snapshot_20261029_222037.json` created, `eligible_unseen_below_floor_count = 0`, universe unchanged (N=275).
