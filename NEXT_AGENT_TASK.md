# NEXT AGENT TASK — Durable Handoff

## Current state (turn 2026-10-27T14:40:36.764637+00:00 — verified by current agent)

- Gate re-checked offline at now `2026-10-27T14:40:36.764637+00:00`: `eligible=False`, reason "the 24 h refresh bound 2026-10-27T17:19:35.198212+00:00 has not elapsed yet". Bound unchanged. No provider contact (compliant). Nothing actionable before the bound (~2h 39m remaining).
- Tests: `PYTHONPATH=. python3 -m pytest tests/ -q` → 248 passed, 1 failed. The single failure is the pre-existing clock bug `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible`, to be ignored per AGENTS.md §6.
- Resume wakeup scheduled: **`wku_17dca6d07001vg5DdtgcKB14La`**, due `2026-10-27T17:26:20.611Z` (at/after the bound `2026-10-27T17:19:35.198212+00:00`). Record its id in both handoffs. Do not create a duplicate wakeup.
- Baseline grid `results/20261019_135940_grid` re-verified complete: `summary.json` `n_cells=18150` (275 symbols x 66 pairs), `n_rejected=18123`, `n_blocked=0`, `n_exploratory_signal=27`. `progress.json` `completed_cells=18150`, `all_symbols_processed=true`, `next_cell=null`, `stopped=false`, `n_symbols=275`, `n_pairs=66`.
- `universe/mcap_rank.json` holds 275 symbols, `ALPINE/USDT` last (floor), BTC/USDT first — matches `last_scan.json`.
- Mutations remain `NOT_PROMOTED` per `results/mutations.json`: `C_min_risk_atr` complete/18150 cells/delta all-zero (final NOT_PROMOTED verdict), `C_stricter_trend` complete/18150 cells/delta `None` (no-op). Baseline grid remains the program grid.
- Git clean (`git status --short` empty, `git diff --stat` empty).

## Next action (immediately at/after bound)

At/after bound `2026-10-27T17:19:35.198212+00:00`, check eligibility offline first with:

```bash
PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"
```

- If `eligible=False` → stop and report bound + reason / `next_eligible_refresh_at`.
- If `eligible=True` → run exactly one 20-page pass:
  ```bash
  PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20
  ```
  Re-check `eligible_unseen_below_floor_count` in `universe/last_scan.json`.
  - If >0 → apply with `--apply` (append below floor in desc mcap order), update `universe/mcap_rank.json`, run baseline 66-pair grid for new symbols only or full per implementation (baseline config only; no cost/fold/entry-exit/gate changes; no combining vars), then run `candidate_check`, `oos_grid_scan`, `null_grid_scan`, `survivor_selection_audit`, `cost_drag_leg`, append to `results/FINAL_DECISION.md` and `results/RESEARCH_CONCLUSION.md`.
  - If 0 → record pass in `universe/mcap_expansion_log.md` and set next +24h bound via gated refresh path.
- Update both handoffs (`NEXT_AGENT_TASK.md`, `INITIAL_TASK_FOR_NEXT_AGENT.md`). Run `PYTHONPATH=. python3 -m pytest tests/ -q`.

**Wakeup.** Exactly one resume wakeup is scheduled — **`wku_17dca6d07001vg5DdtgcKB14La`**, due `2026-10-27T17:26:20.611Z` (at/after the bound) — so the loop continues without polling; record its id in both handoffs. Do not create duplicate wakeups.

## Constraints

- No provider before bound; no second writer on grid; no partial-grid promotion.
- No changes to costs/folds/entry-exit/gates; don't combine vars; expand desc mcap only.
- Historical research only. Ignore pre-existing clock bug in `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible`.

## Key artifacts

- `results/FINAL_DECISION.md` and `results/RESEARCH_CONCLUSION.md` — program decision: no credible edge; keep expanding universe per PROMPT.md §2.1.
- `results/20261019_135940_grid/` — baseline program grid (275 symbols x 66 pairs = 18150 cells).
- `results/mutations.json` — both mutations NOT_PROMOTED.
- `universe/last_scan.json`, `universe/mcap_rank.json`, `universe/mcap_expansion_log.md`.
