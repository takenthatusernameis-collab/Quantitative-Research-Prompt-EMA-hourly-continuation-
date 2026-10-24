# NEXT TASK — refresh bound 2026-10-24T12:28:28.949476Z (verified 2026-10-24T03:11 UTC)

## Current status (current session)
- State: `AWAITING_NEW_ELIGIBLE_CANDIDATES`
- Offline check (2026-10-24T03:11:17Z): `eligible: False`, bound `2026-10-24T12:28:28.949476+00:00`, now `2026-10-24T03:11:17.022575+00:00`. Reason: the 24 h refresh bound has not elapsed yet (~9h 17m remaining). No provider contact made. Confirmed via `scripts.refresh_gate.gate_status(universe/last_scan.json)`.
- Wakeup scheduled: `wku_16bda2ec5001ktwBWJUOUvAufm` at 2026-10-24T12:28:29Z to resume automatically. If harness does not resume, run steps at/after bound.
- Last scan: batch 28 (2026-10-23T12:28:28Z) found 0 eligible unseen names below floor; 2000-entry CoinGecko band exhausted down to $3,441,774. Universe n=275, eligible_unseen_below_floor_count=0.

## Your task (run at/after 2026-10-24T12:28:28.949476Z)
**Do NOT** contact provider (CoinGecko/KuCoin) before that timestamp.

1. **Verify eligibility offline first:**
   ```bash
   PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"
   ```
   Must return `eligible: True`. If `False`, stop and report bound; nothing actionable yet.

2. **Run exactly one 20-page market-cap ranking pass:**
   ```bash
   PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20
   ```
   (or `scripts/refresh_universe.py fetch`). This is the only provider contact this cycle. The tool freezes snapshot for 24h and writes new bound to `universe/last_scan.json`.

3. **Re-check band below current floor** for eligible unseen candidates (`eligible_unseen_below_floor_count`).

4. **If candidates exist:** Expand per PROMPT.md §2.1 - append next lower market-cap candidates descending (track previous→new N, rank range, log to `universe/mcap_expansion_log.md` with source/date). Fetch OHLCV for each via `scripts/fetch_kucoin.py`. Run full 66-pair EMA grid on each new symbol with `scripts/run_grid.py --resume results/20261019_135940_grid`. Never create second writer on baseline grid; never promote from partial child grid.

5. **If no candidates exist:** Record pass (snapshot_id, fetch time, pages, floor, exclusions) in `universe/mcap_expansion_log.md`. Set state back to `AWAITING_NEW_ELIGIBLE_CANDIDATES` in `universe/last_scan.json`; next bound becomes +24h from new scan time.

6. **Update handoffs:** After completing (or determining no-candidates), update both `NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with the new bound and next unprocessed symbol/pair batch (or "none").

## Next unprocessed symbol/pair batch
- None. No candidates exist; awaiting new eligible names from next 20-page pass at/after bound.

## Constraints
- No provider call before 2026-10-24T12:28:28.949476Z
- No second writer on `results/20261019_135940_grid`; no promotion from partial child grid
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates
- Do not combine variables (`--min-risk-atr`, `--rr`, `--aggressive-exit`)
- Do not stop program due to failures - expand descending market cap and continue per PROMPT.md §2.1.4, §6.7
- Tests: `pytest` not importable in prior sessions; confirm test env before relying on 248/249 figure. `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible` is pre-existing clock-relative bug — do not loosen gate.
