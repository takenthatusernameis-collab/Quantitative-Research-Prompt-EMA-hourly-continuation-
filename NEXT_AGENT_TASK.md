# NEXT AGENT TASK

## Current state (verified against the saved artifacts, 2026-10-20T22:30:00Z)

**Program status: `EXPANSION_AVAILABLE`.** Batch 25 (universe N 247 -> 257) is **complete**: all 10 symbols (CELR, DOGS, LQTY, DIA, BIGTIME, CYBER, FIDA, CHR, QI, ARPA) processed - 660/660 cells complete, 0 blocked. Aggregate and OOS + 2x-cost candidate check re-run. The universe is **not** exhausted: `universe/last_scan.json` (snapshot `mcap_snapshot_20261020_113004`, fetched 2026-10-20T11:30:04Z) still holds **9 eligible unseen names below the floor** (POKT/USDT at $17 067 402).

- Universe: **N = 257**, floor **ARPA/USDT** $17 223 422. Snapshot coverage reaches below floor (pages 1-10). Eligible unseen below floor: **9** (POKT, XAI, ANYONE, ACE, MOVR, RIO, BICO, AGLD, TAIKO).
- Grid: **16 962 / 16 962 cells complete** in `results/20261019_135940_grid/` (257 symbols × 66 EMA pairs); 0 blocked. `progress.json` reports `next_cell: null`, `all_symbols_processed: true`.
- Decision count: **16 936 rejected**, 26 exploratory at aggregate scan, **0 credible candidates** after OOS + 2x-cost check.
- Pooled, full-sample net of costs (10 bps taker + 2 bps slippage per side): mean net PF **0.4979**, median **0.5188**, best in-sample PF **2.2274** (BABYDOGE/USDT P50_55; rejected, zero OOS trades), ~13.24M+ trades.
- Cells with full-sample net PF > 1: **36 / 16 962 (0.2%)**. All 36 failed OOS + 2x-cost checks (unchanged from batch 20). Batch 25 contributed **no survivors** (all 660 rejected; BIGTIME best cell 0.9130).
- Latest candidate-check artifact: `results/20261020_223841_candidate_check/summary.md` (36 cells, 36 rejected). Gates unchanged.

**Machine-readable state:** `universe/last_scan.json` - `state=EXPANSION_AVAILABLE`, `universe_n=257`, floor `ARPA/USDT`, `eligible_unseen_below_floor_count=9`, `batch_selected` will be refreshed on apply. **Do not wait 24h** - snapshot still has eligible names; fresh CoinGecko only allowed from 2026-10-21T11:30:04Z if needed.

## Required next action - apply and process batch 26

1. **Reconcile state first.** Read this handoff, `PROMPT.md` §2.1, `universe/mcap_rank.json`, `universe/last_scan.json`, `universe/mcap_snapshot_20261020_113004.json`, `universe/mcap_expansion_log.md`, grid `progress.json` and latest candidate-check artifact. Do not repeat completed scans/cells.

2. **Apply next names from the saved snapshot** strictly below the floor (ARPA), in descending market-cap order:

   | Rank in snapshot | Symbol | Name | Market cap (USD) |
   |---|---|---|---|
   | 944 | POKT/USDT | Pocket Network | 17 067 402 |
   | 945 | XAI/USDT | Xai | 17 056 252 |
   | 947 | ANYONE/USDT | ANyONe Protocol | 16 944 562 |
   | 955 | ACE/USDT | Fusionist | 16 766 208 |
   | 961 | MOVR/USDT | Moonriver | 16 632 333 |
   | 964 | RIO/USDT | Realio Network Token | 16 469 905 |
   | 976 | BICO/USDT | Biconomy | 16 006 036 |
   | 982 | AGLD/USDT | Adventure Gold | 15 735 984 |
   | 992 | TAIKO/USDT | Taiko | 15 436 339 |

   Apply with:
   ```bash
   PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --apply-from universe/mcap_snapshot_20261020_113004.json --batch-size 10 --apply
   ```
   Then re-run without `--apply` to refresh `last_scan.json`; confirm `universe_n` increases by 9, floor becomes TAIKO/USDT, and `eligible_unseen_below_floor_count` becomes 0 (snapshot band exhausted).

3. **Fetch and validate hourly OHLCV** for the 9 new symbols (none on disk). Use `scripts/fetch_kucoin.py` with `--target-bars 22000` and `--reconcile-manifest`. Check: no duplicates, contiguous 1h grid (no missing hours), no invalid OHLC, price identity `|log(last close / CoinGecko price)|` within tolerance. Run ticker-collision checks for short names if ambiguous. Note any cost-dominated names (report cost-to-move multiple). Record exclusions with evidence if any (transient errors -> re-query before excluding).

4. **Run full 66-pair grid for ranks N = 258..266** (one `--n` per symbol), resume from `results/20261019_135940_grid`, checkpoint after each symbol (`python scripts/remote_checkpoint.py --message "chore: grid <SYMBOL>"`). After each, run `scripts/aggregate_grid.py` and `scripts/candidate_check.py`. Update expansion log with batch 26 details and update this handoff.

5. **If snapshot band exhausted** (0 remain after batch 26) take fresh descending snapshot with `scripts/fetch_mcap_snapshot.py --pages 10 --batch-size 10` (dry run), inspect timestamped snapshot/exclusions, extend pages only if not below floor. If zero eligible, persist `AWAITING_NEW_ELIGIBLE_CANDIDATES` with evidence and next refresh >=24h out. Never force expansion or relax gates.

## Guardrails
- Append-only, market-cap descending, only below current floor.
- No stopping on negative results.
- Never promote without OOS + 2x-cost gates.
- Keep baseline/grid unchanged unless preregistered mutation.
- Run `python -m pytest tests/ -q` after changes; report exact results.

## Environment
Use `PYTHONPATH=. python3 scripts/...` from repo root. Checkpoint durably after each symbol. ~10 min/symbol budget.

## Session update (2026-10-20T22:30:00Z)
- Applied batch 25 from saved snapshot (N 247→257). Fetched/validated 10 fixtures (all below WOO floor, now ARPA floor). Completed 66-pair grid for all 10 (660 cells), re-ran aggregate and candidate check: 0 credible candidates. Updated `universe/mcap_expansion_log.md` with batch 25 section. Refreshed handoffs. Tests: 56 passed. No code changes.