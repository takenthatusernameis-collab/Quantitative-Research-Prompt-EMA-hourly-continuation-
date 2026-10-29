# INITIAL TASK FOR NEXT AGENT

Read `NEXT_AGENT_TASK.md` (updated 2026-10-29T19:25:29Z) and act at/after `2026-10-29T21:25:00.000Z` when wakeup `wku_189235b3c0015sTzA3PV9Nm171` fires (due 2026-10-29T21:25:00.000Z).

Immediate action on wakeup:
1. Run offline gate check:
```bash
PYTHONPATH=. python3 -c "import json; from scripts.refresh_gate import gate_status; print(gate_status(json.load(open('universe/last_scan.json'))))"
```
2. Follow the exact branch in `NEXT_AGENT_TASK.md` (if not eligible -> single wakeup just after bound; if eligible -> exactly one 20-page pass, inspect below-floor band, act per rules). No provider before bound. Single wakeup only. Preserve all constraints in AGENTS.md/README.md/PROMPT.md.

Do not start exploratory pilots or modify baseline grid/costs/fills/entry-exit semantics. Keep strict confirmatory separate. Update `NEXT_AGENT_TASK.md` and this file with concrete evidence after acting.
