# NEXT AGENT TASK — Durable Handoff (updated 2026-10-24T05:10 UTC)

## Current state
- State: `AWAITING_NEW_ELIGIBLE_CANDIDATES`
- Universe: **N = 275** symbols (BTC/USDT ... ALPINE/USDT), ranked strictly market-cap descending, append-only.
- Baseline grid: `results/20261019_135940_grid` — **18 150/18 150 cells complete** (275 × 66 EMA pairs), `all_symbols_processed=true`, `next_cell=null`, `stopped=false`, 0 blocked (verified: `progress.json.completed` list length 18150, no blocked markers). Pooled mean net PF 0.4987, 37 cells net PF > 1, all fail OOS + 2x-cost stress. **0 credible candidates.**
- Last scan: batch 28, `universe/mcap_snapshot_20261023_122828.json` (2026-10-23T12:28:28.949476Z, 20/20 pages, 2 000 entries, lowest covered $3 441 774). Floor `BOSON/USDT` $3 558 643. `eligible_unseen_below_floor_count = 0`.
- Refresh bound: **2026-10-24T12:28:28.949476Z**.
- **This session (2026-10-24T05:14:14Z): verified the gate offline** — `gate_status` returned `eligible: False`, bound `2026-10-24T12:28:28.949476+00:00`, now `2026-10-24T05:14:14+00:00`, reason "the 24 h refresh bound ... has not elapsed yet" (~7h 14m remaining). **No provider contact made.** Nothing is actionable until the bound elapses.
- A wakeup is scheduled for 2026-10-24T12:29:00Z (id `wku_16c5187d0001F7XRWQEhtcsvUh`) to resume automatically. If the harness does not resume, run the steps below at/after the bound.

## Your task (run at/after 2026-10-24T12:28:28.949476Z)
**Do NOT** contact CoinGecko/KuCoin before that timestamp.

1. Verify eligibility offline:
   ```bash
   PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"
   ```
   Must return `eligible: True`. If `False`, stop and report the bound — nothing is actionable.

2. Run exactly one 20-page ranking pass (the only provider contact this cycle):
   ```bash
   PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20
   ```

3. Re-check `eligible_unseen_below_floor_count` against the new floor.

4. **If candidates exist:** append descending market-cap names, log to `universe/mcap_expansion_log.md` (previous N → new N, rank range, source/date), fetch OHLCV via `scripts/fetch_kucoin.py`, run the full 66-pair EMA grid per new symbol with `scripts/run_grid.py --resume results/20261019_135940_grid`, then `scripts/aggregate_grid.py`. Never create a second writer on the baseline grid; never promote from a partial child grid.

5. **If no candidates exist:** record the pass in `universe/mcap_expansion_log.md` (snapshot_id, fetch time, pages, floor, exclusions), set `universe/last_scan.json` state back to `AWAITING_NEW_ELIGIBLE_CANDIDATES`, and set the next bound to +24 h from the new scan time.

6. Update both `NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with the new bound and the next unprocessed symbol/pair batch (or "none").

## Next unprocessed symbol/pair batch
- None. Awaiting new eligible names from the next 20-page pass at/after the bound.

## Constraints
- No provider call before 2026-10-24T12:28:28.949476Z.
- No second writer on `results/20261019_135940_grid`; no promotion from a partial child grid.
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates.
- Do not combine variables (`--min-risk-atr`, `--rr`, `--aggressive-exit`).
- Do not stop the program on failures — expand descending market cap and continue per PROMPT.md §2.1.4, §6.7.
- `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible` is a pre-existing clock-relative bug — do not loosen the gate.

(End of file - total 45 lines)