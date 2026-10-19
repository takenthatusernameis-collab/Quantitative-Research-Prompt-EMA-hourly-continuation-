# Market-Cap Universe Expansion Log

Every universe change for the EMA hourly-continuation program, in order.
Required by PROMPT.md §2.1 (rule 6): *previous N -> new N, rank range added,
source/date of the ranking used*. The machine-readable copy of the current
ranking is `universe/mcap_rank.json`; each ranking snapshot is kept verbatim in
`universe/mcap_snapshot_<TS>.json`.

**Ranking source family (all batches):** CoinGecko public API
`/api/v3/coins/markets?vs_currency=usd&order=market_cap_desc`, filtered by
`scripts/fetch_mcap_snapshot.py` to names that (a) are not stablecoins / fiat
pegs, (b) are not wrapped or staked duplicates of an existing name, (c) have a
tradable KuCoin spot USDT pair, and (d) have >= 2 years of hourly history
(`MIN_HISTORY_YEARS = 2.0`, enough to cover the largest registered period
P_slow = 200 plus an out-of-sample window).

---

## Batch 0 - initial program snapshot: N = 5

- `updated_at`: 2026-10-19T00:50:00Z
- Symbols (market-cap descending): BTC, ETH, SOL, BNB, XRP
- Note: the original file carried no source metadata; the ranking family was
  fixed with batch 1 below and re-verified against it.

---

## Batch 1 - expansion to N = 17

- Snapshot: `universe/mcap_snapshot_20261019_133403.json`
- Source: CoinGecko `/api/v3/coins/markets` (`order=market_cap_desc`)
- Fetched at: 2026-10-19T13:34:03Z
- Previous N -> new N: **5 -> 17** (ranks 6-17 added)
- Added (market cap at snapshot time, USD):

| # | Symbol | Market cap |
|---|---|---|
| 6 | TRX | 31 529 306 203 |
| 7 | ZEC | 19 437 807 896 |
| 8 | DOGE | 12 467 701 858 |
| 9 | XMR | 11 213 006 011 |
| 10 | LINK | 9 260 283 739 |
| 11 | ADA | 8 227 929 563 |
| 12 | NEAR | 6 521 016 141 |
| 13 | XLM | 6 236 195 716 |
| 14 | BCH | 5 605 992 228 |
| 15 | LTC | 4 681 549 464 |
| 16 | UNI | 4 590 903 394 |
| 17 | AVAX | 4 316 521 653 |

---

## Batch 2 - expansion to N = 27

- Snapshot: `universe/mcap_snapshot_20261019_144235.json`
- Source: CoinGecko `/api/v3/coins/markets` (`order=market_cap_desc`)
- Fetched at: 2026-10-19T14:42:35Z
- Previous N -> new N: **17 -> 27** (ranks 18-27 of the working universe)
- Expansion floor: AVAX at 4 258 366 460 USD (the lowest market cap already in
  the universe); every added name is strictly below it.
- Added (market cap at snapshot time, USD):

| Rank in snapshot | Symbol | Market cap |
|---|---|---|
| 29 | SUI | 4 063 737 931 |
| 31 | GRAM | 3 782 489 272 |
| 32 | HBAR | 3 629 315 356 |
| 35 | TAO | 3 031 583 353 |
| 36 | SHIB | 2 933 457 866 |
| 37 | CRO | 2 911 067 973 |
| 40 | QNT | 2 829 274 851 |
| 41 | ENA | 2 476 194 849 |
| 46 | AAVE | 2 271 611 606 |
| 48 | ONDO | 2 103 230 369 |

### Rank drift, batch 1 snapshot (13:34) vs batch 2 snapshot (14:42)

| Symbol | 13:34 market cap | 14:42 market cap | Drift |
|---|---|---|---|
| TRX | 31 529 306 203 | 31 523 294 925 | -0.02 % |
| ZEC | 19 437 807 896 | 19 039 011 896 | -2.05 % |
| DOGE | 12 467 701 858 | 12 345 718 482 | -0.98 % |
| XMR | 11 213 006 011 | 11 273 029 115 | +0.53 % |
| LINK | 9 260 283 739 | 9 157 744 554 | -1.11 % |
| ADA | 8 227 929 563 | 8 125 711 767 | -1.24 % |
| NEAR | 6 521 016 141 | 6 390 935 582 | -2.00 % |
| XLM | 6 236 195 716 | 6 167 236 773 | -1.11 % |
| BCH | 5 605 992 228 | 5 564 337 607 | -0.74 % |
| LTC | 4 681 549 464 | 4 636 903 287 | -0.95 % |
| UNI | 4 590 903 394 | 4 534 625 041 | -1.22 % |
| AVAX | 4 316 521 653 | 4 258 366 460 | -1.35 % |

**No order changes inside the working universe** (max drift 2.05 %), so the
global strictly-descending market-cap order is preserved across the two
snapshots. This is why the batch-2 additions can be appended without reordering
anything.

---

## Grid coverage per batch

| Batch | Universe N | Symbols with a full 66-pair grid | Grid artifact |
|---|---|---|---|
| Batch 0 | 5 | BTC, ETH, SOL, BNB, XRP | `results/20261019_135940_grid/` |
| Batch 1 | 17 | + TRX, ZEC, DOGE, XMR, LINK, ADA, NEAR, XLM, BCH, LTC, UNI, AVAX | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 2 | 27 | pending - SUI, GRAM, HBAR, TAO, SHIB, CRO, QNT, ENA, AAVE, ONDO | - |

The grid directory is shared across batches (the runner resumes from
`progress.json`), so one aggregate report covers the whole processed universe.
OHLCV for every symbol in every batch is in `data/fixtures/`, with provenance in
`data/fixtures/fetch_manifest.json` (KuCoin public `/api/v1/market/candles`,
1h, UTC).
