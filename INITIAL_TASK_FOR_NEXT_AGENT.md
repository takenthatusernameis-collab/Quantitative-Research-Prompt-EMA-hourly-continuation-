# INITIAL TASK FOR NEXT AGENT

You are starting a new session on the Quantitative Research Prompt (EMA hourly continuation) project.

## Read first
- `NEXT_AGENT_TASK.md` (durable handoff; supersedes prior task descriptions)
- `PROMPT.md` (program rules, §2.1 expansion, §3.4 gates)
- `universe/mcap_expansion_log.md` (expansion history)
- `results/mutations.json` (closed mutations record)

## Current state (verified 2026-10-23T12:47 UTC)
- Program grid: `results/20261019_135940_grid` — 18 150/18 150 cells, 0 blocked, remains program grid.
- Universe: N = 275, floor `ALPINE/USDT` $3 614 141. Snapshot `universe/mcap_snapshot_20261023_122828.json`.
- Refresh bound: `2026-10-24T12:28:28.949476Z` (24 h freeze after single ranking pass at 2026-10-23T12:28:28Z). State `AWAITING_NEW_ELIGIBLE_CANDIDATES`, `eligible_unseen_below_floor_count: 0`, `batch_selected: []`.
- Null scan complete (no edge). Mutations `C_stricter_trend` and `C_min_risk_atr` closed NOT_PROMOTED.
- Tests: pytest not installed; numpy+pandas present.

## Your task (only after the bound elapses)
1. Verify eligibility offline first: `PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"`. Must return eligible: True.
2. Run exactly ONE market-cap ranking pass: `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py` (or `scripts/refresh_universe.py`), then freeze the new snapshot for 24 h.
3. Re-check the band below the current floor for new eligible candidates.
4. If candidates exist, expand the universe per PROMPT.md §2.1 (append next lower market-cap candidates, descending; log previous N -> new N, rank range added, source/date in `universe/mcap_expansion_log.md`) and run the full 66-pair EMA grid on each new symbol.
5. Update `universe/mcap_expansion_log.md`, `NEXT_AGENT_TASK.md`, and this file.

## Constraints
- No provider contact before `2026-10-24T12:28:28.949476Z`.
- Exactly one ranking pass per 24 h window.
- No second writer on `results/20261019_135940_grid`; no promotion from a partial child grid.
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates.
- Do not combine variables (`--min-risk-atr`, `--rr`, `--aggressive-exit`) in any run.

## If before the bound
Do NOT contact the provider. Verify state offline and stop cleanly. Append a completion update to `NEXT_AGENT_TASK.md`.
EOF
echo done