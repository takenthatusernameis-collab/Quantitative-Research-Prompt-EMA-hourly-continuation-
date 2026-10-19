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

## Batch 3 - expansion to N = 37

- Snapshot: `universe/mcap_snapshot_20261019_163400.json`
- Source: CoinGecko `/api/v3/coins/markets` (`order=market_cap_desc`)
- Fetched at: 2026-10-19T16:34:00Z
- Previous N -> new N: **27 -> 37** (ranks 28-37 of the working universe)
- Expansion floor: ONDO at 2 122 015 803 USD (the lowest market cap already in
  the universe in this snapshot); every added name is strictly below it.
- Added (market cap at snapshot time, USD):

| Rank in snapshot | Symbol | Market cap |
|---|---|---|
| 50 | DOT | 1 992 608 822 |
| 51 | WLD | 1 958 399 586 |
| 56 | MNT | 1 768 796 975 |
| 59 | PEPE | 1 734 788 742 |
| 62 | SKY | 1 629 404 908 |
| 63 | ICP | 1 598 220 188 |
| 65 | HTX | 1 469 017 242 |
| 66 | ARB | 1 358 407 731 |
| 70 | ETC | 1 234 200 245 |
| 72 | JST | 1 122 408 238 |

### Hourly coverage of the batch-3 fixtures

OHLCV comes from the KuCoin public candles API (1h, UTC), 22 000 bars per
symbol, same as the earlier batches. Two names have a slightly different span
because their KuCoin listing date is what bounds the history:

| Symbol | Rows | Span (UTC) |
|---|---|---|
| DOT, WLD, MNT, PEPE, ICP, ARB, ETC | 22 000 | 2024-04-16 .. 2026-10-19 |
| HTX | 22 098 | 2024-04-11 .. 2026-10-19 |
| JST | 22 099 | 2024-04-11 .. 2026-10-19 |
| SKY | 17 934 | 2024-10-02 .. 2026-10-19 |

SKY is the only name in the batch with a shorter history: it was listed on
KuCoin in October 2024, so it carries 17 934 hourly bars (~2.04 years). That
still clears the 2-year eligibility floor used for the ranking filter
(`MIN_HISTORY_YEARS = 2.0`) and covers the largest registered period
(P_slow = 200) plus an out-of-sample window, but it is the shortest sample in
the working universe and is flagged here for the record.

### Rank drift, batch 2 snapshot (14:42) vs batch 3 snapshot (16:34)

Max absolute market-cap drift across the 27 names already in the universe was
**2.33 %** (ENA +2.33 %, NEAR +1.83 %, ZEC +1.80 %). Two names changed rank
(NEAR 20 -> 19, QNT 40 -> 38) because of names that are **not** in the working
universe, so the relative order of the 27 already-included names is unchanged.
The global strictly-descending market-cap order is therefore preserved across
the three snapshots, and the batch-3 additions can be appended without
reordering anything.

---

## Batch 4 - expansion to N = 47

- Snapshot: `universe/mcap_snapshot_20261019_181146.json`
- Source: CoinGecko `/api/v3/coins/markets` (`order=market_cap_desc`)
- Fetched at: 2026-10-19T18:11:46Z
- Previous N -> new N: **37 -> 47** (ranks 38-47 of the working universe)
- Expansion floor: JST at 1 121 015 524 USD (the lowest market cap already in
  the universe in this snapshot); every added name is strictly below it.
- Added (market cap at snapshot time, USD):

| Rank in snapshot | Symbol | Market cap |
|---|---|---|
| 74 | KCS | 1 037 220 420 |
| 75 | ALGO | 985 041 622 |
| 76 | POL | 978 151 993 |
| 77 | KAS | 971 555 192 |
| 78 | JUP | 967 935 498 |
| 80 | ATOM | 939 040 936 |
| 81 | RENDER | 932 190 782 |
| 83 | INJ | 861 230 020 |
| 84 | FIL | 844 516 724 |
| 88 | AERO | 783 036 938 |

The batch was applied from the reviewed snapshot file itself
(`--apply-from universe/mcap_snapshot_20261019_181146.json`), so the names
processed by the grid are exactly the ones listed above. The batch is in
strictly descending market-cap order and every name ranks below JST.

### Hourly coverage of the batch-4 fixtures

OHLCV comes from the KuCoin public candles API (1h, UTC), 22 000 bars per
symbol, same as the earlier batches:

| Symbol | Rows | Span (UTC) |
|---|---|---|
| KCS, ALGO, POL, KAS, JUP, ATOM, INJ, FIL, AERO | 22 000 | 2024-04-16 .. 2026-10-19 |
| RENDER | 18 947 | 2024-08-21 .. 2026-10-19 |

RENDER is the only short sample in this batch (KuCoin listing date
2024-08-21, ~2.16 years of hourly bars); it still clears the 2-year
eligibility floor and covers the largest registered period (P_slow = 200)
plus an out-of-sample window. All 10 fixtures have no duplicate timestamps
and no hourly gaps.

### Rank drift, batch 3 snapshot (16:34) vs batch 4 snapshot (18:11)

Max absolute market-cap drift across the 37 names already in the universe was
**2.15 %** (DOT -2.15 %, ARB -1.32 %, ICP -1.22 %, TAO -1.18 %, ZEC -1.14 %,
ENA -1.05 %). Two included names swapped rank with each other:

| Symbol | 16:34 market cap | 18:11 market cap | Rank |
|---|---|---|---|
| DOT | 1 992 608 822 | 1 949 703 669 | 50 -> 51 |
| WLD | 1 958 399 586 | 1 964 671 177 | 51 -> 50 |

DOT and WLD inverted on a 0.77 % market-cap difference. The working universe
is **append-only**: the batch-3 order (DOT before WLD) is kept so that the
already-processed symbols keep their artifact continuity and the reported
processing order stays stable. The batch-4 additions are appended below the
existing floor, so the global order remains strictly descending across
batches apart from this single sub-1 % inversion inside the batch-3 block.

(The SOL/BNB order in the working universe is inherited from batch 0, whose
ranking file carried no source metadata; it was left untouched for the same
append-only reason.)

---

## Grid coverage per batch

| Batch | Universe N | Symbols with a full 66-pair grid | Grid artifact |
|---|---|---|---|
| Batch 0 | 5 | BTC, ETH, SOL, BNB, XRP | `results/20261019_135940_grid/` |
| Batch 1 | 17 | + TRX, ZEC, DOGE, XMR, LINK, ADA, NEAR, XLM, BCH, LTC, UNI, AVAX | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 2 | 27 | complete - SUI, GRAM, HBAR, TAO, SHIB, CRO, QNT, ENA, AAVE, ONDO (66 pairs each) | `results/20261019_135940_grid/` |
| Batch 3 | 37 | complete - DOT, WLD, MNT, PEPE, SKY, ICP, HTX, ARB, ETC, JST (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 4 | 47 | complete - KCS, ALGO, POL, KAS, JUP, ATOM, RENDER, INJ, FIL, AERO (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |

The grid directory is shared across batches (the runner resumes from
`progress.json`), so one aggregate report covers the whole processed universe.
OHLCV for every symbol in every batch is in `data/fixtures/`, with provenance in
`data/fixtures/fetch_manifest.json` (KuCoin public `/api/v1/market/candles`,
1h, UTC).
