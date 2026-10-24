# NEXT TASK — refresh bound 2026-10-25T14:30:39.449637Z (verified 2026-10-24T15:11Z, gate eligible=False, bound not yet elapsed)
## Initial task message for the next agent

Offline gate re-verified 2026-10-24T15:11:00Z: `eligible=False`, bound `2026-10-25T14:30:39.449637+00:00` not yet elapsed; no provider contact made. Nothing actionable until the bound.

The program is in `AWAITING_NEW_ELIGIBLE_CANDIDATES` after batch 29 (2026-10-24T14:30:39Z pass found 0 eligible unseen names below the floor; 2000-entry CoinGecko ranking band exhausted down to $3,363,414). Universe n=275. The 24h refresh bound expires at 2026-10-25T14:30:39.449637Z. **Do not** contact CoinGecko/KuCoin before that timestamp.

Batch 29 already ran in the prior session (2026-10-24T14:33Z): `gate_status` returned `eligible: True` (bound `2026-10-24T12:28:28.949476+00:00` had elapsed), exactly one 20-page market-cap ranking pass was run (`scripts/fetch_mcap_snapshot.py --pages 20`, pages 20/20, 429s on pages 8 and 16 recovered with backoff). Snapshot `universe/mcap_snapshot_20261024_143039.json` written and frozen for 24 h. Scan record: state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, `universe_n=275`, floor `CWEB/USDT` $3 388 825 (moved down from `BOSON/USDT` $3 558 643 as included names' market caps drifted), `eligible_unseen_below_floor_count=0`, `next_eligible_refresh_at=2026-10-25T14:30:39.449637+00:00`. Coverage reaches below the floor ($3 363 414 < $3 388 825), so the band was genuinely inspected. The 7 entries below the floor are all ineligible (7 no tradable KuCoin spot USDT pair; 0 history-probe failures). No candidates exist below the floor, so no expansion was applied and `universe/mcap_rank.json` is unchanged. Batch 29 recorded in `universe/mcap_expansion_log.md`.

Baseline grid independently re-verified this session (2026-10-24T15:11Z): 18150/18150 cells complete (275 symbols x 66 pairs), `all_symbols_processed=true`, `next_cell=null`, `stopped=false`, `stop_reason=null`, `completed_cells=18150 == n_symbols(275) x n_pairs(66)`, 0 blocked — no "blocked" substring anywhere in `progress.json`. `summary.json` pooled: n_cells 18150, n_symbols 275, n_pairs 66, total_trades 14 676 563, mean_net_pf 0.4987, median 0.5198, best_net_pf 2.2274, n_cells_net_pf_gt_1 37, n_exploratory_signal 27, n_rejected 18123, n_blocked 0, credible candidates 0. Last symbol in the working universe is ALPINE/USDT; expansion floor is CWEB/USDT $3,388,825. No provider contact was made during the offline gate re-verification before the pass; the only provider contact was the single 20-page ranking pass.

## Steps
1. **Verify eligibility offline first:**
   ```bash
   PYTHONPATH=. python3 -c "from scripts.refresh_gate import gate_status; import json; from pathlib import Path; print(gate_status(json.loads(Path('universe/last_scan.json').read_text())))"
   ```
   Must return `eligible: True`. If `False`, stop and report bound; nothing actionable.

2. **Run exactly one 20-page market-cap ranking pass:**
   ```bash
   PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 20
   ```
   Only provider contact this cycle. Freezes snapshot for 24h and writes new bound to `universe/last_scan.json`.

3. **Re-check band below current floor** for `eligible_unseen_below_floor_count`.

4. **If candidates exist:** expand per PROMPT.md §2.1 — append descending market-cap candidates (track previous→new N, log to `universe/mcap_expansion_log.md` with source/date), fetch OHLCV via `scripts/fetch_kucoin.py`, run full 66-pair EMA grid on each new symbol with `scripts/run_grid.py --resume results/20261019_135940_grid`, then `scripts/aggregate_grid.py` and `scripts/candidate_check.py`. Never create second writer on baseline grid; never promote from partial child grid.

5. **If no candidates exist:** record pass (snapshot_id, fetch time, pages, floor, exclusions) in `universe/mcap_expansion_log.md`, set `universe/last_scan.json` state to `AWAITING_NEW_ELIGIBLE_CANDIDATES`, next bound becomes +24h from new scan time.

6. **Update handoffs:** after completing (or determining no-candidates), update both `NEXT_AGENT_TASK.md` and `INITIAL_TASK_FOR_NEXT_AGENT.md` with new bound and next unprocessed symbol/pair batch (or "none").

## Next unprocessed symbol/pair batch
- None. No candidates exist; awaiting new eligible names from next 20-page pass at/after bound 2026-10-25T14:30:39.449637Z.

## Constraints
- No provider call before 2026-10-25T14:30:39.449637Z
- No second writer on `results/20261019_135940_grid`; no promotion from partial child grid
- No change to registered costs, folds, entry/exit semantics, or §3.4 gates
- Do not combine variables (`--min-risk-atr`, `--rr`, `--aggressive-exit`)
- Do not stop on failures — expand descending market cap and continue per PROMPT.md §2.1.4, §6.7
- `test_refresh_gate.py::test_the_classic_path_records_the_bound_even_when_names_are_eligible` is pre-existing clock-relative bug — do not loosen gate.
- Wakeup `wku_16dcc65f9001i6INGKlOahwLY1` at 2026-10-24T12:29:00Z executes the refresh pass; do not re-schedule a duplicate.
