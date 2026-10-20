# NEXT AGENT TASK

## Current state (verified against the saved artifacts, 2026-10-20T21:25:46Z)

**Program status: `EXPANSION_AVAILABLE`.** Batch 24 (universe N 237 -> 247) is **complete**: all 10 symbols (SATS, OGN, CETUS, YGG, DODO, ONE, AEVO, SLP, CGPT, WOO) processed - 660/660 cells complete, 0 blocked. Aggregate and OOS + 2x-cost candidate check re-run. The universe is **not** exhausted: `universe/last_scan.json` (snapshot `mcap_snapshot_20261020_113004`, fetched 2026-10-20T11:30:04Z) still holds **19 eligible unseen names below the floor** (WOO/USDT at $19 716 095).

- Universe: **N = 247**, floor **WOO/USDT** $19 716 095. Snapshot coverage reaches below floor (pages 1-10). Eligible unseen below floor: **19** (CELR, DOGS, LQTY, DIA, BIGTIME, CYBER, FIDA, CHR, QI, ARPA, ...).
- Grid: **16 302 / 16 302 cells complete** in `results/20261019_135940_grid/` (247 symbols × 66 EMA pairs); 0 blocked. `progress.json` reports `next_cell: null`, `all_symbols_processed: true`.
- Decision count: **16 276 rejected**, 26 exploratory at aggregate scan, **0 credible candidates** after OOS + 2x-cost check.
- Pooled, full-sample net of costs (10 bps taker + 2 bps slippage per side): mean net PF **0.4966**, median **0.5171**, best in-sample PF **2.2274** (BABYDOGE/USDT P50_55; rejected, zero OOS trades), ~13.24M trades.
- Cells with full-sample net PF > 1: **36 / 16 302 (0.22 %)**. All 36 failed OOS + 2x-cost checks (unchanged from batch 20). Batch 24 contributed **no survivors** (all 660 rejected; SATS cost-dominated).
- Latest candidate-check artifact: `results/20261020_211006_candidate_check/summary.md` (36 cells, 36 rejected). Gates unchanged.

**Machine-readable state:** `universe/last_scan.json` - `state=EXPANSION_AVAILABLE`, `universe_n=247`, floor `WOO/USDT`, `eligible_unseen_below_floor_count=19`, `batch_selected` will be refreshed on apply. **Do not wait 24h** - snapshot still has eligible names; fresh CoinGecko only allowed from 2026-10-21T11:30:04Z if needed.

## Required next action - apply and process batch 25

1. **Reconcile state first.** Read this handoff, `PROMPT.md` §2.1, `universe/mcap_rank.json`, `universe/last_scan.json`, `universe/mcap_snapshot_20261020_113004.json`, `universe/mcap_expansion_log.md`, grid `progress.json` and latest candidate-check artifact. Do not repeat completed scans/cells.

2. **Apply next 10 names from the saved snapshot** strictly below the floor (WOO), in descending market-cap order:
   
   | Rank in snapshot | Symbol | Name | Market cap (USD) |
   |---|---|---|---|
   | 863 | CELR/USDT | Celer Network | 19 715 136 |
   | 867 | DOGS/USDT | Dogs | 19 645 934 |
   | 881 | LQTY/USDT | Liquity | 19 254 508 |
   | 884 | DIA/USDT | DIA | 19 167 153 |
   | 888 | BIGTIME/USDT | Big Time | 19 057 587 |
   | 893 | CYBER/USDT | CYBER | 18 929 002 |
   | 918 | FIDA/USDT | Bonfida | 17 875 930 |
   | 922 | CHR/USDT | Chromia | 17 769 533 |
   | 939 | QI/USDT | BENQI | 17 229 915 |
   | 940 | ARPA/USDT | ARPA Chain | 17 212 793 |

   Apply with:
   ```bash
   PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --apply-from universe/mcap_snapshot_20261020_113004.json --batch-size 10 --apply
   ```
   Then re-run without `--apply` to refresh `last_scan.json`; confirm `universe_n` increases by 10, floor becomes ARPA/USDT, and `eligible_unseen_below_floor_count` becomes 9.

3. **Fetch and validate hourly OHLCV** for the 10 new symbols (none on disk). Use `scripts/fetch_kucoin.py` with `--target-bars 22000` and `--reconcile-manifest`. Check: no duplicates, contiguous 1h grid (no missing hours), no invalid OHLC, price identity `|log(last close / CoinGecko price)|` within tolerance. Run ticker-collision checks for short names if ambiguous. Note any cost-dominated names (report cost-to-move multiple). Record exclusions with evidence if any (transient errors -> re-query before excluding).

4. **Run full 66-pair grid for ranks N = 248..257** (one `--n` per symbol), resume from `results/20261019_135940_grid`, checkpoint after each symbol (`python scripts/remote_checkpoint.py --message "chore: grid <SYMBOL>"`). After each, run `scripts/aggregate_grid.py` and `scripts/candidate_check.py`. Update expansion log with batch 25 details and update this handoff.

5. **If snapshot band exhausted** (9 remain after batch 25) take fresh descending snapshot with `scripts/fetch_mcap_snapshot.py --pages 10 --batch-size 10` (dry run), inspect timestamped snapshot/exclusions, extend pages only if not below floor. If zero eligible, persist `AWAITING_NEW_ELIGIBLE_CANDIDATES` with evidence and next refresh >=24h out. Never force expansion or relax gates.

## Guardrails
- Append-only, market-cap descending, only below current floor.
- No stopping on negative results. 
- Never promote without OOS + 2x-cost gates.
- Keep baseline/grid unchanged unless preregistered mutation.
- Run `python -m pytest tests/ -q` after changes; report exact results.

## Environment
Use `PYTHONPATH=. python3 scripts/...` from repo root. Checkpoint durably after each symbol. ~10 min/symbol budget.

## Session update (2026-10-20T21:25:46Z)
- Applied batch 24 from saved snapshot (N 237→247). Fetched/validated 10 fixtures (ONE confirmed Harmony; SATS noted as sub-cent/cost-dominated). Completed 66-pair grid for all 10 (660 cells), re-ran aggregate and candidate check: 0 credible candidates. Updated `universe/mcap_expansion_log.md` with batch 24 section. Refreshed handoffs. Tests: 56 passed. No code changes.
