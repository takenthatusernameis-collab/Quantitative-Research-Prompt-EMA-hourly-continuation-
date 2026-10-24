# NEXT TASK — refresh bound 2026-10-24T12:28:28.949476Z (verified 2026-10-24T02:05 UTC)

## Initial task message for the next agent
The program is in `AWAITING_NEW_ELIGIBLE_CANDIDATES` after batch 28 (the 2026-10-23T12:28:28Z pass found 0 eligible unseen names below the floor; the 2,000-entry CoinGecko ranking band is exhausted down to $3,441,774). The 24 h refresh bound expires at 2026-10-24T12:28:28.949476Z. Do **not** contact CoinGecko/KuCoin before that timestamp.

Offline check confirmed (2026-10-24T02:05 UTC): `eligible: False`, bound not elapsed (~10h 23m remaining). No provider contact made. Nothing is actionable until the bound expires.

A wakeup is scheduled for 2026-10-24T12:29:00Z (id `wku_16b9183ce0017UAJnQiguyUidY`) to resume the task automatically. If the harness does not resume, the next agent should run the steps below at/after the bound.

## Current offline check (2026-10-24T02:05 UTC)
`eligible: False`, bound `2026-10-24T12:28:28.949476+00:00`, now `2026-10-24T02:05:48.740829+00:00`. Reason: bound not elapsed (~10h 23m remaining). No provider contact made. State unchanged: `AWAITING_NEW_ELIGIBLE_CANDIDATES`, `universe_n=275`, `eligible_unseen_below_floor_count=0`, `batch_selected=[]`. Baseline grid verified complete (18150/18150).

## Steps
1. **Verify eligibility offline first:**
   ```bash
   PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"
   ```
   Must return `eligible: True`. If `False`, stop and report the bound; nothing is actionable yet.

2. **Run exactly one 20-page market-cap ranking pass** (only provider contact this cycle):
   ```bash
   PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20
   ```
   Freezes snapshot for 24h and writes new bound to `universe/last_scan.json`.

3. **Re-check band below current floor** (`eligible_unseen_below_floor_count`).

4. **If candidates exist:** expand per PROMPT.md §2.1 — append descending market-cap candidates (track previous→new N, rank range, log to `universe/mcap_expansion_log.md` with source/date), fetch OHLCV via `scripts/fetch_kucoin.py`, run full 66-pair EMA grid on each new symbol with `scripts/run_grid.py --resume results/20261019_135940_grid`. Never create second writer on baseline grid; never promote from partial child grid.

5. **If no candidates exist:** record pass (snapshot_id, fetch time, pages, floor, exclusions) in `universe/mcap_expansion_log.md`, set `universe/last_scan.json` state to `AWAITING_NEW_ELIGIBLE_CANDIDATES`, next bound becomes +24h from new scan time.

6. **Update handoffs:** after completing (or determining no-candidates), update both `NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with the new bound and next unprocessed symbol/pair batch (or "none").

## Constraints
- No provider call before 2026-10-24T12:28:28.949476Z
- No second writer on `results/20261019_135940_grid`; no promotion from partial child grid
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates
- Do not combine variables (`--min-risk-atr`, `--rr`, `--aggressive-exit`)
- Do not stop on failures — expand descending market cap and continue per PROMPT.md §2.1.4, §6.7
- Tests: `pytest` was **not importable** in this session (`ModuleNotFoundError: No module named 'pytest'`), so `python3 -m pytest tests/` could not be executed and the 248/249 figure was not re-verified here. Handoff notes expect pytest 9.1.1 / numpy 2.5.4 / pandas 3.1.0 installed with 248/249 pass; `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible` is a pre-existing clock-relative bug — do not loosen gate. Confirm the test environment before relying on the 248/249 figure.

(End of file)
