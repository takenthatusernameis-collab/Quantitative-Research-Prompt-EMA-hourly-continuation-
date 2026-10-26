# NEXT AGENT TASK — Durable Handoff

## Turn 2026-10-26T12:19:48Z (gate check — not yet eligible, wakeup scheduled)

- Offline gate check: `eligible=False`, bound `2026-10-26T15:14:53.192289+00:00` not yet elapsed (`now` `2026-10-26T12:19:48.346965+00:00`). Reason: `the 24 h refresh bound 2026-10-26T15:14:53.192289+00:00 has not elapsed yet`.
- No provider contact. `universe/last_scan.json` unchanged (state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261025_151453`, N=275, floor ALPINE/USDT $3,405,003, eligible count 0).
- Baseline grid `results/20261019_135940_grid/progress.json` re-verified directly: `all_symbols_processed=true`, `next_cell=null`, `stopped=false`, `stop_reason=null`, `completed_cells=18150` (275 x 66), 0 blocked.
- `git status --short` empty, `git diff --stat` empty.
- pytest unavailable in this environment (pandas not installed); no code changed, so tests unchanged. No code changes were made this cycle.

**Current state:** `AWAITING_NEW_ELIGIBLE_CANDIDATES`. Universe N=275 (BTC/USDT … ALPINE/USDT), floor ALPINE/USDT $3,405,003. Baseline grid `results/20261019_135940_grid` (275×66) is complete: 0 blocked, 0 credible candidates. Last scan `universe/mcap_snapshot_20261025_151453.json` covered 2000 entries down to rank 2000 (~$3.34M) with 0 eligible unseen names below floor. Gate bound `2026-10-26T15:14:53.192289+00:00` not yet elapsed as of `2026-10-26T12:19:48Z`. Wakeup scheduled due `2026-10-26T16:06:50Z` (id `wku_1781fc64b001Pi32d4Qnv62KEQ`, after the bound) to resume. No provider contact permitted before the bound.

**Your task, in order:**

1. **Wait for the gate.** Do NOT contact CoinGecko/KuCoin before `2026-10-26T15:14:53.192289+00:00`. Check eligibility offline first:
   ```bash
   PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"
   ```
   Must return `eligible: True`. If `False`, stop and report the bound — nothing is actionable.

2. **If eligible, run exactly one 20-page ranking pass** (the only provider contact this cycle):
   ```bash
   PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20
   ```

3. **Re-check `eligible_unseen_below_floor_count`** against the new floor.

4. **If candidates exist:** append descending market-cap names, log to `universe/mcap_expansion_log.md` (previous N → new N, rank range, source/date), fetch OHLCV via `scripts/fetch_kucoin.py`, then run the full 66-pair EMA grid per new symbol with:
   ```bash
   PYTHONPATH=. python3 scripts/run_grid.py --mcap universe/mcap_rank.json --n <NEW_TOTAL_N> --fixture-base data/fixtures --resume results/20261019_135940_grid
   ```
   (`--n` is the new total N; `--resume` skips already-completed cells.) Then:
   ```bash
   PYTHONPATH=. python3 scripts/aggregate_grid.py --run results/20261019_135940_grid
   PYTHONPATH=. python3 scripts/candidate_check.py --run results/20261019_135940_grid
   ```
   Never create a second writer on the baseline grid; never promote from a partial child grid.

5. **If no candidates exist:** record the pass in `universe/mcap_expansion_log.md` (snapshot_id, fetch time, pages, floor, exclusions), set `universe/last_scan.json` state back to `AWAITING_NEW_ELIGIBLE_CANDIDATES`, and set the next bound to +24 h from the new scan time.

6. **Update both `NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md`** with the new bound and the next unprocessed symbol/pair batch (or "none").

**Hard constraints:** no provider call before the bound; no second writer on the baseline grid; no partial-grid promotion; no changes to costs/folds/entry-exit/gates; do not combine variables; do not stop on failures — expand descending market cap and continue; ignore the pre-existing clock bug in `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible`.

**Evidence to report:** gate status before/after; snapshot path/pages/floor/N and eligible count; if expanded: old→new N, ranks, log entry; if not: log entry + new bound; grid/aggregate/candidate output paths and any blocked/credible counts; tests after changes (or confirm unchanged if none).

(End of file - total 45 lines)