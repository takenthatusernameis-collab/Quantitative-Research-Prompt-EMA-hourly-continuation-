# NEXT AGENT TASK — Durable Handoff

## Turn 2026-10-26T13:55Z (gate check — not yet eligible, no provider contact)

- Offline gate check (run at `2026-10-26T13:55:16.753133+00:00`): `eligible=False`, bound `2026-10-26T15:14:53.192289+00:00` not yet elapsed. Reason: `the 24 h refresh bound 2026-10-26T15:14:53.192289+00:00 has not elapsed yet`.
- No provider contact. `universe/last_scan.json` unchanged (state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261025_151453`, N=275, floor ALPINE/USDT $3,405,003, eligible count 0).
- Baseline grid `results/20261019_135940_grid` re-verified: complete (0 blocked/credible).
- `git status --short` empty, `git diff --stat` empty.
- Wakeup `wku_1787ece36001DkbrTFmJjvWasN` scheduled due `2026-10-26T15:15:38.675Z` (after the bound) to resume gate workflow.

**Current state:** `AWAITING_NEW_ELIGIBLE_CANDIDATES`. Universe N=275, baseline grid complete (0 blocked/credible). Gate bound `2026-10-26T15:14:53.192289+00:00` not yet elapsed. No provider contact permitted before the bound. Next action is to wait for the wakeup/gate eligibility and follow steps: if eligible, run one 20-page ranking pass (`scripts/fetch_mcap_snapshot.py --pages 20`), re-check eligible candidates, expand or record the pass and set the next +24 h bound, then update both handoff files.

# NEXT AGENT TASK — Durable Handoff

## Turn 2026-10-26T13:28Z (gate check — not yet eligible, no provider contact)

- Offline gate check (run at `2026-10-26T13:28:34.210876+00:00`): `eligible=False`, bound `2026-10-26T15:14:53.192289+00:00` not yet elapsed. Reason: `the 24 h refresh bound 2026-10-26T15:14:53.192289+00:00 has not elapsed yet`.
- No provider contact. `universe/last_scan.json` unchanged (state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261025_151453`, N=275, floor ALPINE/USDT $3,405,003, eligible count 0).
- Baseline grid `results/20261019_135940_grid` re-verified: complete (0 blocked/credible).
- `git status --short` empty, `git diff --stat` empty.
- Wakeup `wku_178663416001JgXu3X7JSPXo7f` scheduled due `2026-10-26T15:16:00.000Z` (after the bound) to resume gate workflow.
- Nothing actionable until bound; next symbol/pair batch: none.

**Current state:** `AWAITING_NEW_ELIGIBLE_CANDIDATES`. Universe N=275, baseline grid complete (0 blocked/credible). Gate bound `2026-10-26T15:14:53.192289+00:00` not yet elapsed. No provider contact permitted before the bound. Next action is to wait for the wakeup/gate eligibility and follow steps below: if eligible, run one 20-page ranking pass (`scripts/fetch_mcap_snapshot.py --pages 20`), re-check eligible candidates, expand or record the pass and set the next +24 h bound, then update both handoff files.

## Turn 2026-10-26T13:08Z (gate check — not yet eligible, no provider contact)

- Offline gate check (run at `2026-10-26T13:08:25.202877+00:00`): `eligible=False`, bound `2026-10-26T15:14:53.192289+00:00` not yet elapsed. Reason: `the 24 h refresh bound 2026-10-26T15:14:53.192289+00:00 has not elapsed yet`.
- No provider contact. `universe/last_scan.json` unchanged (state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261025_151453`, N=275, floor ALPINE/USDT $3,405,003, eligible count 0).
- Baseline grid `results/20261019_135940_grid` re-verified: complete (0 blocked/credible).
- `git status --short` empty, `git diff --stat` empty.
- Wakeup `wku_17848df130018Q0pT9WhiHdpXD` scheduled due `2026-10-26T15:16:00.000Z` (after the bound) to resume.

**Current state:** `AWAITING_NEW_ELIGIBLE_CANDIDATES`. Universe N=275, baseline grid complete (0 blocked/credible). Gate bound `2026-10-26T15:14:53.192289+00:00` not yet elapsed. No provider contact permitted before the bound. Next action is to wait for the wakeup/gate eligibility and follow steps below: if eligible, run one 20-page ranking pass (`scripts/fetch_mcap_snapshot.py --pages 20`), re-check eligible candidates, expand or record the pass and set the next +24 h bound, then update both handoff files.

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

## Turn 2026-10-26T13:12Z (gate check — not yet eligible, no provider contact)

- Offline gate check (run at `2026-10-26T13:12:24.475896+00:00`): `eligible=False`, bound `2026-10-26T15:14:53.192289+00:00` not yet elapsed.
- No provider contact. `universe/last_scan.json` unchanged.
- Wakeup `wku_178575688001zYiJxS9bWe6tv6` scheduled due `2026-10-26T15:16:32.132Z` to resume gate workflow.
- Nothing actionable until bound; next symbol/pair batch: none.

**Current state:** unchanged `AWAITING_NEW_ELIGIBLE_CANDIDATES`. Next action: wait for bound, then follow steps in prior turn.

## Turn 2026-10-26T13:18Z (gate check — not yet eligible, no provider contact)

- Offline gate check (run at `2026-10-26T13:18:20.779067+00:00`): `eligible=False`, bound `2026-10-26T15:14:53.192289+00:00` not yet elapsed. Reason: `the 24 h refresh bound 2026-10-26T15:14:53.192289+00:00 has not elapsed yet`.
- No provider contact. `universe/last_scan.json` unchanged (state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, snapshot `mcap_snapshot_20261025_151453`, N=275, floor ALPINE/USDT $3,405,003, eligible count 0).
- Baseline grid `results/20261019_135940_grid` re-verified: complete (0 blocked/credible).
- `git status --short` empty, `git diff --stat` empty.
- Wakeup `wku_1785cd6b8001jVm5vDixJ8C76J` scheduled due `2026-10-26T15:14:32.628Z` (after the bound) to resume gate workflow.

**Current state:** `AWAITING_NEW_ELIGIBLE_CANDIDATES`. Universe N=275, baseline grid complete (0 blocked/credible). Gate bound `2026-10-26T15:14:53.192289+00:00` not yet elapsed. No provider contact permitted before the bound. Next action is to wait for the wakeup/gate eligibility and follow steps in prior turn.

(End of file)
">">
