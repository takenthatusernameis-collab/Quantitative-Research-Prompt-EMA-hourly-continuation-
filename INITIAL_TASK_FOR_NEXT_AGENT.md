# INITIAL TASK FOR NEXT AGENT

Run at/after 2026-10-24T12:28:28.949476Z (refresh bound). Do NOT contact the provider before that timestamp.

1. Verify eligibility offline first: `PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"` → must return `eligible: True`.
2. Run exactly one 20-page market-cap ranking pass: `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py`.
3. Freeze the new snapshot for 24 h.
4. Re-check the band below the current floor for eligible unseen candidates.
5. If candidates exist, expand the universe per PROMPT.md §2.1 (append next lower market-cap candidates, descending order; previous N → new N, rank range added, source/date in `universe/mcap_expansion_log.md`) and run the full 66-pair EMA grid on each new symbol.
6. Log the pass in `universe/mcap_expansion_log.md`.
7. Update `NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md`.

Program state: N=275, floor ALPINE/USDT $3 614 141, baseline grid `results/20261019_135940_grid` (18 150/18 150 cells, 0 blocked), null scan complete (no edge), both mutations NOT_PROMOTED, batch 28 logged (no new candidates). No provider contact before the bound.