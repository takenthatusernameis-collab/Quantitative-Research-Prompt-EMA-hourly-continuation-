# NEXT AGENT TASK

## Current state (verified against the saved artifacts, 2026-10-20T17:25:00Z)

**Program status: `EXPANSION_AVAILABLE`.** Batch 21 (universe N 207 -> 217) is **complete**: the 66-pair EMA grid is finished for all 217 symbols, the aggregate and the OOS + 2x-cost candidate check have been re-run, and the expansion log records the outcome. The universe is **not** exhausted: the current ranking snapshot still holds 49 eligible unseen names below the floor, so the next batch can be applied from the saved snapshot **without** querying CoinGecko again.

- Universe: **N = 217**, last symbol EUL/USDT at **USD 26 770 327** (the floor). `universe/mcap_rank.json`, snapshot `mcap_snapshot_20261020_113004` (CoinGecko, fetched 2026-10-20T11:30:04Z, pages 1-10, 1 000 ranked entries down to $15 174 185 - the pass reaches below the floor).
- Grid: **14 322 / 14 322 cells complete** in `results/20261019_135940_grid/` (217 symbols x 66 EMA pairs); 0 blocked. `progress.json` reports `next_cell: null` and `all_symbols_processed: true`.
- Decision count: **14 296 rejected**, 26 exploratory at the aggregate scan, and **0 credible candidates** after the OOS + 2x-cost check.
- Pooled, full-sample net of costs (10 bps taker + 2 bps slippage per side): mean net profit factor **0.4967**, median **0.5177**, best in-sample PF **2.2274** (BABYDOGE/USDT P50_55; rejected, zero OOS trades), **11 666 585 trades**.
- Cells with full-sample net PF > 1: **36 / 14 322 (0.25 %)**. All 36 failed the required OOS and 2x-cost checks, and the set is **unchanged from batch 20** (32 BABYDOGE cells with zero OOS trades, JASMY P20_200, JASMY P21_200, SUPER P8_200, MOODENG P8_200). The OOS window is the trailing 35% of each symbol's bars. Batch 21 added no survivor.
- Candidate-check artifact: `results/20261020_171216_candidate_check/summary.md` (36 cells, 36 rejected). Requirements for credibility remain: OOS net PF > 1, OOS Sharpe > 0, at least 30 OOS trades, and PF > 1 under 2x fees/slippage.
- Tests last recorded: `python -m pytest tests/ -q` -> **56 passed** (re-verified 2026-10-20T17:20:00Z). No code changes in this session.

**Machine-readable state:** `universe/last_scan.json` - `state=EXPANSION_AVAILABLE`, `universe_n=217`, floor `EUL/USDT 26 770 327`, `eligible_unseen_below_floor_count=49`, `batch_selected` = the 10 batch-22 names below, `next_eligible_refresh_at=null` (no waiting is required because the snapshot still holds eligible names).

**Do not wait 24 hours.** The 24h refresh bound in PROMPT.md §2.1.5 applies only when a ranking pass yields **zero** eligible unseen names. The 2026-10-20T11:30:04Z pass was not empty, so the next batch is applied from that saved snapshot. A fresh CoinGecko pull would only be allowed from 2026-10-21T11:30:04Z, and is not needed for batch 22.

## Required next action - apply and process batch 22

1. **Reconcile state first.** Read this handoff, `PROMPT.md` §2.1, `universe/mcap_rank.json`, `universe/last_scan.json`, `universe/mcap_snapshot_20261020_113004.json`, `universe/mcap_expansion_log.md`, the grid `progress.json` and the latest candidate-check artifact. Do not repeat a completed scan and do not re-run finished grid cells.
2. **Apply the next 10 names from the saved snapshot** (verified by dry run at 2026-10-20T17:16Z; they are the 10 highest-ranked eligible names strictly below the floor, in descending market-cap order):

   | Rank in snapshot | Symbol | Name | Market cap (USD) | Fixture on disk? |
   |---|---|---|---|---|
   | 721 | FLIP/USDT | Chainflip | 26 697 475 | no |
   | 726 | G/USDT | Gravity (by Galxe) | 26 376 038 | no |
   | 730 | EWT/USDT | Energy Web Token | 26 309 600 | no |
   | 734 | ERG/USDT | Ergo | 26 061 512 | no |
   | 745 | NYM/USDT | Nym | 25 472 687 | no |
   | 746 | SKL/USDT | SKALE | 25 450 152 | no |
   | 752 | AUCTION/USDT | Bounce | 25 193 109 | no |
   | 754 | KNC/USDT | Kyber Network Crystal | 25 068 821 | no |
   | 756 | VR/USDT | Victoria VR | 25 025 182 | no |
   | 763 | CARV/USDT | CARV | 24 788 571 | no |

   `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --apply-from universe/mcap_snapshot_20261020_113004.json --batch-size 10 --apply`

   Apply only from the reviewed saved snapshot. Preserve append-only global ordering: never remove or reorder existing rows. The apply step rewrites `universe/last_scan.json`; that is expected. Re-run the same command **without** `--apply` afterwards to refresh `last_scan.json` against the new N, and confirm the file then reports `universe_n=227`, floor `CARV/USDT`, `eligible_unseen_below_floor_count=39` and `batch_selected` = the ten names after CARV (the current file, recorded 2026-10-20T17:16:53Z, is consistent with N=217).
