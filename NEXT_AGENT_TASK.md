# NEXT AGENT TASK — Durable Handoff (re-verified 2026-10-25T12:59:49Z)

## Turn 2026-10-25T12:59:49Z verification (no provider contact)
- Offline gate re-checked: `eligible=False`, bound `2026-10-25T14:30:39.449637+00:00` not yet elapsed (`now` 2026-10-25T12:59:49.473273+00:00`). Nothing actionable until the bound elapses.
- Baseline grid re-verified directly via `results/20261019_135940_grid/progress.json`: 275 symbols x 66 pairs, `all_symbols_processed=true`, `next_cell=null`, `stopped=false`, `stop_reason=null`, `completed_cells=18150`. `summary.json.pooled`: n_cells 18150, n_symbols 275, n_pairs 66, total_trades 14676563, mean net PF 0.49869497744821545, median_net_pf 0.5197980508009844, best net PF 2.227366213741068, n_cells_net_pf_gt_1 37, n_exploratory_signal 27, n_rejected 18123, n_blocked 0, **0 credible candidates**.
- Session prep (verified this turn): `git status --short` empty, `git diff --stat` empty.
- Wakeup state: no pending wakeups for this session (previous wakeup appears to have fired/resolved). If resuming at bound, ensure only one wakeup is scheduled per policy; do **not** create duplicates.
- `universe/mcap_expansion_log.md` current state unchanged by this turn (no provider contact).
- Tests: `python -m pytest tests/ -q` -> 248 passed, 1 failed — the single failure is the pre-existing clock-relative bug (`test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible`), left untouched.

## Current state
- State: `AWAITING_NEW_ELIGIBLE_CANDIDATES`
- Offline gate re-verified **2026-10-25T12:57:04.072636+00:00**:
  `{'eligible': False, 'bound': '2026-10-25T14:30:39.449637+00:00', 'now': '2026-10-25T12:57:04.072636+00:00', 'reason': 'the 24 h refresh bound 2026-10-25T14:30:39.449637+00:00 has not elapsed yet'}`.
- Nothing is actionable until the bound elapses; **no provider contact was made this turn**.
- Baseline grid re-verified directly via `results/20261019_135940_grid/progress.json`: 275x66, all processed, 0 blocked, 0 credible candidates (summary as above).
- Universe: **N = 275** symbols (BTC/USDT ... ALPINE/USDT), ranked strictly market-cap descending. `universe/mcap_rank.json` updated_at `2026-10-22T12:15:58.878331+00:00`. Last scan `universe/mcap_snapshot_20261024_143039.json` (2026-10-24T14:30:39.449637Z), floor `CWEB/USDT` 3 388 825 USD, `eligible_unseen_below_floor_count = 0`. Next bound `2026-10-25T14:30:39.449637+00:00`.

## Your task (run at/after 2026-10-25T14:30:39.449637+00:00)
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

4. **If candidates exist:** append descending market-cap names, log to `universe/mcap_expansion_log.md` (previous N -> new N, rank range, source/date), fetch OHLCV via `scripts/fetch_kucoin.py`, run the full 66-pair EMA grid per new symbol with:
   ```bash
   PYTHONPATH=. python3 scripts/run_grid.py --mcap universe/mcap_rank.json --n <NEW_TOTAL_N> --fixture-base data/fixtures --resume results/20261019_135940_grid
   ```
   (`--n` is the new total N, not the default 5; resume skips the 18150 already-completed cells.) Then `scripts/aggregate_grid.py --run results/20261019_135940_grid` and `scripts/candidate_check.py --run results/20261019_135940_grid`. Never create a second writer on the baseline grid; never promote from a partial child grid.

5. **If no candidates exist:** record the pass in `universe/mcap_expansion_log.md` (snapshot_id, fetch time, pages, floor, exclusions), set `universe/last_scan.json` state back to `AWAITING_NEW_ELIGIBLE_CANDIDATES`, and set the next bound to +24 h from the new scan time.

6. Update both `NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with the new bound and the next unprocessed symbol/pair batch (or "none").

## Next unprocessed symbol/pair batch
- None. Awaiting new eligible names from the next 20-page pass at/after the bound 2026-10-25T14:30:39.449637+00:00.

## Constraints
- No provider call before 2026-10-25T14:30:39.449637+00:00.
- No second writer on `results/20261019_135940_grid`; no promotion from a partial child grid.
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates.
- Do not combine variables (`--min-risk-atr`, `--rr`, `--aggressive-exit`).
- Do not stop the program on failures — expand descending market cap and continue per PROMPT.md §2.1.4, §6.7.
- `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible` is a pre-existing clock-relative bug — do not loosen the gate.