3. **Fetch and validate the new hourly OHLCV fixtures** for the 10 symbols that have none:
   `PYTHONPATH=. python3 scripts/fetch_kucoin.py --target-bars 22000 --symbols FLIP/USDT G/USDT EWT/USDT ERG/USDT NYM/USDT SKL/USDT AUCTION/USDT KNC/USDT VR/USDT CARV/USDT`
   then reconcile provenance with `PYTHONPATH=. python3 scripts/fetch_kucoin.py --reconcile-manifest`.
   A transient API error is not proof of ineligibility: re-query a failed symbol as the existing prompt specifies before excluding it. Record coverage, gaps, duplicates, price/ticker identity and all exclusion reasons (the batch-20/batch-21 validation recipe: no duplicate timestamps, contiguous 1h grid with no missing hours, no invalid OHLC rows, and `|log(last close / CoinGecko price)|` well inside the script's 0.20 tolerance).
   **Ticker-collision check is mandatory for this batch:** `G/USDT` (Gravity by Galxe) and `VR/USDT` (Victoria VR) are short symbols that could resolve to a different KuCoin asset. The script's price-identity tolerance (0.20 in log terms) is the gate - if a fetched pair does not match the ranked CoinGecko price, treat it as the `kucoin_pair_trades_a_different_asset` exclusion, not as a data error.
   **Price-scale warning (carry-over from batch 21):** a symbol trading far below a cent is dominated by the fixed 12 bps per-side cost. ELON/USDT (~2.96e-08 USD) cost ~29x its median absolute hourly move, and NFT/USDT (batch 8, last close 2.39e-07 USD) ~58x. This is a valid test of the registered rules, but its result measures cost drag rather than signal quality, and its cell trade counts can behave oddly (in batch 21 ELON's trade counts did **not** explode - 805 per cell - so verify rather than assume). Report it, do not treat it as a defect.
4. **Run the entire 66-pair grid for each newly appended symbol** in strict market-cap order, checkpointing one symbol at a time. Resume the existing run; do not overwrite completed cells:
   `PYTHONPATH=. python3 scripts/run_grid.py --n <rank-in-working-universe> --resume results/20261019_135940_grid --note "universe expansion batch 22: N 217 -> 227 (<SYMBOL>/USDT, 66-pair EMA grid)"`
   Ranks 218-227 = FLIP, G, EWT, ERG, NYM, SKL, AUCTION, KNC, VR, CARV. Note the `--n` semantics: it is the **count** of symbols to process from the top of the market-cap ranking, so `--n 218` processes ranks 1-218 and the runner skips the 217 already-complete symbols, leaving exactly FLIP's 66 cells; `--n 219` adds G, and so on. One `--n` invocation per symbol keeps the checkpoint delta small. After each symbol, checkpoint its result (remote push, see "Environment"), then run `scripts/aggregate_grid.py --run results/20261019_135940_grid` and `scripts/candidate_check.py --run results/20261019_135940_grid`; update the expansion log, progress summary and this handoff with the actual outcome.
5. **When the saved snapshot's band is exhausted** (49 eligible names remain below the floor now, so this is not close), take a fresh descending market-cap snapshot with the existing script (`PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 10 --batch-size 10` as a dry run), inspect the timestamped snapshot it writes and the exact candidate/exclusion results, and extend the page count only if the pass does not reach below the current floor. Respect bounded retries and provider rate limits. If a complete pass yields zero eligible names, persist a truthful `AWAITING_NEW_ELIGIBLE_CANDIDATES` state with evidence and a next refresh time >= 24h out. Do not invent names, repeatedly hit providers, change the strategy baseline, or call a candidate credible on in-sample metrics.

## Known gaps and open items (carry these forward truthfully)

- **GAS (rank 320, $80.3M) and CCD (rank 533, $41.79M)** are eligible in the current snapshot but rank **above** the floor, so the strict "append only names strictly below the floor" rule (PROMPT.md §2.1.2) keeps them out of the universe. CCD's hourly fixture is already on disk (`data/fixtures/CCD_USDT.csv`); it enters the universe automatically if a later snapshot puts it below the floor. Do not insert either name out of market-cap order.
- **`data/fixtures/fetch_manifest.json` holds 218 rows**, not 217: the extra row is the pre-fetched CCD file, which is not a universe member. Reconcile rather than hand-edit. (`data/fixtures/sample_hourly.csv` is a synthetic sample and is correctly absent from the manifest.)
- **UQC/USDT (batch 21) is an extremely thin pair**: 48.9 % of its bars have zero volume and 55.8 % close unchanged, so its trade count (377 per cell) and mean net PF (0.2053) are artefacts of a flat price, not a broken fixture. It has 0 zero-volume-but-moving-OHLC quote-carry bars. Do not "fix" it.
- **ELON/USDT (batch 21) is cost-dominated** (12 bps per side vs a 0.41 % median absolute hourly move). Its result measures cost drag, not signal quality.
- **Thin pairs quote-carry** (bars with zero volume but moving OHLC): LISTA 12.9 %, GTC 11.5 %, MAGIC 9.3 % of bars in batch 20. This is a known property of the data layer, not a defect; a zero-volume-bar filter would be a registered mutation (§5), not a silent change. Batch 21 had **no** quote-carry bars in any of its ten fixtures.
- **REZ/USDT (batch 20) is the strongest single symbol in the program** (mean net PF 0.6629 over 51 445 trades) and BABYDOGE/USDT (batch 14) is the only symbol whose mean net PF exceeds 1.0 (1.0628) - but on just 2 775 trades across 66 cells, with zero OOS trades in every one of its 32 above-PF cells. Both are multiple-testing noise, not edges.
- **Batch 21 had the lowest mean net PF of any batch so far (0.4697)**, and the per-batch means are flat-to-declining from b7 to b21. The registered rule does not improve as market cap falls; this is the program-level finding, and it does not authorise stopping.
- The b7-b20 mean-net-PF-by-batch list printed in the batch-20 cumulative section of `universe/mcap_expansion_log.md` was misaligned by one entry from b14 onward; the batch-21 cumulative section carries the recomputed list (b7-b21) derived from `results/20261019_135940_grid/per_symbol.json` and the coverage table in the log. Use the recomputed one.

## Guardrails

- Keep the universe append-only and strictly market-cap descending; add only new eligible symbols below the existing floor.
- Never stop merely because the grid or a batch produced no edge. A negative result on the registered rules is not authorization to close the program.
- Never lower data-history or liquidity requirements to force expansion. Distinguish a genuinely absent pair/history from a transient API error or an incomplete ranking scan.
- Never promote an in-sample winner without passing the preregistered OOS and doubled-cost gates. Preserve every prior result, candidate rejection and provenance record.
- Keep the registered baseline and 66-pair EMA grid unchanged unless a separately preregistered mutation is authorized.
- Run `python -m pytest tests/ -q` after code changes and report the exact results.

## Environment

Use `PYTHONPATH=. python3 scripts/...` from the repository root. Available data fixtures and all prior result artifacts are reusable; fetch only data for genuinely new symbols. Checkpoint durably after each finished symbol with `python scripts/remote_checkpoint.py --message "chore: grid <SYMBOL>"` (the workflow controller only allows a 30s push, so keep each delta small).

## Session update (2026-10-20T17:25:00Z)

- Read the batch-21 handoff and reconciled the saved artifacts: the prior session had already applied batch 21 (universe **N 207 -> 217**: ELON, CTSI, IOST, SWFTC, UQC, ILV, AVA, CPOOL, BLUR, EUL), fetched and validated the 10 new hourly fixtures, run the 66-pair grid for all ten (ranks 208-217), and re-run the aggregate + candidate check. Re-verified every artifact rather than re-running finished work: **14 322 / 14 322 cells** complete, 0 blocked, `next_cell: null`; all 10 new symbols have 66 cells each with a complete artifact set (config, trades, equity, summary).
- Re-validated the batch-21 fixtures independently: no duplicate timestamps, no missing hours (contiguous 1h grid), no invalid OHLC rows, and price identity `|log(last close / CoinGecko price)|` <= 0.1353 (worst: IOST) - all well inside the 0.20 tolerance. Manifest reconciled: 218 rows (217 universe symbols + the pre-fetched CCD file).
- Re-ran `scripts/aggregate_grid.py` outputs: mean net PF 0.4967, median 0.5177, best 2.2274, 11 666 585 trades, 36 cells above net PF 1, 26 exploratory, 14 296 rejected, 0 blocked. Re-ran `scripts/candidate_check.py`: `results/20261020_171216_candidate_check/` - 36/36 rejected, **0 credible candidates**. The above-PF set is unchanged from batch 20; batch 21 contributed no survivor.
- Updated `universe/mcap_expansion_log.md`: added the batch-21 section (selection, fixture coverage table, grid outcome table), the cumulative state at N=217, the batch-22 candidate list, the batch-21 row in the per-batch coverage table, and a correction note for the previously misaligned b7-b20 mean-PF list.
- Refreshed this handoff and `INITIAL_TASK_FOR_NEXT_AGENT.md` for batch 22 (FLIP, G, EWT, ERG, NYM, SKL, AUCTION, KNC, VR, CARV; ranks 218-227).
- Tests: `python -m pytest tests/ -q` -> **56 passed**. No code changes in this session.
