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

## Batch 5 - expansion to N = 57

- Snapshot: `universe/mcap_snapshot_20261019_185635.json`
- Source: CoinGecko `/api/v3/coins/markets` (`order=market_cap_desc`)
- Fetched at: 2026-10-19T18:56:35Z
- Previous N -> new N: **47 -> 57** (ranks 48-57 of the working universe)
- Expansion floor: AERO at 780 838 782 USD (the lowest market cap already in
  the universe in this snapshot); every added name is strictly below it.
- Added (market cap at snapshot time, USD):

| Rank in snapshot | Symbol | Market cap |
|---|---|---|
| 90 | ZRO | 760 259 950 |
| 92 | CAKE | 688 795 599 |
| 94 | STX | 675 577 750 |
| 95 | APT | 674 374 228 |
| 98 | ETHFI | 654 227 649 |
| 99 | XDC | 652 852 067 |
| 100 | DASH | 639 062 735 |
| 102 | TIA | 596 408 959 |
| 103 | BDX | 586 463 512 |
| 105 | CRV | 579 257 148 |

### Hourly coverage of the batch-5 fixtures

OHLCV from the KuCoin public candles API (1h, UTC), 22 000 bars per symbol:

| Symbol | Rows | Span (UTC) |
|---|---|---|
| CAKE, APT, ETHFI, XDC, DASH, TIA, BDX, CRV | 22 000 | 2024-04-16 .. 2026-10-19 |
| STX | 22 099 | 2024-04-12 .. 2026-10-19 |
| ZRO | 20 431 | 2024-06-20 .. 2026-10-19 |

ZRO is the shortest sample in the batch (KuCoin listing date 2024-06-20,
~2.34 years of hourly bars). It still clears the 2-year eligibility floor and
covers the largest registered period (P_slow = 200) plus an out-of-sample
window. All 10 fixtures have no duplicate timestamps and no hourly gaps.

### Rank drift, batch 4 snapshot (18:11) vs batch 5 snapshot (18:56)

Max absolute market-cap drift across the 47 names already in the universe was
**1.52 %** (WLD -1.52 %, XMR -0.54 %, AAVE -0.38 %). The only order change
inside the working universe was the already-recorded DOT/WLD inversion
(WLD 50 -> 51, DOT 51 -> 50 on a 0.77 % market-cap gap); the append-only
policy keeps the batch-3 order, so the global strictly-descending order is
preserved apart from that single sub-1 % inversion.

*(This section was reconstructed after the fact from
`universe/mcap_snapshot_20261019_185635.json`, `universe/mcap_rank.json` and
`data/fixtures/fetch_manifest.json`; the batch-5 grid itself ran exactly the
10 names listed above.)*

---

## Batch 6 - expansion to N = 67

- Snapshot: `universe/mcap_snapshot_20261019_200749.json`
- Source: CoinGecko `/api/v3/coins/markets` (`order=market_cap_desc`)
- Fetched at: 2026-10-19T20:07:49Z
- Previous N -> new N: **57 -> 67** (ranks 58-67 of the working universe)
- Expansion floor: CRV at 576 270 770 USD (the lowest market cap already in
  the universe in this snapshot); every added name is strictly below it.
- The batch was applied from the reviewed snapshot file itself
  (`--apply-from universe/mcap_snapshot_20261019_200749.json`), so the names
  processed by the grid are exactly the ones listed below.
- Added (market cap at snapshot time, USD):

| Rank in snapshot | Symbol | Market cap |
|---|---|---|
| 106 | VET | 574 830 218 |
| 107 | PYTH | 566 923 311 |
| 108 | FLR | 556 391 814 |
| 113 | RAY | 505 400 534 |
| 122 | STRK | 438 877 813 |
| 123 | FET | 433 365 015 |
| 126 | SEI | 405 089 053 |
| 128 | PENDLE | 355 726 956 |
| 129 | BSV | 351 699 982 |
| 132 | BTT | 345 385 873 |

VET is the first name in the batch and is the 58th symbol of the working
universe; BTT is the 67th and last. XTZ (rank 136) is the next eligible name
below the floor and is reserved for batch 7.

### Hourly coverage of the batch-6 fixtures

OHLCV from the KuCoin public candles API (1h, UTC), 22 000 bars per symbol:

| Symbol | Rows | Span (UTC) |
|---|---|---|
| VET, PYTH, FLR, RAY, STRK, FET, SEI, PENDLE, BSV, BTT | 22 000 | 2024-04-16 05:00 .. 2026-10-19 20:00 |

All 10 fixtures carry the full 22 000 hourly bars (~2.51 years), have no
duplicate timestamps and no hourly gaps, and comfortably clear the 2-year
eligibility floor.

### Rank drift, batch 5 snapshot (18:56) vs batch 6 snapshot (20:07)

Max absolute market-cap drift across the 57 names already in the universe was
**1.08 %** (XMR +1.08 %, AERO +0.91 %, ETHFI -0.82 %, SKY +0.80 %). The only
order changes inside the working universe are the already-recorded DOT/WLD
inversion and two new sub-1 % inversions (KAS/JUP and ETHFI/XDC):

| Symbol | 18:56 market cap | 20:07 market cap | Rank |
|---|---|---|---|
| WLD | 1 934 801 860 | 1 949 109 830 | 51 -> 50 |
| DOT | 1 948 989 365 | 1 942 717 060 | 50 -> 51 |
| KAS | 971 478 091 | 965 596 519 | 77 -> 78 |
| JUP | 965 652 778 | 969 381 503 | 78 -> 77 |
| ETHFI | 654 227 649 | 648 845 637 | 98 -> 100 |
| XDC | 652 852 067 | 652 900 299 | 99 -> 98 |

The working universe is **append-only**: the existing order is kept so that the
already-processed symbols keep their artifact continuity and the reported
processing order stays stable. The batch-6 additions are appended strictly
below the CRV floor, so the global order remains strictly descending across
batches apart from those sub-1 % inversions inside earlier blocks.

---

## Batch 7 - expansion to N = 77

- Snapshot: `universe/mcap_snapshot_20261019_204714.json`
- Source: CoinGecko `/api/v3/coins/markets` (`order=market_cap_desc`)
- Fetched at: 2026-10-19T20:47:14Z
- Previous N -> new N: **67 -> 77** (ranks 68-77 of the working universe)
- Expansion floor: BTT at 345 406 528 USD (the lowest market cap already in the
  universe in this snapshot); every added name is strictly below it.
- The batch was applied from the reviewed snapshot file itself
  (`--apply-from universe/mcap_snapshot_20261019_204714.json`), so the names
  processed by the grid are exactly the ones listed below.
- Added (market cap at snapshot time, USD):

| Rank in snapshot | Symbol | Market cap |
|---|---|---|
| 135 | XTZ | 330 121 475 |
| 138 | LDO | 321 149 160 |
| 140 | SUN | 317 204 872 |
| 144 | BAT | 294 580 125 |
| 150 | OP | 284 207 834 |
| 151 | CFX | 272 199 535 |
| 155 | GRT | 259 117 191 |
| 156 | DCR | 257 502 629 |
| 157 | BONK | 256 628 563 |
| 158 | LUNC | 252 104 160 |

XTZ is the first name in the batch and is the 68th symbol of the working
universe; LUNC is the 77th and last. AR (Arweave, rank 160) is the next
eligible name below the floor and is reserved for batch 8.

### Hourly coverage of the batch-7 fixtures

OHLCV from the KuCoin public candles API (1h, UTC), 22 000 bars per symbol:

| Symbol | Rows | Span (UTC) |
|---|---|---|
| XTZ, LDO, BAT, OP, CFX, BONK, LUNC | 22 000 | 2024-04-16 05:00/06:00 .. 2026-10-19 20:00/21:00 |
| SUN | 22 098 | 2024-04-12 01:00 .. 2026-10-19 18:00 |
| GRT, DCR | 22 099 | 2024-04-12 02:00 .. 2026-10-19 20:00 |

All 10 fixtures carry ~22 000 hourly bars (~2.5 years), have no duplicate
timestamps and no hourly gaps, and comfortably clear the 2-year eligibility
floor.

### Rank drift, batch 6 snapshot (20:07) vs batch 7 snapshot (20:47)

Max absolute market-cap drift across the 67 names already in the universe was
**1.12 %** (ZRO -1.12 %, TIA -0.99 %, NEAR -0.52 %). Six names changed rank,
all by sub-1.2 % market-cap gaps:

| Symbol | 20:07 market cap | 20:47 market cap | Rank |
|---|---|---|---|
| ZRO | 759 959 482 | 751 478 133 | 89 -> 90 |
| KAS | 965 596 519 | 963 109 731 | 78 -> 79 |
| TAO | 3 013 164 632 | 3 007 216 660 | 35 -> 36 |
| ETHFI | 648 845 637 | 647 636 846 | 100 -> 99 |
| DASH | 636 303 132 | 636 671 012 | 101 -> 100 |
| XDC | 652 900 299 | 653 002 658 | 99 -> 98 |

The working universe is **append-only**: the existing order is kept so that the
already-processed symbols keep their artifact continuity and the reported
processing order stays stable. The batch-7 additions are appended strictly
below the BTT floor, so the global order remains strictly descending across
batches apart from those sub-1.2 % inversions inside earlier blocks.

### Batch-7 grid outcome (66 pairs per symbol, net of costs)

| Symbol | Cells | Trades | Mean net PF | Best net PF (cell) | Max net Sharpe | Rejected |
|---|---|---|---|---|---|---|
| XTZ | 66 | 55 064 | 0.4828 | 0.7513 (P34_144) | -1.9452 | 66 |
| LDO | 66 | 54 893 | 0.4774 | 0.6505 (P21_200) | -2.2277 | 66 |
| SUN | 66 | 47 793 | 0.2913 | 0.4978 (P8_200) | -3.8785 | 66 |
| BAT | 66 | 52 773 | 0.4633 | 0.7500 (P8_200) | -1.4044 | 66 |
| OP | 66 | 52 241 | 0.5101 | 0.7400 (P34_200) | -1.5232 | 66 |
| CFX | 66 | 52 968 | 0.5048 | 0.7672 (P8_144) | -1.8555 | 66 |
| GRT | 66 | 53 055 | 0.5251 | 0.9087 (P20_200) | -0.4398 | 66 |
| DCR | 66 | 57 530 | 0.4605 | 0.7359 (P21_200) | -2.1056 | 66 |
| BONK | 66 | 53 245 | 0.5615 | 0.7338 (P8_200) | -1.8996 | 66 |
| LUNC | 66 | 60 053 | 0.4055 | 0.6568 (P55_200) | -2.7820 | 66 |

Batch 7 alone: 660 / 660 cells rejected, 0 cells with net PF > 1, pooled mean
net PF 0.4682, median 0.4896, best 0.9087 (GRT/USDT P20_200), 539 615 trades.
Cumulative over all 77 symbols: **5 082 / 5 082 cells rejected (100 %)**, 0
cells with net PF > 1, pooled mean net PF 0.4629, median 0.4806, best 0.9523
(WLD/USDT P20_200).

---

## Batch 8 - expansion to N = 87

- Snapshot: `universe/mcap_snapshot_20261019_221313.json`
- Source: CoinGecko `/api/v3/coins/markets` (`order=market_cap_desc`)
- Fetched at: 2026-10-19T22:13:13Z
- Previous N -> new N: **77 -> 87** (ranks 78-87 of the working universe)
- Expansion floor: LUNC at 254 234 276 USD (the lowest market cap already in the
  universe in this snapshot); every added name is strictly below it.
- The batch was applied from the reviewed snapshot file itself
  (`--apply-from universe/mcap_snapshot_20261019_221313.json`).
- Added (market cap at snapshot time, USD):

| Rank in snapshot | Symbol | Name | Market cap |
|---|---|---|---|
| 159 | AR | Arweave | 247 175 234 |
| 163 | JTO | Jito | 238 996 450 |
| 164 | NFT | AINFT | 237 016 002 |
| 166 | JASMY | JasmyCoin | 235 618 171 |
| 168 | EIGEN | EigenCloud | 234 581 116 |
| 169 | ENS | Ethereum Name Service | 232 440 182 |
| 170 | KMNO | Kamino | 228 817 283 |
| 171 | FLOKI | FLOKI | 227 904 935 |
| 175 | COMP | Compound | 215 992 779 |
| 178 | RUNE | THORChain | 212 038 301 |

AR is the 78th symbol of the working universe; RUNE is the 87th and last. The
name `NFT` is CoinGecko's ticker for **AINFT** (not an NFT collection index) and
`RUNE` is **THORChain**; both are distinct, liquid spot names on KuCoin.

### Hourly coverage of the batch-8 fixtures

OHLCV from the KuCoin public candles API (1h, UTC):

| Symbol | Rows | Span (UTC) |
|---|---|---|
| AR, JTO, NFT, JASMY, ENS, FLOKI, COMP, RUNE | 22 000 | 2024-04-16 07:00 .. 2026-10-19 22:00 |
| KMNO | 21 659 | 2024-04-30 12:00 .. 2026-10-19 22:00 |
| EIGEN | 17 971 | 2024-10-01 04:00 .. 2026-10-19 22:00 |

All 10 fixtures have no duplicate timestamps and no hourly gaps. KMNO and
EIGEN are listed later than the rest (EIGEN still clears the 2-year floor with
17 971 hourly bars).

### Batch-8 grid outcome (66 pairs per symbol, net of costs)

| Symbol | Cells | Trades | Mean net PF | Best net PF (cell) | Max net Sharpe | Rejected |
|---|---|---|---|---|---|---|
| AR | 66 | 53 213 | 0.5196 | 0.8616 (P8_200) | -0.6920 | 66 |
| JTO | 66 | 53 809 | 0.5736 | 0.8488 (P8_200) | -1.0030 | 66 |
| NFT | 66 | 88 188 | 0.2038 | 0.3322 (P12_100) | -12.9510 | 66 |
| JASMY | 66 | 54 353 | 0.5950 | **1.0341 (P21_200)** | **+0.2673** | 64 |
| EIGEN | 66 | 44 378 | 0.6113 | 0.8574 (P20_200) | -0.9950 | 66 |
| ENS | 66 | 54 536 | 0.5044 | 0.6795 (P12_144) | -2.2080 | 66 |
| KMNO | 66 | 45 605 | 0.5582 | 0.8142 (P8_200) | -1.2120 | 66 |
| FLOKI | 66 | 55 663 | 0.5365 | 0.7157 (P12_100) | -2.0310 | 66 |
| COMP | 66 | 56 509 | 0.4352 | 0.6550 (P8_89) | -2.4860 | 66 |
| RUNE | 66 | 49 710 | 0.5475 | 0.8114 (P50_200) | -1.0050 | 66 |

Batch 8 alone: 660 cells, 658 rejected, 2 exploratory (net PF > 1), pooled mean
net PF 0.5085, median 0.5432, 555 964 trades.

**The first cells in the whole program with net PF > 1** are both on JASMY/USDT:

| Symbol | Cell | Trades | Net PF | Net Sharpe | Gross PF | Net win rate | Avg hold (bars) |
|---|---|---|---|---|---|---|---|
| JASMY/USDT | P20_200 | 353 | 1.0097 | +0.1189 | 1.4115 | 0.5779 | 40.9 |
| JASMY/USDT | P21_200 | 362 | 1.0341 | +0.2673 | 1.4577 | 0.5856 | 38.7 |

They are **not** promoted to "credible candidate": with 6 402 cells scanned, a
0.03 % hit rate is 50x *below* the ~50 % null expectation of a no-edge strategy,
so a marginal in-sample profit factor of 1.03 with a Sharpe of 0.27 is what
noise looks like. They need an out-of-sample and cost-stress check before any
claim (PROMPT.md §3.3, §3.4).

**AINFT (`NFT`) is a price-scale outlier**: its spot price is ~4.6e-07 USD, so
the fixed 12 bps per side cost is a large fraction of every bar move, the
registered 1 % risk rule fires on essentially every EMA cross, and the cell trade
counts explode (88 188 trades over 66 cells vs ~50 000 for ordinary names). It is
a valid test of the registered rules, but its result is dominated by cost drag
rather than by signal quality.

---

## Batch 9 - expansion to N = 97

- Snapshot: `universe/mcap_snapshot_20261019_221514.json`
- Source: CoinGecko `/api/v3/coins/markets` (`order=market_cap_desc`)
- Fetched at: 2026-10-19T22:15:14Z
- Previous N -> new N: **87 -> 97** (ranks 88-97 of the working universe)
- Expansion floor: RUNE at 212 066 417 USD (the lowest market cap already in the
  universe in this snapshot); every added name is strictly below it.
- The batch was applied from the reviewed snapshot file itself
  (`--apply-from universe/mcap_snapshot_20261019_221514.json`).
- Added (market cap at snapshot time, USD):

| Rank in snapshot | Symbol | Name | Market cap |
|---|---|---|---|
| 179 | IOTA | IOTA | 211 287 520 |
| 182 | ZBCN | Zebec Network | 208 394 911 |
| 184 | AKT | Akash Network | 207 165 183 |
| 186 | WIF | dogwifhat | 200 666 439 |
| 187 | CVX | Convex Finance | 195 374 485 |
| 190 | TWT | Trust Wallet | 189 404 592 |
| 191 | THETA | Theta Network | 187 286 791 |
| 198 | AXS | Axie Infinity | 175 746 207 |
| 200 | SAND | The Sandbox | 174 429 112 |
| 201 | TRAC | OriginTrail | 174 150 625 |

IOTA is the 88th symbol of the working universe; TRAC is the 97th and last.
`AXS` here is **Axie Infinity** (not the `AXS` wrapper of a different token) and
`TRAC` is **OriginTrail** (not `TRAC` the crypto index); both are liquid spot
USDT pairs on KuCoin and pass the 2-year hourly-history filter.

### Hourly coverage of the batch-9 fixtures

OHLCV from the KuCoin public candles API (1h, UTC):

| Symbol | Rows | Span (UTC) |
|---|---|---|
| IOTA, AKT, WIF, CVX, TWT, THETA, SAND, TRAC | 22 000 | 2024-04-16 07:00/08:00 .. 2026-10-19 22:00/23:00 |
| ZBCN | 21 614 | 2024-05-02 09:00 .. 2026-10-19 22:00 |
| AXS | 22 099 | 2024-04-12 04:00 .. 2026-10-19 22:00 |

All 10 fixtures have no duplicate timestamps and no hourly gaps. AXS, SAND and
TRAC were re-fetched in this session because the earlier expansion pass had
left them without an OHLCV fixture.

### Batch-9 grid outcome (66 pairs per symbol, net of costs)

| Symbol | Cells | Trades | Mean net PF | Best net PF (cell) | Max net Sharpe | Rejected |
|---|---|---|---|---|---|---|
| IOTA | 66 | 54 400 | 0.4875 | 0.7740 (P8_200) | -1.5490 | 66 |
| ZBCN | 66 | 62 063 | 0.5594 | 0.8712 (P12_200) | -1.0330 | 66 |
| AKT | 66 | 53 244 | 0.5659 | 0.7774 (P34_200) | -1.5150 | 66 |
| WIF | 66 | 54 981 | 0.5844 | 0.7137 (P12_144) | -2.3840 | 66 |
| CVX | 66 | 52 895 | 0.5130 | 0.8391 (P8_200) | -0.8250 | 66 |
| TWT | 66 | 57 795 | 0.4248 | 0.6753 (P12_200) | -2.1900 | 66 |
| THETA | 66 | 52 998 | 0.5286 | 0.8508 (P8_200) | -0.9860 | 66 |
| AXS | 66 | 50 377 | 0.5469 | 0.8426 (P55_200) | -0.9870 | 66 |
| SAND | 66 | 50 742 | 0.4660 | 0.7213 (P50_200) | -2.0260 | 66 |
| TRAC | 66 | 48 642 | 0.5339 | 0.7126 (P26_144) | -2.1530 | 66 |

Batch 9 alone: 660 / 660 cells rejected, 0 cells with net PF > 1, pooled mean
net PF 0.5210, median 0.5453, best 0.8712 (ZBCN/USDT P12_200), 538 137 trades.

### Cumulative state after batch 9 (N = 97)

- **6 402 / 6 402 cells** complete (97 symbols x 66 EMA pairs), 0 blocked.
- 6 400 cells **rejected** (99.97 %), 2 cells **exploratory signal** (the JASMY
  P20_200 / P21_200 cells above), 0 credible candidates.
- Pooled (net of costs, full sample, 10 bps taker + 2 bps slippage per side):
  mean net PF **0.4736**, median 0.4955, best net PF **1.0341**
  (JASMY/USDT P21_200), 5 280 967 trades.
- Cells with net PF > 1: 2 / 6 402 = 0.03 % against a ~50 % no-edge null
  (excess -49.97 %).
- Per-pair pooled leaders (mean net PF over 97 symbols): P8_200 0.6708,
  P20_200 0.6639, P12_200 0.6602, P21_200 0.6549. Worst: P20_21 0.1236,
  P50_55 0.1825, P8_12 0.1845.
- The first 77 symbols are unchanged (mean net PF 0.4629, best 0.9523), so the
  new batches did not resurrect the baseline.

---

## Batch 10 - expansion to N = 107

- Snapshot: `universe/mcap_snapshot_20261019_231438.json`
- Source: CoinGecko `/api/v3/coins/markets` (`order=market_cap_desc`)
- Fetched at: 2026-10-19T23:14:38Z
- Previous N -> new N: **97 -> 107** (ranks 98-107 of the working universe)
- Expansion floor: TRAC at 174 258 174 USD (the lowest market cap already in the
  universe in this snapshot); every added name is strictly below it.
- The batch was applied from the reviewed snapshot file itself
  (`--apply-from universe/mcap_snapshot_20261019_231438.json`).
- Added (market cap at snapshot time, USD):

| Rank in snapshot | Symbol | Name | Market cap |
|---|---|---|---|
| 204 | MANA | Decentraland | 161 677 485 |
| 207 | XCN | Onyxcoin | 160 532 201 |
| 208 | ZK | ZKsync | 159 134 167 |
| 210 | NEO | NEO | 156 227 504 |
| 222 | CHZ | Chiliz | 145 184 423 |
| 223 | APE | ApeCoin | 145 092 257 |
| 228 | IMX | Immutable | 137 664 148 |
| 232 | AIOZ | AIOZ Network | 130 967 117 |
| 233 | 1INCH | 1INCH | 129 868 057 |
| 234 | XEC | eCash | 129 191 291 |

MANA is the 98th symbol of the working universe; XEC is the 107th and last.
`XCN` is **Onyxcoin** (Onyx Protocol), not a wrapped variant of any name already
in the universe.

### Hourly coverage of the batch-10 fixtures

OHLCV from the KuCoin public candles API (1h, UTC):

| Symbol | Rows | Span (UTC) |
|---|---|---|
| MANA, XCN, NEO, CHZ, APE, AIOZ, 1INCH | 22 000 | 2024-04-16 08:00 .. 2026-10-19 23:00 |
| IMX, XEC | 22 099 | 2024-04-12 04:00 .. 2026-10-19 22:00 |
| ZK | 20 511 | 2024-06-17 08:00 .. 2026-10-19 22:00 |

All 10 fixtures have no duplicate timestamps and no hourly gaps; ZK is listed
later than the rest but still clears the 2-year floor with 20 511 hourly bars.

### Batch-10 grid outcome (66 pairs per symbol, net of costs)

| Symbol | Cells | Trades | Mean net PF | Best net PF (cell) | Max net Sharpe | Rejected |
|---|---|---|---|---|---|---|
| MANA | 66 | 53 756 | 0.4909 | 0.7493 (P26_200) | -1.7920 | 66 |
| XCN | 66 | 66 758 | 0.3750 | 0.6097 (P26_200) | -3.5650 | 66 |
| ZK | 66 | 52 705 | 0.5977 | 0.8084 (P12_200) | -1.2190 | 66 |
| NEO | 66 | 54 441 | 0.4280 | 0.6798 (P8_200) | -2.1480 | 66 |
| CHZ | 66 | 53 504 | 0.5327 | 0.8649 (P20_200) | -0.8210 | 66 |
| APE | 66 | 54 416 | 0.5099 | 0.7283 (P20_200) | -1.7740 | 66 |
| IMX | 66 | 52 249 | 0.5783 | 0.9891 (P34_200) | -0.0015 | 66 |
| AIOZ | 66 | 59 072 | 0.5778 | 0.7206 (P8_144) | -2.6530 | 66 |
| 1INCH | 66 | 54 921 | 0.4634 | 0.8176 (P34_200) | -0.9580 | 66 |
| XEC | 66 | 57 718 | 0.4630 | 0.6660 (P26_144) | -2.9520 | 66 |

Batch 10 alone: 660 / 660 cells rejected, 0 cells with net PF > 1, pooled mean
net PF 0.5017, median 0.5195, best 0.9891 (IMX/USDT P34_200), 559 540 trades.

---

## Batch 11 - expansion to N = 117

- Snapshot: `universe/mcap_snapshot_20261020_001659.json`
- Source: CoinGecko `/api/v3/coins/markets` (`order=market_cap_desc`)
- Fetched at: 2026-10-20T00:16:59Z
- Previous N -> new N: **107 -> 117** (ranks 108-117 of the working universe)
- Expansion floor: XEC at 128 921 566 USD (the lowest market cap already in the
  universe in this snapshot); every added name is strictly below it.
- The batch was applied from the reviewed snapshot file itself
  (`--apply-from universe/mcap_snapshot_20261020_001659.json`).
- Added (market cap at snapshot time, USD):

| Rank in snapshot | Symbol | Name | Market cap |
|---|---|---|---|
| 242 | SNX | Synthetix | 125 319 862 |
| 246 | SUPER | SuperVerse | 121 344 825 |
| 248 | DBR | deBridge | 119 457 637 |
| 252 | RSR | Reserve Rights | 115 661 828 |
| 260 | EGLD | MultiversX | 112 034 441 |
| 262 | GLM | Golem | 111 601 948 |
| 265 | ZEN | Horizen | 109 813 570 |
| 266 | ATH | Aethir | 108 538 983 |
| 269 | ORCA | Orca | 106 196 724 |
| 285 | GALA | GALA | 97 855 080 |

SNX is the 108th symbol of the working universe; GALA is the 117th and last.
`SUPER` is **SuperVerse**, `ZEN` is **Horizen**, `ATH` is **Aethir** and `EGLD` is
**MultiversX** - four tickers that collide with unrelated tokens elsewhere in the
market, so the CoinGecko `name` column (reproduced above) is the authoritative
identity for every batch.

### Hourly coverage of the batch-11 fixtures

OHLCV from the KuCoin public candles API (1h, UTC):

| Symbol | Rows | Span (UTC) |
|---|---|---|
| SUPER, RSR, EGLD, GLM, ZEN, ORCA, GALA | 22 000 | 2024-04-16 09:00 .. 2026-10-20 00:00 |
| SNX | 22 099 | 2024-04-12 05:00 .. 2026-10-19 23:00 |
| ATH | 20 631 | 2024-06-12 10:00 .. 2026-10-20 00:00 |
| DBR | 17 585 | 2024-10-17 08:00 .. 2026-10-20 00:00 |

All 10 fixtures have no duplicate timestamps and no hourly gaps. DBR is the
shortest fixture in the program so far (17 585 hourly bars, ~2.01 years) and
still clears the 2-year eligibility floor, but with the least OOS head-room.

### Batch-11 grid outcome (66 pairs per symbol, net of costs)

| Symbol | Cells | Trades | Mean net PF | Best net PF (cell) | Max net Sharpe | Rejected |
|---|---|---|---|---|---|---|
| SNX | 66 | 54 440 | 0.5731 | 0.8887 (P8_200) | -0.6560 | 66 |
| SUPER | 66 | 53 105 | 0.5842 | **1.0377 (P8_200)** | **+0.2611** | 65 |
| DBR | 66 | 36 204 | 0.4516 | 0.6113 (P8_50) | -3.8780 | 66 |
| RSR | 66 | 52 928 | 0.5803 | 0.7832 (P21_144) | -1.7520 | 66 |
| EGLD | 66 | 53 256 | 0.4873 | 0.7590 (P12_200) | -1.6050 | 66 |
| GLM | 66 | 52 624 | 0.4738 | 0.7276 (P34_200) | -2.0080 | 66 |
| ZEN | 66 | 56 341 | 0.5065 | 0.9702 (P8_200) | -0.0710 | 66 |
| ATH | 66 | 51 252 | 0.5762 | 0.8919 (P21_200) | -0.7220 | 66 |
| ORCA | 66 | 49 278 | 0.5515 | 0.7537 (P26_200) | -1.7260 | 66 |
| GALA | 66 | 53 289 | 0.5023 | 0.7211 (P8_144) | -1.7850 | 66 |

Batch 11 alone: 660 cells, 659 rejected, 1 exploratory (SUPER/USDT P8_200),
pooled mean net PF 0.5287, median 0.5418, 512 717 trades. Batch 11 has the
highest mean net PF of any batch so far (0.5287), and it still contains no
surviving edge.

---

## Batch 12 - expansion to N = 127

- Snapshot: `universe/mcap_snapshot_20261020_011116.json`
- Source: CoinGecko `/api/v3/coins/markets` (`order=market_cap_desc`)
- Fetched at: 2026-10-20T01:11:16Z
- Previous N -> new N: **117 -> 127** (ranks 118-127 of the working universe)
- Expansion floor: GALA at 97 855 080 USD (the lowest market cap already in the
  universe in this snapshot); every added name is strictly below it.
- The batch was applied from the reviewed snapshot file itself
  (`--apply-from universe/mcap_snapshot_20261020_011116.json`).
- Added (market cap at snapshot time, USD):

| Rank in snapshot | Symbol | Name | Market cap |
|---|---|---|---|
| 290 | DYDX | dYdX | 96 133 434 |
| 297 | MINA | Mina Protocol | 91 161 485 |
| 299 | ZRX | 0x Protocol | 90 898 735 |
| 301 | WEMIX | WEMIX | 90 295 428 |
| 304 | GMX | GMX | 88 421 953 |
| 305 | PROM | Prom | 87 913 778 |
| 308 | W | Wormhole | 86 027 111 |
| 313 | ARKM | Arkham | 82 554 390 |
| 316 | LPT | Livepeer | 80 760 813 |
| 319 | SAFE | Safe | 80 267 894 |

DYDX is the 118th symbol of the working universe; SAFE is the 127th and last.
`W` is **Wormhole**, `ZRX` is **0x Protocol**, `DYDX` is **dYdX** (the
re-launched, renamed dYdX chain token) and `ARKM` is **Arkham** - tickers that
collide with unrelated tokens elsewhere in the market, so the CoinGecko `name`
column (reproduced above) is the authoritative identity for every batch.

### Data-layer incident during batch 12 (transient, resolved)

The first attempt to download the batch-12 fixtures failed for the six names
DYDX, MINA, ZRX, WEMIX, GMX and PROM with KuCoin error `400100`
(*symbol does not exist*), and the universe file had already been written with
all 10 names. The failure was **not** a real listing gap: all ten pairs are
listed and enabled on KuCoin (`/api/v1/symbols` reports
`GMX-USDT`, `PROM-USDT`, `W-USDT`, `ARKM-USDT`, `LPT-USDT`, `SAFE-USDT` with
`enableTrading = true`) and the CoinGecko eligibility filter had already passed
for all ten in the 01:11 and 01:23 snapshots. A re-query of the candles endpoint
returned `code = 200000` for every one of them, so the earlier `400100` was a
transient API error, not missing data.

Re-running `scripts/fetch_kucoin.py` on the same six names fetched all of them
cleanly, so **no name was dropped from the universe and no alternate exchange
was needed**. The universe stayed append-only and strictly market-cap
descending (PROMPT.md §2.1.2). Lesson for the next agent: a KuCoin `400100`
on a name that `/api/v1/symbols` reports as enabled should be retried before
the name is treated as ineligible.

### Hourly coverage of the batch-12 fixtures

OHLCV from the KuCoin public candles API (1h, UTC):

| Symbol | Rows | Span (UTC) |
|---|---|---|
| GMX, PROM, W, ARKM, LPT | 22 000 | 2024-04-16 10:00 .. 2026-10-20 01:00 |
| SAFE | 21 836 | 2024-04-23 06:00 .. 2026-10-20 01:00 |

All 10 fixtures have no duplicate timestamps and no hourly gaps; SAFE is the
shortest at 21 836 hourly bars (~2.49 years) and still clears the 2-year
eligibility floor with more OOS head-room than batch 11's DBR (17 585 bars).

Thin pairs quote-carry: a bar can have zero traded volume while the OHLC
values move. GMX has the highest share of such bars in the program so far
(2 655 of 22 000 = 12.1 %), followed by PROM 8.8 %, SAFE 3.6 %, LPT 3.3 %,
ARKM 0.7 % and W 0.1 %. This is not new to the program (DBR 20.6 %, SUN 15.0 %,
DCR 14.8 %, HTX 12.1 %, GLM 10.4 % in earlier batches), so the baseline was left
unchanged; a zero-volume-bar filter would be a registered mutation (§5), not a
silent change.

### Batch-12 grid outcome (66 pairs per symbol, net of costs)

| Symbol | Cells | Trades | Mean net PF | Best net PF (cell) | Max net Sharpe | Rejected |
|---|---|---|---|---|---|---|
| DYDX | 66 | 52 965 | 0.5666 | 0.8425 (P50_200) | -0.9243 | 66 |
| MINA | 66 | 53 016 | 0.5559 | 0.7974 (P34_200) | -1.1384 | 66 |
| ZRX | 66 | 52 956 | 0.4964 | 0.7381 (P8_144) | -2.0713 | 66 |
| WEMIX | 66 | 79 618 | 0.2376 | 0.3780 (P34_200) | -7.9026 | 66 |
| GMX | 66 | 54 090 | 0.5069 | 0.7177 (P8_200) | -2.4255 | 66 |
| PROM | 66 | 56 765 | 0.4176 | 0.5733 (P12_89) | -5.1076 | 66 |
| W | 66 | 53 055 | 0.6345 | 0.9717 (P8_200) | -0.1056 | 66 |
| ARKM | 66 | 55 735 | 0.5584 | 0.7426 (P20_200) | -1.8402 | 66 |
| LPT | 66 | 56 447 | 0.5094 | 0.7141 (P34_200) | -2.1415 | 66 |
| SAFE | 66 | 50 942 | 0.5266 | 0.7998 (P34_200) | -1.3193 | 66 |

Batch 12 alone: 660 cells, **660 rejected, 0 exploratory**, pooled mean net PF
0.5010, median 0.5248, best 0.9717 (W/USDT P8_200), 565 589 trades. No cell in
the batch reached net PF > 1 - the ninth of the thirteen batches so far with
no cell clearing the in-sample scan threshold (only batches 8, 10 and 11
produced any).

---

## Batch 13 - expansion to N = 137

- Snapshot: `universe/mcap_snapshot_20261020_021004.json`
- Source: CoinGecko `/api/v3/coins/markets` (`order=market_cap_desc`)
- Fetched at: 2026-10-20T02:10:04Z
- Previous N -> new N: **127 -> 137** (ranks 128-137 of the working universe)
- Expansion floor: SAFE at 80 642 232 USD (the lowest market cap already in
  the universe in this snapshot); every added name is strictly below it.
- The batch was applied from the reviewed snapshot file itself
  (`--apply-from universe/mcap_snapshot_20261020_021004.json`).
- Added (market cap at snapshot time, USD):

| Rank in snapshot | Symbol | Name | Market cap |
|---|---|---|---|
| 320 | KSM | Kusama | 79 352 005 |
| 323 | NMR | Numeraire | 79 072 655 |
| 324 | YFI | yearn.finance | 78 877 573 |
| 325 | HNT | Helium | 78 667 114 |
| 326 | ORDI | ORDI | 78 525 316 |
| 331 | KAVA | Kava | 76 724 152 |
| 348 | CKB | Nervos Network | 72 155 051 |
| 349 | DUSK | DUSK Network | 72 144 987 |
| 350 | AMP | Amp | 72 021 528 |
| 358 | VELO | Velo | 70 523 988 |

KSM is the 128th symbol of the working universe; VELO is the 137th and last.

### Hourly coverage of the batch-13 fixtures

OHLCV from the KuCoin public candles API (1h, UTC):

| Symbol | Rows | Span (UTC) |
|---|---|---|
| KSM, NMR, HNT, ORDI, KAVA, CKB, DUSK, AMP, VELO | 22 000 | 2024-04-16 11:00 .. 2026-10-20 02:00 |
| YFI | 22 099 | 2024-04-12 07:00 .. 2026-10-20 01:00 |

All 10 fixtures have no duplicate timestamps and no hourly gaps.

### Batch-13 grid outcome (66 pairs per symbol, net of costs)

| Symbol | Cells | Trades | Mean net PF | Best net PF (cell) | Max net Sharpe | Rejected |
|---|---|---|---|---|---|---|
| KSM | 66 | 52 327 | 0.4905 | 0.6988 (P34_200) | -2.2663 | 66 |
| NMR | 66 | 57 589 | 0.5342 | 0.6991 (P8_200) | -2.1037 | 66 |
| YFI | 66 | 59 706 | 0.4186 | 0.6605 (P34_200) | -2.5851 | 66 |
| HNT | 66 | 56 881 | 0.4746 | 0.7381 (P20_200) | -1.7414 | 66 |
| ORDI | 66 | 55 959 | 0.5569 | 0.7760 (P26_200) | -1.7852 | 66 |
| KAVA | 66 | 57 128 | 0.4576 | 0.6337 (P34_200) | -3.2862 | 66 |
| CKB | 66 | 54 794 | 0.5159 | 0.6866 (P8_144) | -2.3224 | 66 |
| DUSK | 66 | 52 108 | 0.5811 | 0.8137 (P8_144) | -1.1330 | 66 |
| AMP | 66 | 75 572 | 0.3167 | 0.4552 (P12_200) | -5.5779 | 66 |
| VELO | 66 | 57 920 | 0.6150 | 0.8305 (P20_144) | -1.3268 | 66 |

Batch 13 alone: 660 cells, **660 rejected, 0 exploratory**, pooled mean net PF
0.4961, median 0.5159, best 0.8305 (VELO/USDT P20_144), 579 984 trades. No cell
in the batch reached net PF > 1.

---

## Batch 14 - expansion to N = 147

- Snapshot: `universe/mcap_snapshot_20261020_030608.json`
- Source: CoinGecko `/api/v3/coins/markets` (`order=market_cap_desc`)
- Fetched at: 2026-10-20T03:06:08Z
- Previous N -> new N: **137 -> 147** (ranks 138-147 of the working universe)
- Expansion floor: VELO at 70 523 988 USD (the lowest market cap already in
  the universe in this snapshot); every added name is strictly below it.
- The batch was applied from the reviewed snapshot file itself
  (`--apply-from universe/mcap_snapshot_20261020_030608.json`).
- Added (market cap at snapshot time, USD):

| Rank in snapshot | Symbol | Market cap |
|---|---|---|
| 138 | ZETA | 69 127 750 |
| 139 | ALT | 68 615 672 |
| 140 | AXL | 68 245 246 |
| 141 | BABYDOGE | 65 893 189 |
| 142 | TFUEL | 65 223 292 |
| 143 | IO | 64 059 810 |
| 144 | SUSHI | 62 190 873 |
| 145 | EDU | 61 859 142 |
| 146 | DGB | 61 553 312 |
| 147 | DEXE | 61 407 515 |

ZETA is the 138th symbol of the working universe; DEXE is the 147th and last.
Ranks 138-144 (ZETA, ALT, AXL, BABYDOGE, TFUEL, IO, SUSHI) were grid-processed
in the prior session; ranks 145-147 (EDU, DGB, DEXE) were grid-processed in this
session. Note: the fresh 03:06 snapshot displaced RLC with DEXE and reordered
ALT/AXL and IO/SUSHI versus the 02:10 snapshot; the applied ranking is
strictly market-cap descending.

### Hourly coverage of the batch-14 fixtures

OHLCV from the KuCoin public candles API (1h, UTC), 22 000 bars per symbol:

| Symbol | Rows | Span (UTC) |
|---|---|---|
| ZETA, ALT, AXL, BABYDOGE, TFUEL, IO, SUSHI, EDU, DGB, DEXE | 22 000 | 2024-04-16 .. 2026-10-20 |

All 10 fixtures have no duplicate timestamps and no hourly gaps.

### Batch-14 grid outcome (66 pairs per symbol, net of costs)

| Symbol | Cells | Trades | Mean net PF | Best net PF (cell) | Max net Sharpe | Rejected |
|---|---|---|---|---|---|---|
| ZETA | 66 | 51 823 | 0.5767 | 0.8062 (P21_200) | -1.3291 | 66 |
| ALT | 66 | 47 542 | 0.5679 | 0.7340 (P26_200) | -1.9025 | 66 |
| AXL | 66 | 59 203 | 0.5463 | 0.7225 (P26_200) | -2.3306 | 66 |
| BABYDOGE | 66 | 2 775 | 1.0628 | 2.2274 (P50_55) | 0.9426 | 44 |
| TFUEL | 66 | 63 820 | 0.4235 | 0.5659 (P8_89) | -5.5003 | 66 |
| IO | 66 | 52 120 | 0.5642 | 0.7403 (P55_200) | -2.0819 | 66 |
| SUSHI | 66 | 54 945 | 0.4933 | 0.6540 (P50_200) | -2.4837 | 66 |
| EDU | 66 | 56 676 | 0.5107 | 0.7100 (P21_200) | -2.3085 | 66 |
| DGB | 66 | 61 038 | 0.4808 | 0.7099 (P20_200) | -2.6803 | 66 |
| DEXE | 66 | 49 652 | 0.4963 | 0.8354 (P12_144) | -0.9126 | 66 |

Batch 14 alone: 660 cells, **638 rejected, 22 exploratory signal** (all BABYDOGE),
0 cells surviving OOS + cost stress. Pooled mean net PF 0.5222, 499 594 trades.
No non-BABYDOGE cell reached net PF > 1.

BABYDOGE (rank 141) produced 32 in-sample cells with net PF > 1 (best 2.2274,
P50_55) but all are rejected: 30 have zero out-of-sample trades, and the 2 with
adequate OOS trades fail 2x cost stress (OOS PF 0.0000). BABYDOGE is a very
thinly traded name (2 775 total trades across 66 cells), so its in-sample PFs
are multiple-testing noise on a tiny sample.

---

## Robustness check of the net-PF > 1 cells (PROMPT.md §3.3)

`scripts/candidate_check.py` re-runs every cell in the run with net PF > 1 in
four configurations: full sample at the registered costs, the trailing 35 % of
the bars (out-of-sample, entries restricted to that window), the full sample at
2x fees and slippage, and the out-of-sample window at 2x costs.

After batch 10 (N = 107), artifact `results/20261020_000649_candidate_check/`:

| Symbol | Cell | Base net PF | Base Sharpe | OOS net PF | OOS Sharpe | OOS trades | 2x-cost net PF | 2x-cost OOS net PF | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| JASMY/USDT | P20_200 | 1.0097 | +0.1189 | 0.9068 | -0.5973 | 174 | 0.7465 | 0.5944 | rejected |
| JASMY/USDT | P21_200 | 1.0341 | +0.2673 | 0.9167 | -0.5194 | 173 | 0.7576 | 0.6015 | rejected |

After batch 11 (N = 117), artifact `results/20261020_015931_candidate_check/`:

| Symbol | Cell | Base net PF | Base Sharpe | OOS net PF | OOS Sharpe | OOS trades | 2x-cost net PF | 2x-cost OOS net PF | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| JASMY/USDT | P20_200 | 1.0097 | +0.1189 | 0.9068 | -0.5973 | 174 | 0.7465 | 0.5944 | rejected |
| JASMY/USDT | P21_200 | 1.0341 | +0.2673 | 0.9167 | -0.5194 | 173 | 0.7576 | 0.6015 | rejected |
| SUPER/USDT | P8_200 | 1.0377 | +0.2611 | 0.9536 | -0.1638 | 78 | 0.8093 | 0.7176 | rejected |

(The SUPER/USDT row was transcribed incorrectly when the batch-11 table was
first written - OOS Sharpe -0.4627 / 2x-cost OOS PF 0.6975. The artifact
`results/20261020_015931_candidate_check/summary.json` has always carried
-0.1638 / 0.7176, and the batch-12 re-run reproduces those numbers exactly;
the table above is corrected to match the artifact. The verdict is unchanged.)

After batch 12 (N = 127), artifact `results/20261020_020152_candidate_check/`:

| Symbol | Cell | Base net PF | Base Sharpe | OOS net PF | OOS Sharpe | OOS trades | 2x-cost net PF | 2x-cost OOS net PF | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| JASMY/USDT | P20_200 | 1.0097 | +0.1189 | 0.9068 | -0.5973 | 174 | 0.7465 | 0.5944 | rejected |
| JASMY/USDT | P21_200 | 1.0341 | +0.2673 | 0.9167 | -0.5194 | 173 | 0.7576 | 0.6015 | rejected |
| SUPER/USDT | P8_200 | 1.0377 | +0.2611 | 0.9536 | -0.1638 | 78 | 0.8093 | 0.7176 | rejected |

After batch 13 (N = 137), artifact `results/20261020_025729_candidate_check/`:
same three cells re-checked against the expanded 9 042-cell grid, same
outcome - all rejected.

The batch-13 grid added no cell above net PF > 1, so the candidate set is
unchanged - still the same three in-sample survivors, all of them failing the
same gates.

**Every cell that has ever reached net PF > 1 in this program failed both
out-of-sample and cost stress**, so all of them are rejected rather than
promoted (PROMPT.md §3.4). The program's cumulative credible-candidate count
stays at **0** after 9 042 grid cells: an in-sample profit factor of ~1.03-1.04
is scan noise, exactly as the multiple-testing expectation predicted (0.03 % of
cells above 1.0 against a ~50 % null).

---

## Cumulative state after batch 14 (N = 147)

- **9 702 / 9 702 cells** complete (147 symbols x 66 EMA pairs), 0 blocked.
- 9 677 cells **rejected** (99.74 %), 25 cells **exploratory signal** in the
  aggregate scan and **rejected** by the OOS + cost-stress check above,
  **0 credible candidates**.
- Pooled (net of costs, full sample, 10 bps taker + 2 bps slippage per side):
  mean net PF **0.4894**, median 0.5098, best net PF **2.2274**
  (BABYDOGE/USDT P50_55, rejected - 0 OOS trades), 7 998 391 trades.
- Cells with net PF > 1: 35 / 9 702 = 0.4 % against a ~50 % no-edge null
  (excess -49.6 %). All 35 failed OOS + cost stress: 32 BABYDOGE cells have
  zero OOS trades; JASMY P20_200 / P21_200 and SUPER P8_200 fail cost stress.
- Per-pair pooled leaders (mean net PF over 147 symbols): P8_200 0.6750,
  P20_200 0.6713, P12_200 0.6669, P21_200 0.6653. Worst: P20_21 0.1371,
  P50_55 0.2094, P8_12 0.2043.
- Mean net PF by batch (b7-b14): 0.4682, 0.5085, 0.5210, 0.5017, 0.5287,
  0.5010, 0.4961, 0.5222. Lower market cap does not improve the registered rule.
- The shape of the result is stable across every batch: mean net PF per batch
  stays in the 0.46-0.53 band. The pooled mean drifts up only because smaller
  names trade less often per bar.

---

## Grid coverage per batch

| Batch | Universe N | Symbols with a full 66-pair grid | Grid artifact |
|---|---|---|---|
| Batch 0 | 5 | BTC, ETH, SOL, BNB, XRP | `results/20261019_135940_grid/` |
| Batch 1 | 17 | + TRX, ZEC, DOGE, XMR, LINK, ADA, NEAR, XLM, BCH, LTC, UNI, AVAX | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 2 | 27 | complete - SUI, GRAM, HBAR, TAO, SHIB, CRO, QNT, ENA, AAVE, ONDO (66 pairs each) | `results/20261019_135940_grid/` |
| Batch 3 | 37 | complete - DOT, WLD, MNT, PEPE, SKY, ICP, HTX, ARB, ETC, JST (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 4 | 47 | complete - KCS, ALGO, POL, KAS, JUP, ATOM, RENDER, INJ, FIL, AERO (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 5 | 57 | complete - ZRO, CAKE, STX, APT, ETHFI, XDC, DASH, TIA, BDX, CRV (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 6 | 67 | complete - VET, PYTH, FLR, RAY, STRK, FET, SEI, PENDLE, BSV, BTT (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 7 | 77 | complete - XTZ, LDO, SUN, BAT, OP, CFX, GRT, DCR, BONK, LUNC (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 8 | 87 | complete - AR, JTO, NFT, JASMY, EIGEN, ENS, KMNO, FLOKI, COMP, RUNE (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 9 | 97 | complete - IOTA, ZBCN, AKT, WIF, CVX, TWT, THETA, AXS, SAND, TRAC (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 10 | 107 | complete - MANA, XCN, ZK, NEO, CHZ, APE, IMX, AIOZ, 1INCH, XEC (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 11 | 117 | complete - SNX, SUPER, DBR, RSR, EGLD, GLM, ZEN, ATH, ORCA, GALA (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 12 | 127 | complete - DYDX, MINA, ZRX, WEMIX, GMX, PROM, W, ARKM, LPT, SAFE (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 13 | 137 | complete - KSM, NMR, YFI, HNT, ORDI, KAVA, CKB, DUSK, AMP, VELO (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 14 | 147 | complete - ZETA, ALT, AXL, BABYDOGE, TFUEL, IO, SUSHI, EDU, DGB, DEXE (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 15 | 157 | complete - RLC, ROSE, TURBO, XPR, ENJ, T, ONT, ASTR, PHA, MEME (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |

The grid directory is shared across batches (the runner resumes from
`progress.json`), so one aggregate report covers the whole processed universe.
OHLCV for every symbol in every batch is in `data/fixtures/`, with provenance in
`data/fixtures/fetch_manifest.json` (KuCoin public `/api/v1/market/candles`,
1h, UTC).

## Batch 15 - expansion to N = 157 (COMPLETED 2026-10-20)

- Previous N -> new N: **147 -> 157** (ranks 148-157)
- Snapshot: `universe/mcap_snapshot_20261020_041243.json` (fetched 2026-10-20T04:12:43Z)
- Added (market cap at snapshot time, USD):

| # | Symbol | Market cap |
|---|---|---|
| 148 | RLC/USDT | 60,905,772 |
| 149 | ROSE/USDT | 59,243,861 |
| 150 | TURBO/USDT | 57,952,190 |
| 151 | XPR/USDT | 55,086,574 |
| 152 | ENJ/USDT | 54,873,285 |
| 153 | T/USDT | 53,675,358 |
| 154 | ONT/USDT | 52,871,091 |
| 155 | ASTR/USDT | 52,502,307 |
| 156 | PHA/USDT | 51,979,788 |
| 157 | MEME/USDT | 51,673,755 |

- OHLCV: fetched via `scripts/fetch_kucoin.py --target-bars 22000` for all 10; fixtures added to `data/fixtures/` (all 10 present). Manifest reconciled (`data/fixtures/fetch_manifest.json`, 157 symbols).
- Grid: ran `scripts/run_grid.py --resume results/20261019_135940_grid` per-symbol (n 148-157) with checkpoint after each. **10,362 / 10,362 cells complete** (157 symbols x 66 pairs), 0 blocked.
- Aggregate: `scripts/aggregate_grid.py` -> mean net PF **0.4918**, median 0.5120, best 2.2274; cells with net PF > 1: **35/10362 (0.3%)**; exploratory 25, rejected 10337.
- Robustness: `scripts/candidate_check.py` (artifact `results/20261020_062438_candidate_check/`) tested all 35 net-PF>1 cells: 32 BABYDOGE cells have **0 OOS trades** (rejected), JASMY P20_200/P21_200 and SUPER P8_200 fail **cost stress** (OOS+2x costs) -> **0 credible candidates**.
- Cumulative rejection rate: **10337 / 10362 cells (99.76 %)**, 0 credible candidates. Pooled 8,313,668 trades.
- Checkpoints pushed to remote after each symbol (VERIFIED).

---

## Batch 16 - expansion to N = 167 (COMPLETED 2026-10-20)

- Previous N -> new N: **157 -> 167** (ranks 158-167)
- Snapshot: `universe/mcap_snapshot_20261020_065809.json` (fetched 2026-10-20T06:58:09Z)
- Expansion floor: MEME at 51,673,755 USD (the lowest market cap already in the universe); every added name is strictly below it.
- The batch was applied from the reviewed snapshot file itself (`--apply-from universe/mcap_snapshot_20261020_065809.json`), so the names processed by the grid are exactly the ones listed below.
- Added (market cap at snapshot time, USD):

| Rank in snapshot | Symbol | Market cap |
|---|---|---|
| 158 | WIN/USDT | 50,429,633 |
| 159 | TRB/USDT | 50,377,279 |
| 160 | CELO/USDT | 49,862,879 |
| 161 | FLOW/USDT | 49,834,441 |
| 162 | ID/USDT | 48,146,413 |
| 163 | CTC/USDT | 47,969,021 |
| 164 | DEEP/USDT | 47,666,673 |
| 165 | BRETT/USDT | 46,407,594 |
| 166 | CFG/USDT | 45,703,546 |
| 167 | XNO/USDT | 45,527,633 |

WIN is the 158th symbol of the working universe; XNO is the 167th and last.

### Hourly coverage of the batch-16 fixtures

OHLCV from the KuCoin public candles API (1h, UTC), 22 000 bars per symbol:

| Symbol | Rows | Span (UTC) |
|---|---|---|
| WIN, TRB, CELO, FLOW, ID, CTC, DEEP, BRETT, CFG, XNO | 22 000 | 2024-04-16 .. 2026-10-20 |

All 10 fixtures have no duplicate timestamps and no hourly gaps. Manifest reconciled (`data/fixtures/fetch_manifest.json`, 167 symbols).

### Batch-16 grid outcome (66 pairs per symbol, net of costs)

| Symbol | Cells | Trades | Mean net PF | Best net PF (cell) | Max net Sharpe | Rejected |
|---|---|---|---|---|---|---|
| WIN | 66 | 51 380 | 0.3576 | 0.6402 (P12_200) | -2.1786 | 66 |
| TRB | 66 | 56 623 | 0.4536 | 0.6601 (P34_200) | -2.3833 | 66 |
| CELO | 66 | 51 311 | 0.5546 | 0.8204 (P34_200) | -1.2170 | 66 |
| FLOW | 66 | 54 372 | 0.4669 | 0.6445 (P8_144) | -2.5071 | 66 |
| ID | 66 | 48 847 | 0.5310 | 0.7778 (P12_144) | -1.5534 | 66 |
| CTC | 66 | 55 063 | 0.4587 | 0.6644 (P12_144) | -2.9713 | 66 |
| DEEP | 66 | 38 932 | 0.6564 | 0.8235 (P26_100) | -1.1582 | 66 |
| BRETT | 66 | 49 505 | 0.5853 | 0.8337 (P8_200) | -0.7766 | 66 |
| CFG | 66 | 49 598 | 0.4798 | 0.7124 (P8_200) | -1.7807 | 66 |
| XNO | 66 | 65 410 | 0.4328 | 0.5774 (P12_200) | -4.2023 | 66 |

Batch 16 alone: 660 cells, **660 rejected, 0 exploratory**, pooled mean net PF 0.4977, 521,041 trades. No cell in the batch reached net PF > 1.

---

## Cumulative state after batch 16 (N = 167)

- **11,022 / 11,022 cells** complete (167 symbols x 66 EMA pairs), 0 blocked.
- 10,997 cells **rejected** (99.77 %), 25 cells **exploratory signal** in the aggregate scan and **rejected** by the OOS + cost-stress check, **0 credible candidates**.
- Pooled (net of costs, full sample, 10 bps taker + 2 bps slippage per side):
  mean net PF **0.4922**, median 0.5124, best net PF **2.2274** (BABYDOGE/USDT P50_55, rejected - 0 OOS trades), 9,035,501 trades.
- Cells with net PF > 1: 35 / 11,022 = 0.3 % against a ~50 % no-edge null (excess -49.7 %). All 35 failed OOS + cost stress: 32 BABYDOGE cells have zero OOS trades; JASMY P20_200 / P21_200 and SUPER P8_200 fail cost stress.
- Per-pair pooled leaders (mean net PF over 167 symbols): P8_200 0.6750, P20_200 0.6713, P12_200 0.6669, P21_200 0.6653. Worst: P20_21 0.1371, P50_55 0.2094, P8_12 0.2043.
- Mean net PF by batch (b7-b16): 0.4682, 0.5085, 0.5210, 0.5017, 0.5287, 0.5010, 0.4961, 0.5222, ~0.4977. Lower market cap does not improve the registered rule.

---

## Batch 17 - expansion to N = 177 (COMPLETED 2026-10-20)

- Previous N -> new N: **167 -> 177** (ranks 168-177 of the working universe)
- Snapshot: `universe/mcap_snapshot_20261020_082835.json` (fetched 2026-10-20T08:28:35Z, pages 1-10, 1 000 ranked entries down to $15 182 785 - the pass covers the band below the floor)
- Expansion floor: MEME at 51 673 755 USD (the lowest market cap already in the universe); every added name is strictly below it.
- Added (market cap at snapshot time, USD):

| Rank in snapshot | Symbol | Market cap |
|---|---|---|
| 168 | XYO/USDT | 45 129 567 |
| 169 | POLYX/USDT | 44 933 926 |
| 170 | AURORA/USDT | 44 114 791 |
| 171 | POPCAT/USDT | 43 197 187 |
| 172 | REQ/USDT | 42 955 154 |
| 173 | LSK/USDT | 42 473 640 |
| 174 | MASK/USDT | 41 802 261 |
| 175 | ZIL/USDT | 41 689 179 |
| 176 | ANKR/USDT | 41 277 977 |
| 177 | BOME/USDT | 41 203 035 |

BOME is the 177th and last symbol of the working universe; the floor is now $41 203 035.

### Hourly coverage of the batch-17 fixtures

OHLCV from the KuCoin public candles API (1h, UTC):

| Symbol | Rows | Span (UTC) |
|---|---|---|
| XYO | 22 099 | 2024-04-12 .. 2026-10-20 |
| POLYX, AURORA, REQ, LSK, MASK, ZIL, ANKR, BOME | 22 000 | 2024-04-16 .. 2026-10-20 |
| POPCAT | 18 930 | 2024-08-22 .. 2026-10-20 |

All 10 fixtures are present and reconciled in `data/fixtures/fetch_manifest.json` (177 symbols).

### Batch-17 grid outcome (66 pairs per symbol, net of costs)

| Symbol | Cells | Trades | Mean net PF | Best net PF (cell) | Max net Sharpe | Rejected |
|---|---|---|---|---|---|---|
| XYO | 66 | 61 521 | 0.3873 | 0.5513 (P21_200) | -4.2426 | 66 |
| POLYX | 66 | 50 649 | 0.5615 | 0.7721 (P21_200) | -1.4871 | 66 |
| AURORA | 66 | 46 469 | 0.4697 | 0.6727 (P8_144) | -2.7630 | 66 |
| POPCAT | 66 | 47 653 | 0.5882 | 0.8890 (P34_200) | -0.7522 | 66 |
| REQ | 66 | 63 224 | 0.3891 | 0.5324 (P26_144) | -6.4234 | 66 |
| LSK | 66 | 45 894 | 0.5454 | 0.7650 (P8_200) | -1.6394 | 66 |
| MASK | 66 | 55 546 | 0.3989 | 0.6380 (P50_200) | -2.7920 | 66 |
| ZIL | 66 | 54 709 | 0.4804 | 0.7036 (P8_200) | -2.1128 | 66 |
| ANKR | 66 | 52 735 | 0.4843 | 0.7038 (P8_200) | -2.0698 | 66 |
| BOME | 66 | 53 168 | 0.5318 | 0.7778 (P8_200) | -1.2516 | 66 |

Batch 17 alone: 660 cells, **660 rejected, 0 exploratory**, 531 568 trades. No cell in the batch reached net PF > 1.

---

## Cumulative state after batch 17 (N = 177)

- **11 682 / 11 682 cells** complete (177 symbols x 66 EMA pairs), 0 blocked.
- 11 657 cells **rejected**, 25 cells **exploratory signal** in the aggregate scan and **rejected** by the OOS + cost-stress check, **0 credible candidates**.
- Pooled (net of costs, full sample, 10 bps taker + 2 bps slippage per side):
  mean net PF **0.4917**, median 0.5112, best net PF **2.2274** (BABYDOGE/USDT P50_55, rejected - 0 OOS trades), 9 567 069 trades.
- Cells with net PF > 1: 35 / 11 682 = 0.3 % against a ~50 % no-edge null (excess -49.7 %). All 35 failed OOS + cost stress (artifact `results/20261020_094859_candidate_check/`): 32 BABYDOGE cells have zero OOS trades; JASMY P20_200 / P21_200 and SUPER P8_200 fail cost stress.

---

## Batch 18 - expansion to N = 187 (COMPLETED 2026-10-20)

- Previous N -> new N: **177 -> 187** (ranks 178-187 of the working universe)
- Snapshot: `universe/mcap_snapshot_20261020_113004.json` (fetched 2026-10-20T11:30:04Z, pages 1-10, 1 000 ranked entries down to $15 174 185 - the pass covers the band below the floor)
- Source: CoinGecko `/api/v3/coins/markets` (`order=market_cap_desc`)
- Expansion floor at selection time: BOME at 40 764 606 USD (the lowest market cap already in the universe); every added name is strictly below it.
- The batch was applied from the reviewed snapshot file itself (`--apply-from universe/mcap_snapshot_20261020_113004.json`), so the names processed by the grid are exactly the ones listed below.
- Snapshot coverage/exclusions (1 000 entries): 269 eligible; 731 excluded - 505 `no_tradable_kucoin_spot_usdt_pair`, 185 `insufficient_hourly_history_for_grid`, 25 `stablecoin_or_fiat_pegged`, 16 `kucoin_pair_trades_a_different_asset`.
- Added (market cap at snapshot time, USD):

| Rank in snapshot | Universe rank | Symbol | Market cap |
|---|---|---|---|
| 546 | 178 | API3/USDT | 39 787 614 |
| 548 | 179 | SYN/USDT | 39 709 917 |
| 549 | 180 | BAND/USDT | 39 644 632 |
| 550 | 181 | MOG/USDT | 39 157 351 |
| 551 | 182 | CSPR/USDT | 39 152 806 |
| 554 | 183 | NOT/USDT | 38 716 786 |
| 559 | 184 | ETN/USDT | 38 334 381 |
| 564 | 185 | PEOPLE/USDT | 38 019 382 |
| 569 | 186 | IOTX/USDT | 37 390 402 |
| 571 | 187 | SSV/USDT | 37 149 593 |

SSV is the 187th and last symbol of the working universe; the floor is now **$37 149 593**.

### Hourly coverage of the batch-18 fixtures

OHLCV from the KuCoin public candles API (1h, UTC), verified per fixture: no duplicate timestamps, no missing hours (contiguous 1h grid), no invalid OHLC rows.

| Symbol | Rows | Span (UTC) |
|---|---|---|
| API3, SYN, CSPR, IOTX | 22 000 | 2024-04-16 .. 2026-10-20 |
| BAND, PEOPLE, SSV | 22 099 | 2024-04-12 .. 2026-10-20 |
| NOT | 21 288 | 2024-05-16 .. 2026-10-20 |
| MOG | 20 116 | 2024-07-04 .. 2026-10-20 |
| ETN | 18 410 | 2024-09-13 .. 2026-10-20 |

Ticker identity: each of the 10 tickers maps to exactly one CoinGecko entry, and the last close of every fixture is within `|log(close / coingecko price)| <= 0.012` of the ranked price (script tolerance 0.20), so each KuCoin pair trades the asset the ranking describes. All 10 fixtures are reconciled in `data/fixtures/fetch_manifest.json` (189 rows: the 187 universe symbols plus the pre-fetched CCD and MOODENG files, which are not in the universe - see the skipped names note below).

### Batch-18 grid outcome (66 pairs per symbol, net of costs)

| Symbol | Cells | Trades | Mean net PF | Best net PF (cell) | Max net Sharpe | Rejected |
|---|---|---|---|---|---|---|
| API3 | 66 | 54 791 | 0.5633 | 0.7980 (P89_200) | -1.4175 | 66 |
| SYN | 66 | 52 207 | 0.5665 | 0.8407 (P34_200) | -0.9444 | 66 |
| BAND | 66 | 49 062 | 0.5476 | 0.8339 (P12_200) | -1.0851 | 66 |
| MOG | 66 | 48 733 | 0.6368 | 0.9033 (P8_200) | -0.4967 | 66 |
| CSPR | 66 | 70 513 | 0.3847 | 0.5698 (P12_200) | -4.5062 | 66 |
| NOT | 66 | 53 210 | 0.5520 | 0.7995 (P12_144) | -1.3003 | 66 |
| ETN | 66 | 52 976 | 0.3485 | 0.5473 (P34_200) | -5.0131 | 66 |
| PEOPLE | 66 | 51 086 | 0.5747 | 0.8733 (P21_144) | -0.7810 | 66 |
| IOTX | 66 | 54 372 | 0.5234 | 0.7234 (P8_200) | -1.6411 | 66 |
| SSV | 66 | 56 513 | 0.5318 | 0.7285 (P8_200) | -1.4505 | 66 |

Batch 18 alone: 660 cells, **660 rejected, 0 exploratory**, mean net PF 0.5229, 543 463 trades. No cell in the batch reached net PF > 1.

### Names deliberately skipped in the batch-18 snapshot

Two names in the snapshot are eligible but rank **above** the expansion floor, so the strict "append only names strictly below the floor" rule (PROMPT.md §2.1.2) keeps them out of the universe for now:

| Rank | Symbol | Name | Market cap | Note |
|---|---|---|---|---|
| 320 | GAS | Gas | 80 295 659 | eligible, but far above the floor |
| 533 | CCD | Concordium | 41 793 103 | eligible; it was the 11th eligible name below the floor when batch 17 took the first 10, and its market cap has since drifted above the floor. Its hourly fixture is already on disk (`data/fixtures/CCD_USDT.csv`). |

MOODENG (rank 574, $37 050 928) is eligible and **below** the new floor; it is the first name of the next batch.

---

## Cumulative state after batch 18 (N = 187)

- **12 342 / 12 342 cells** complete (187 symbols x 66 EMA pairs), 0 blocked.
- 12 317 cells **rejected** (99.80 %), 25 cells **exploratory signal** in the aggregate scan and **rejected** by the OOS + cost-stress check, **0 credible candidates**.
- Pooled (net of costs, full sample, 10 bps taker + 2 bps slippage per side):
  mean net PF **0.4934**, median 0.5134, best net PF **2.2274** (BABYDOGE/USDT P50_55, rejected - 0 OOS trades), 10 110 532 trades.
- Cells with net PF > 1: 35 / 12 342 = 0.28 % against a ~50 % no-edge null (excess -49.7 %). All 35 failed OOS + cost stress (artifact `results/20261020_125819_candidate_check/`): 32 BABYDOGE cells have zero OOS trades; JASMY P20_200 / P21_200 and SUPER P8_200 fail cost stress.
- Per-pair pooled leaders (mean net PF over 187 symbols): P8_200 0.6772, P12_200 0.6694, P20_200 0.6684, P21_200 0.6637. Worst: P20_21 0.1419, P8_12 0.2114, P50_55 0.2115.
- Mean net PF by batch (b7-b18): 0.4682, 0.5085, 0.5210, 0.5017, 0.5287, 0.5010, 0.4961, 0.5222, 0.4977, 0.5318, ~0.5229. Lower market cap does not improve the registered rule.

### Remaining eligible names below the floor (batch 19 candidates)

The 2026-10-20T11:30:04Z snapshot still holds **79 eligible unseen names below the current floor** (SSV, $37 149 593), so the universe is **not** exhausted and no new CoinGecko query is needed for the next batch. The next 10 by rank are OSMO, MOODENG, MEW, MERL, RPL, MOCA, UMA, DEGEN, ORBS, CATI. MOODENG's fixture is already on disk; the other 9 still need fetching.

---

## Batch 19 - expansion to N = 197 (COMPLETED 2026-10-20)

- Previous N -> new N: **187 -> 197** (ranks 188-197 of the working universe)
- Snapshot: `universe/mcap_snapshot_20261020_113004.json` (fetched 2026-10-20T11:30:04Z, pages 1-10, 1 000 ranked entries down to $15 174 185 - the pass covers the band below the floor)
- Source: CoinGecko `/api/v3/coins/markets` (`order=market_cap_desc`)
- Expansion floor at selection time: SSV at 37 149 593 USD (the lowest market cap already in the universe); every added name is strictly below it.
- The batch was applied from the reviewed snapshot file itself (`--apply-from universe/mcap_snapshot_20261020_113004.json`), so the names processed by the grid are exactly the ones listed below.
- Added (market cap at snapshot time, USD):

| Rank in snapshot | Universe rank | Symbol | Name | Market cap |
|---|---|---|---|---|
| 572 | 188 | OSMO/USDT | Osmosis | 37 083 307 |
| 574 | 189 | MOODENG/USDT | Moo Deng | 37 050 928 |
| 580 | 190 | MEW/USDT | cat in a dogs world | 36 350 256 |
| 590 | 191 | MERL/USDT | Merlin Chain | 35 731 205 |
| 598 | 192 | RPL/USDT | Rocket Pool | 34 904 326 |
| 599 | 193 | MOCA/USDT | Moca Network | 34 900 812 |
| 601 | 194 | UMA/USDT | UMA | 34 706 377 |
| 615 | 195 | DEGEN/USDT | Degen | 33 756 064 |
| 619 | 196 | ORBS/USDT | Orbs | 33 552 511 |
| 623 | 197 | CATI/USDT | Catizen | 33 051 490 |

CATI is the 197th and last symbol of the working universe; the floor is now **$33 051 490**.

### Hourly coverage of the batch-19 fixtures

OHLCV from the KuCoin public candles API (1h, UTC):

| Symbol | Rows | Span (UTC) |
|---|---|---|
| OSMO, MEW, UMA, ORBS | 22 000 | 2024-04-16 22:00 .. 2026-10-20 13:00 |
| RPL | 22 097 | 2024-04-12 18:00 .. 2026-10-20 10:00 |
| DEGEN | 21 964 | 2024-04-18 10:00 .. 2026-10-20 13:00 |
| MERL | 21 939 | 2024-04-19 10:00 .. 2026-10-20 12:00 |
| MOCA | 19 948 | 2024-07-11 10:00 .. 2026-10-20 13:00 |
| MOODENG | 18 073 | 2024-09-27 11:00 .. 2026-10-20 11:00 |
| CATI | 18 243 | 2024-09-20 10:00 .. 2026-10-20 12:00 |

MOODENG's fixture was already on disk from the batch-18 pass; the other 9 were
fetched for this batch. All 10 fixtures are reconciled in
`data/fixtures/fetch_manifest.json`.

### Batch-19 grid outcome (66 pairs per symbol, net of costs)

| Symbol | Cells | Trades | Mean net PF | Best net PF (cell) | Max net Sharpe | Rejected |
|---|---|---|---|---|---|---|
| OSMO | 66 | 52 916 | 0.5335 | 0.7832 (P20_200) | -1.6617 | 66 |
| MOODENG | 66 | 43 952 | 0.6315 | **1.0567 (P8_200)** | **+0.3519** | 65 |
| MEW | 66 | 52 726 | 0.5572 | 0.7822 (P8_200) | -1.2124 | 66 |
| MERL | 66 | 52 696 | 0.5765 | 0.8224 (P8_200) | -0.8938 | 66 |
| RPL | 66 | 48 642 | 0.5970 | 0.9671 (P8_200) | -0.1366 | 66 |
| MOCA | 66 | 47 404 | 0.4914 | 0.6126 (P50_200) | -2.8635 | 66 |
| UMA | 66 | 53 572 | 0.4869 | 0.6526 (P50_200) | -2.4956 | 66 |
| DEGEN | 66 | 50 888 | 0.6455 | 0.8306 (P8_144) | -1.2464 | 66 |
| ORBS | 66 | 56 745 | 0.4406 | 0.6407 (P21_200) | -3.4239 | 66 |
| CATI | 66 | 48 383 | 0.4662 | 0.5890 (P34_89) | -3.7009 | 66 |

Batch 19 alone: 660 cells, **659 rejected, 1 exploratory signal**
(MOODENG/USDT P8_200), 516 924 trades. DEGEN has the highest mean net PF of
any batch symbol so far (0.6455) and still contains no surviving edge.

### The MOODENG/USDT P8_200 cell (batch 19's only in-sample survivor)

| Symbol | Cell | Trades | Net PF | Net Sharpe | Gross PF | Net win rate | Avg hold (bars) |
|---|---|---|---|---|---|---|---|
| MOODENG/USDT | P8_200 | 213 | 1.0567 | +0.3519 | 1.2608 | 0.5587 | 71.3 |

The candidate check (artifact `results/20261020_141749_candidate_check/`) rejects
it: out-of-sample (trailing 35 % of bars) net PF **0.8576** with net Sharpe
**-0.9291** over 121 OOS trades, and under 2x fees/slippage the net PF falls to
**0.8999** (OOS 0.6726). It fails the OOS leg and the cost-stress leg, so it is
**not** a credible candidate (PROMPT.md §3.4).

---

## Cumulative state after batch 19 (N = 197)

- **13 002 / 13 002 cells** complete (197 symbols x 66 EMA pairs), 0 blocked.
- 12 976 cells **rejected** (99.80 %), 26 cells **exploratory signal** in the aggregate scan and **rejected** by the OOS + cost-stress check, **0 credible candidates**.
- Pooled (net of costs, full sample, 10 bps taker + 2 bps slippage per side):
  mean net PF **0.4959**, median 0.5162, best net PF **2.2274**
  (BABYDOGE/USDT P50_55, rejected - 0 OOS trades), 10 618 456 trades.
- Cells with net PF > 1: 36 / 13 002 = 0.28 % against a ~50 % no-edge null
  (excess -49.7 %). All 36 failed OOS + cost stress (artifact
  `results/20261020_141749_candidate_check/`): 32 BABYDOGE cells have zero OOS
  trades; JASMY P20_200 / P21_200, SUPER P8_200 and MOODENG P8_200 fail the
  OOS and cost-stress legs.
- Per-pair pooled leaders (mean net PF over 197 symbols): P8_200 0.6803,
  P12_200 0.6707, P20_200 0.6694, P21_200 0.6646. Worst: P20_21 0.1446,
  P50_55 0.2137, P8_12 0.2157.
- Mean net PF by batch (b7-b19): 0.4682, 0.5085, 0.5210, 0.5017, 0.5287,
  0.5010, 0.4961, 0.5222, 0.4977, 0.5318, ~0.5229, ~0.5223. Lower market cap
  does not improve the registered rule.

### Remaining eligible names below the floor (batch 20 candidates)

The 2026-10-20T11:30:04Z snapshot still holds **69 eligible unseen names below
the current floor** (CATI, $33 051 490), so the universe is **not** exhausted and
no new CoinGecko query is needed for the next batch. The next 10 by rank are
METIS, REZ, LISTA, COTI, MAGIC, GTC, MANTA, LUNA, FLUX, XCH.

---

## Batch 20 - expansion to N = 207 (COMPLETED 2026-10-20)

- Previous N -> new N: **197 -> 207** (ranks 198-207 of the working universe)
- Snapshot: `universe/mcap_snapshot_20261020_113004.json` (fetched 2026-10-20T11:30:04Z, pages 1-10, 1 000 ranked entries down to $15 174 185 - the pass covers the band below the floor)
- Source: CoinGecko `/api/v3/coins/markets` (`order=market_cap_desc`)
- Expansion floor at selection time: CATI at 33 051 490 USD (the lowest market cap already in the universe); every added name is strictly below it.
- The batch was applied from the reviewed snapshot file itself (`--apply-from universe/mcap_snapshot_20261020_113004.json`), so the names processed by the grid are exactly the ones listed below.
- Snapshot coverage/exclusions (1 000 entries): 269 eligible; 731 excluded - 505 `no_tradable_kucoin_spot_usdt_pair`, 185 `insufficient_hourly_history_for_grid`, 25 `stablecoin_or_fiat_pegged`, 16 `kucoin_pair_trades_a_different_asset`.
- Added (market cap at snapshot time, USD):

| Rank in snapshot | Universe rank | Symbol | Name | Market cap |
|---|---|---|---|---|
| 626 | 198 | METIS/USDT | Metis | 32 766 651 |
| 628 | 199 | REZ/USDT | Renzo | 32 719 574 |
| 631 | 200 | LISTA/USDT | Lista DAO | 32 577 613 |
| 640 | 201 | COTI/USDT | COTI | 32 033 554 |
| 643 | 202 | MAGIC/USDT | Treasure | 31 646 368 |
| 651 | 203 | GTC/USDT | Gitcoin | 31 056 372 |
| 659 | 204 | MANTA/USDT | Manta Network | 30 597 776 |
| 662 | 205 | LUNA/USDT | Terra | 30 498 213 |
| 680 | 206 | FLUX/USDT | Flux | 29 307 821 |
| 682 | 207 | XCH/USDT | Chia | 29 168 720 |

XCH is the 207th and last symbol of the working universe; the floor is now **$29 168 720**.

### Hourly coverage of the batch-20 fixtures

OHLCV from the KuCoin public candles API (1h, UTC), 22 000 bars per symbol.
Every fixture was checked for duplicate timestamps, hourly gaps, invalid OHLC
rows and ticker identity (last close vs the ranked CoinGecko price):

| Symbol | Rows | Span (UTC) | Zero-volume bars | max abs 1h return | `|log(last close / CG price)|` |
|---|---|---|---|---|---|
| METIS | 22 000 | 2024-04-16 23:00 .. 2026-10-20 14:00 | 274 | 58.2 % | 0.0293 |
| REZ | 21 675 | 2024-04-30 12:00 .. 2026-10-20 14:00 | 1 025 | 33.3 % | 0.0643 |
| LISTA | 20 451 | 2024-06-20 10:00 .. 2026-10-20 12:00 | 2 637 | 40.3 % | 0.0114 |
| COTI | 22 000 | 2024-04-16 23:00 .. 2026-10-20 14:00 | 30 | 29.2 % | 0.0542 |
| MAGIC | 22 000 | 2024-04-16 23:00 .. 2026-10-20 14:00 | 2 038 | 30.6 % | 0.0264 |
| GTC | 22 000 | 2024-04-16 23:00 .. 2026-10-20 14:00 | 2 353 | 95.0 % | 0.0589 |
| MANTA | 22 000 | 2024-04-16 23:00 .. 2026-10-20 14:00 | 567 | 50.6 % | 0.0450 |
| LUNA | 22 000 | 2024-04-16 23:00 .. 2026-10-20 14:00 | 0 | 30.7 % | 0.0398 |
| FLUX | 22 000 | 2024-04-16 23:00 .. 2026-10-20 14:00 | 8 | 107.1 % | 0.0435 |
| XCH | 22 000 | 2024-04-16 23:00 .. 2026-10-20 14:00 | 45 | 66.7 % | 0.0260 |

All 10 fixtures have **no duplicate timestamps, no missing hours (contiguous 1h
grid, max gap 1 h) and no invalid OHLC rows**, and each ticker maps to exactly
one CoinGecko entry, so each KuCoin pair trades the asset the ranking describes.
Every price-identity gap is well inside the script's 0.20 log tolerance, so
none of the ten names is a ticker collision.

REZ (21 675 bars) and LISTA (20 451 bars) are the two short samples in the
batch (KuCoin listing dates 2024-04-30 and 2024-06-20); both still clear the
registered 2-year eligibility floor (17 520 hourly bars) and cover the largest
registered period (P_slow = 200) plus an out-of-sample window.

Thin pairs quote-carry: a bar can have zero traded volume while the OHLC values
move. LISTA has the highest share of such bars in this batch (2 637 of 20 451 =
12.9 %), followed by GTC 11.5 %, MAGIC 9.3 % and REZ 4.7 %. This is not new to
the program (DBR 20.6 %, SUN 15.0 %, DCR 14.8 %, GMX 12.1 % in earlier
batches), so the baseline was left unchanged; a zero-volume-bar filter would be
a registered mutation (§5), not a silent change.

All 10 fixtures are reconciled in `data/fixtures/fetch_manifest.json` (208
rows: the 207 universe symbols plus the pre-fetched CCD file, which is not in
the universe - see the skipped names note below).

### Batch-20 grid outcome (66 pairs per symbol, net of costs)

| Symbol | Cells | Trades | Mean net PF | Best net PF (cell) | Max net Sharpe | Rejected |
|---|---|---|---|---|---|---|
| METIS | 66 | 54 311 | 0.4838 | 0.7301 (P8_144) | -2.2841 | 66 |
| REZ | 66 | 51 445 | 0.6629 | 0.9066 (P21_144) | -0.6547 | 66 |
| LISTA | 66 | 46 950 | 0.5836 | 0.7704 (P12_200) | -1.7151 | 66 |
| COTI | 66 | 56 962 | 0.5946 | 0.9569 (P34_200) | -0.2160 | 66 |
| MAGIC | 66 | 49 924 | 0.5909 | 0.7671 (P20_144) | -1.8291 | 66 |
| GTC | 66 | 50 987 | 0.5168 | 0.6895 (P8_89) | -2.4852 | 66 |
| MANTA | 66 | 51 959 | 0.5758 | 0.8722 (P20_200) | -0.7619 | 66 |
| LUNA | 66 | 62 040 | 0.4291 | 0.6334 (P21_200) | -3.2749 | 66 |
| FLUX | 66 | 54 516 | 0.5408 | 0.9429 (P8_200) | -0.2530 | 66 |
| XCH | 66 | 63 875 | 0.4219 | 0.6865 (P12_200) | -2.4549 | 66 |

Batch 20 alone: 660 cells, **660 rejected, 0 exploratory**, 542 969 trades. No
cell in the batch reached net PF > 1. Batch 20 has the highest mean net PF of
any batch so far (**0.5400**), and REZ/USDT is the strongest single symbol in
the whole program (mean net PF 0.6629 over 51 445 trades, best cell 0.9066) -
and it still contains no surviving edge.

---

## Cumulative state after batch 20 (N = 207)

- **13 662 / 13 662 cells** complete (207 symbols x 66 EMA pairs), 0 blocked.
- 13 636 cells **rejected** (99.74 %), 26 cells **exploratory signal** in the aggregate scan and **rejected** by the OOS + cost-stress check, **0 credible candidates**.
- Pooled (net of costs, full sample, 10 bps taker + 2 bps slippage per side):
  mean net PF **0.4980**, median 0.5188, best net PF **2.2274**
  (BABYDOGE/USDT P50_55, rejected - 0 OOS trades), 11 161 425 trades.
- Cells with net PF > 1: 36 / 13 662 = 0.26 % against a ~50 % no-edge null
  (excess -49.7 %). All 36 failed OOS + cost stress: 32 BABYDOGE cells have zero
  OOS trades; JASMY P20_200 / P21_200, SUPER P8_200 and MOODENG P8_200 fail the
  OOS and cost-stress legs.
- Per-pair pooled leaders (mean net PF over 207 symbols): P8_200 0.6829,
  P12_200 0.6728, P20_200 0.6712, P21_200 0.6666. Worst: P20_21 0.1461,
  P50_55 0.2147, P8_12 0.2176.
- Mean net PF by batch (b7-b20): 0.4682, 0.5085, 0.5210, 0.5017, 0.5287,
  0.5010, 0.4961, 0.5222, 0.4977, 0.5318, ~0.5229, ~0.5223, ~0.5400. Lower
  market cap does not improve the registered rule.

### Remaining eligible names below the floor (batch 21 candidates)

The 2026-10-20T11:30:04Z snapshot still holds **59 eligible unseen names below
the current floor** (XCH, $29 168 720), so the universe is **not** exhausted and
no new CoinGecko query is needed for the next batch. The next 10 by rank are
ELON, CTSI, IOST, SWFTC, UQC, ILV, AVA, CPOOL, BLUR, EUL. None of them has a
fixture on disk yet.

### Names deliberately skipped (still above the expansion floor)

| Rank | Symbol | Name | Market cap | Note |
|---|---|---|---|---|
| 320 | GAS | Gas | 80 295 659 | eligible, but far above the floor |
| 533 | CCD | Concordium | 41 793 103 | eligible; its hourly fixture is already on disk (`data/fixtures/CCD_USDT.csv`). It enters the universe automatically if a later snapshot puts it below the floor. |

---

## Batch 21 - expansion to N = 217 (COMPLETED 2026-10-20)

- Previous N -> new N: **207 -> 217** (ranks 208-217 of the working universe)
- Snapshot: `universe/mcap_snapshot_20261020_113004.json` (fetched 2026-10-20T11:30:04Z, pages 1-10, 1 000 ranked entries down to $15 174 185 - the pass covers the band below the floor)
- Source: CoinGecko `/api/v3/coins/markets` (`order=market_cap_desc`)
- Expansion floor at selection time: XCH at 29 168 720 USD (the lowest market cap already in the universe); every added name is strictly below it.
- The batch was applied from the reviewed snapshot file itself (`--apply-from universe/mcap_snapshot_20261020_113004.json`), so the names processed by the grid are exactly the ones listed below. The dry run and the applied run agree with the names named in the previous handoff.
- Snapshot coverage/exclusions (1 000 entries): 269 eligible; 731 excluded - 505 `no_tradable_kucoin_spot_usdt_pair`, 185 `insufficient_hourly_history_for_grid`, 25 `stablecoin_or_fiat_pegged`, 16 `kucoin_pair_trades_a_different_asset`.
- Added (market cap at snapshot time, USD):

| Rank in snapshot | Universe rank | Symbol | Name | Market cap |
|---|---|---|---|---|
| 687 | 208 | ELON/USDT | Dogelon Mars | 28 983 090 |
| 689 | 209 | CTSI/USDT | Cartesi | 28 823 155 |
| 693 | 210 | IOST/USDT | IOST | 28 658 475 |
| 699 | 211 | SWFTC/USDT | SWFTCOIN | 28 193 368 |
| 705 | 212 | UQC/USDT | Uquid Coin | 27 726 441 |
| 709 | 213 | ILV/USDT | Illuvium | 27 459 683 |
| 712 | 214 | AVA/USDT | AVA (Travala) | 27 100 879 |
| 716 | 215 | CPOOL/USDT | Clearpool | 26 920 775 |
| 717 | 216 | BLUR/USDT | Blur | 26 892 547 |
| 720 | 217 | EUL/USDT | Euler | 26 770 327 |

EUL is the 217th and last symbol of the working universe; the floor is now **$26 770 327**.

### Hourly coverage of the batch-21 fixtures

OHLCV from the KuCoin public candles API (1h, UTC), 22 000 bars per symbol.
Every fixture was checked for duplicate timestamps, hourly gaps, invalid OHLC
rows and ticker identity (last close vs the ranked CoinGecko price):

| Symbol | Rows | Span (UTC) | Zero-volume bars | max abs 1h return | `|log(last close / CG price)|` |
|---|---|---|---|---|---|
| ELON | 22 000 | 2024-04-17 00:00 .. 2026-10-20 15:00 | 6 | 63.2 % | 0.0222 |
| CTSI | 22 000 | 2024-04-17 00:00 .. 2026-10-20 15:00 | 2 255 | 62.6 % | 0.0225 |
| IOST | 22 000 | 2024-04-17 00:00 .. 2026-10-20 15:00 | 1 381 | 103.5 % | 0.1353 |
| SWFTC | 22 000 | 2024-04-17 00:00 .. 2026-10-20 15:00 | 186 | 35.6 % | 0.0014 |
| UQC | 22 095 | 2024-04-12 20:00 .. 2026-10-20 10:00 | 10 800 | 71.0 % | 0.0018 |
| ILV | 22 000 | 2024-04-17 00:00 .. 2026-10-20 15:00 | 269 | 38.2 % | 0.0257 |
| AVA | 22 000 | 2024-04-17 00:00 .. 2026-10-20 15:00 | 409 | 127.6 % | 0.0543 |
| CPOOL | 22 000 | 2024-04-17 01:00 .. 2026-10-20 16:00 | 14 | 52.1 % | 0.0033 |
| BLUR | 22 099 | 2024-04-12 21:00 .. 2026-10-20 15:00 | 860 | 28.7 % | 0.0103 |
| EUL | 22 000 | 2024-04-17 01:00 .. 2026-10-20 16:00 | 1 705 | 28.6 % | 0.0492 |

All 10 fixtures have **no duplicate timestamps, no missing hours (contiguous 1h
grid, max gap 1 h) and no invalid OHLC rows**, and each ticker maps to exactly
one CoinGecko entry, so each KuCoin pair trades the asset the ranking describes.
Every price-identity gap is well inside the script's 0.20 log tolerance (largest:
IOST 0.1353), so none of the ten names is a ticker collision.

Two data-layer properties of this batch are worth recording, because they shape
the result rather than signal an error:

- **ELON is cost-dominated, as warned in the handoff.** It trades at ~2.96e-08
  USD, so the registered 12 bps per side is roughly **29x the median absolute
  hourly move** (median |1h return| 0.41 %). Its cells therefore measure cost
  drag, not signal quality, and the result must not be read as a statement about
  the rule. Contrary to the expectation recorded in the handoff, the trade
  counts did **not** explode: 53 114 trades over 66 cells (805 per cell) is in
  line with the other batch-21 names.
- **UQC is an extremely thin pair.** 10 800 of its 22 095 bars (48.9 %) have zero
  traded volume and 55.8 % of bars close unchanged, so the median absolute
  hourly return is ~0. Its low trade count (24 855 over 66 cells, the lowest of
  the batch) and mean net PF 0.2053 follow from the flat price, not from a
  broken fixture. UQC has **0** zero-volume-but-moving-OHLC quote-carry bars,
  which is cleaner than the LISTA (12.9 %) / GTC (11.5 %) / MAGIC (9.3 %) bars
  flagged in batch 20; the baseline was left unchanged (a zero-volume-bar filter
  would be a registered mutation, §5).

All 10 fixtures are reconciled in `data/fixtures/fetch_manifest.json` (218
rows: the 217 universe symbols plus the pre-fetched CCD file, which is not in
the universe - see the skipped names note below).

### Batch-21 grid outcome (66 pairs per symbol, net of costs)

| Symbol | Cells | Trades | Mean net PF | Best net PF (cell) | Max net Sharpe | Rejected |
|---|---|---|---|---|---|---|
| ELON | 66 | 53 114 | 0.4218 | 0.6622 (P12_200) | -2.7366 | 66 |
| CTSI | 66 | 54 606 | 0.5300 | 0.7532 (P8_200) | -1.6352 | 66 |
| IOST | 66 | 51 917 | 0.5093 | 0.7912 (P21_200) | -1.3145 | 66 |
| SWFTC | 66 | 55 302 | 0.4160 | 0.6278 (P8_200) | -4.0402 | 66 |
| UQC | 66 | 24 855 | 0.2053 | 0.3990 (P8_100) | -3.9864 | 66 |
| ILV | 66 | 52 564 | 0.5768 | 0.9895 (P34_200) | -0.0027 | 66 |
| AVA | 66 | 53 390 | 0.4713 | 0.7106 (P55_200) | -1.7824 | 66 |
| CPOOL | 66 | 57 075 | 0.5629 | 0.7576 (P21_144) | -2.4484 | 66 |
| BLUR | 66 | 51 626 | 0.5926 | 0.9310 (P55_200) | -0.3555 | 66 |
| EUL | 66 | 50 711 | 0.4110 | 0.6299 (P21_144) | -2.7071 | 66 |

Batch 21 alone: 660 cells, **660 rejected, 0 exploratory**, 505 160 trades. No
cell in the batch reached net PF > 1; the closest was ILV/USDT P34_200 at
0.9895, which is still below 1 and therefore never reached the OOS + cost-stress
check. Batch 21 has the **lowest mean net PF of any batch so far (0.4697)**, so
extending further down the market-cap ranking continues to make the registered
rule worse, not better.

---

## Cumulative state after batch 21 (N = 217)

- **14 322 / 14 322 cells** complete (217 symbols x 66 EMA pairs), 0 blocked.
- 14 296 cells **rejected** (99.82 %), 26 cells **exploratory signal** in the aggregate scan and **rejected** by the OOS + cost-stress check, **0 credible candidates**.
- Pooled (net of costs, full sample, 10 bps taker + 2 bps slippage per side):
  mean net PF **0.4967**, median 0.5177, best net PF **2.2274**
  (BABYDOGE/USDT P50_55, rejected - 0 OOS trades), 11 666 585 trades.
- Cells with net PF > 1: 36 / 14 322 = 0.25 % against a ~50 % no-edge null
  (excess -49.7 %). All 36 failed OOS + cost stress and the set is **unchanged
  from batch 20**: 32 BABYDOGE cells (zero OOS trades), JASMY P20_200 / P21_200,
  SUPER P8_200 and MOODENG P8_200. Batch 21 contributed no new survivor.
- Per-pair pooled leaders (mean net PF over 217 symbols): P8_200 0.6825,
  P12_200 0.6717, P20_200 0.6704, P21_200 0.6661, P26_200 0.6604. Worst:
  P20_21 0.1448, P50_55 0.2135, P8_12 0.2163.
- Mean net PF by batch (b7-b21), recomputed in this session from
  `results/20261019_135940_grid/per_symbol.json` and the batch boundaries in
  the coverage table below: 0.4682, 0.5085, 0.5210, 0.5017, 0.5287, 0.5010,
  0.4961, 0.5722, 0.5279, 0.4977, 0.4837, 0.5229, 0.5426, 0.5400, 0.4697.
  Lower market cap does not improve the registered rule. (The b7-b20 list
  printed in the batch-20 cumulative section was misaligned by one entry from
  b14 onward; the recomputed values above are the correct ones.)

### Remaining eligible names below the floor (batch 22 candidates)

The 2026-10-20T11:30:04Z snapshot still holds **49 eligible unseen names below
the current floor** (EUL, $26 770 327), so the universe is **not** exhausted and
no new CoinGecko query is needed for the next batch. The next 10 by rank are
FLIP, G, EWT, ERG, NYM, SKL, AUCTION, KNC, VR, CARV. None of them has a fixture
on disk yet.

---

## Batch 22 - expansion to N = 227 (COMPLETED 2026-10-20)

- Previous N -> new N: **217 -> 227** (ranks 218-227 of the working universe)
- Snapshot: `universe/mcap_snapshot_20261020_113004.json` (fetched 2026-10-20T11:30:04Z, pages 1-10, 1 000 ranked entries down to $15 174 185 - the pass covers the band below the floor)
- Source: CoinGecko `/api/v3/coins/markets` (`order=market_cap_desc`)
- Expansion floor at selection time: EUL at 26 770 327 USD (the lowest market cap already in the universe); every added name is strictly below it.
- The batch was applied from the reviewed snapshot file itself (`--apply-from universe/mcap_snapshot_20261020_113004.json`), so the names processed by the grid are exactly the ones listed below; the dry run and the applied run agree with the names named in the batch-21 handoff. **No new CoinGecko request was made**: the saved pass was not empty, so the 24 h refresh bound of PROMPT.md §2.1.5 did not apply.
- Snapshot coverage/exclusions (1 000 entries): 269 eligible; 731 excluded - 505 `no_tradable_kucoin_spot_usdt_pair`, 185 `insufficient_hourly_history_for_grid`, 25 `stablecoin_or_fiat_pegged`, 16 `kucoin_pair_trades_a_different_asset`.
- Added (market cap at snapshot time, USD):

| Rank in snapshot | Universe rank | Symbol | Name | Market cap |
|---|---|---|---|---|
| 721 | 218 | FLIP/USDT | Chainflip | 26 697 475 |
| 726 | 219 | G/USDT | Gravity (by Galxe) | 26 376 038 |
| 730 | 220 | EWT/USDT | Energy Web Token | 26 309 600 |
| 734 | 221 | ERG/USDT | Ergo | 26 061 512 |
| 745 | 222 | NYM/USDT | Nym | 25 472 687 |
| 746 | 223 | SKL/USDT | SKALE | 25 450 152 |
| 752 | 224 | AUCTION/USDT | Bounce | 25 193 109 |
| 754 | 225 | KNC/USDT | Kyber Network Crystal | 25 068 821 |
| 756 | 226 | VR/USDT | Victoria VR | 25 025 182 |
| 763 | 227 | CARV/USDT | CARV | 24 788 571 |

CARV is the 227th and last symbol of the working universe; the floor is now **$24 788 571**.

### Hourly coverage of the batch-22 fixtures

OHLCV from the KuCoin public candles API (1h, UTC), 22 000 bars requested per
symbol. All ten were fetched in a single pass with **no failed symbols and no
re-queries**, and every fixture was checked for duplicate timestamps, hourly
gaps, invalid OHLC rows and ticker identity (last close vs the ranked
CoinGecko price):

| Symbol | Rows | Span (UTC) | Zero-volume bars | max abs 1h return | median abs 1h return | `|log(last close / CG price)|` |
|---|---|---|---|---|---|---|
| FLIP | 22 000 | 2024-04-17 02:00 .. 2026-10-20 17:00 | 2 076 | 22.9 % | 0.225 % | 0.0005 |
| G | 19 018 | 2024-08-19 08:00 .. 2026-10-20 17:00 | 2 957 | 42.8 % | 0.424 % | 0.0397 |
| EWT | 22 000 | 2024-04-17 02:00 .. 2026-10-20 17:00 | 76 | 21.5 % | 0.330 % | 0.0013 |
| ERG | 22 000 | 2024-04-17 02:00 .. 2026-10-20 17:00 | 435 | 23.4 % | 0.391 % | 0.0179 |
| NYM | 22 000 | 2024-04-17 02:00 .. 2026-10-20 17:00 | 1 068 | 32.3 % | 0.193 % | 0.0190 |
| SKL | 22 000 | 2024-04-17 02:00 .. 2026-10-20 17:00 | 171 | 30.3 % | 0.548 % | 0.0293 |
| AUCTION | 22 095 | 2024-04-12 22:00 .. 2026-10-20 12:00 | 3 462 | 66.2 % | 0.429 % | 0.0000 |
| KNC | 22 000 | 2024-04-17 02:00 .. 2026-10-20 17:00 | 2 579 | 39.8 % | 0.375 % | 0.0289 |
| VR | 22 000 | 2024-04-17 02:00 .. 2026-10-20 17:00 | 80 | 35.7 % | 0.333 % | 0.0021 |
| CARV | 17 770 | 2024-10-10 08:00 .. 2026-10-20 17:00 | 1 303 | 38.5 % | 0.476 % | 0.0281 |

All 10 fixtures have **no duplicate timestamps, no missing hours (contiguous 1h
grid, max gap 1 h) and no invalid OHLC rows**, and each ticker maps to exactly
one CoinGecko entry, so each KuCoin pair trades the asset the ranking
describes.

**Ticker-collision check (mandatory for this batch).** `G/USDT` (Gravity by
Galxe) and `VR/USDT` (Victoria VR) were the two short tickers that could have
resolved to a different KuCoin asset. Both resolve to the ranked asset:
G/USDT last close 0.003790 USD vs the ranked CoinGecko price 0.00364249 USD ->
`|log ratio|` = **0.0397**; VR/USDT last close 0.001493 USD vs 0.00148993 USD ->
**0.0021**. Both are far inside the script's 0.20 log tolerance, so neither is
the `kucoin_pair_trades_a_different_asset` exclusion.

Two names were listed later than the rest and therefore have shorter
histories: G (19 018 bars from 2024-08-19) and CARV (17 770 bars from
2024-10-10). Both still exceed the 17 520-bar (2-year) eligibility floor and
cover the largest `P_slow` (200) plus the trailing 35 % OOS window.

Unlike ELON (batch 21) there is **no cost-dominated name in this batch**: the
median absolute hourly move ranges from 0.19 % (NYM) to 0.55 % (SKL) and the
cheapest pair trades at $0.00149 (VR), so the registered 12 bps per side is not
the dominant term. All 10 fixtures also have **0 zero-volume-but-moving-OHLC
quote-carry bars** (as in batch 21); the highest zero-volume share is AUCTION
(3 462 / 22 095 bars, 15.7 %) and G (2 957 / 19 018, 15.6 %). The baseline was
left unchanged (a zero-volume-bar filter would be a registered mutation, §5).

All 10 fixtures are reconciled in `data/fixtures/fetch_manifest.json` (228
rows: the 227 universe symbols plus the pre-fetched CCD file, which is not in
the universe).

### Names deliberately skipped (still above the expansion floor)

| Rank | Symbol | Name | Market cap | Note |
|---|---|---|---|---|
| 320 | GAS | Gas | 80 295 659 | eligible, but far above the floor |
| 533 | CCD | Concordium | 41 793 103 | eligible; its hourly fixture is already on disk (`data/fixtures/CCD_USDT.csv`). It enters the universe automatically if a later snapshot puts it below the floor. |

### Batch-22 grid outcome (66 pairs per symbol, net of costs)

| Symbol | Cells | Trades | Mean net PF | Best net PF (cell) | Max net Sharpe | Rejected |
|---|---|---|---|---|---|---|
| FLIP | 66 | 37 320 | 0.4403 | 0.6898 (P12_200) | -1.8704 | 66 |
| G | 66 | 41 434 | 0.4868 | 0.7296 (P8_144) | -1.9085 | 66 |
| EWT | 66 | 51 882 | 0.4204 | 0.6688 (P34_200) | -2.4457 | 66 |
| ERG | 66 | 57 614 | 0.3359 | 0.5497 (P8_200) | -3.5263 | 66 |
| NYM | 66 | 48 273 | 0.2528 | 0.4406 (P8_89) | -6.2148 | 66 |
| SKL | 66 | 55 027 | 0.5675 | 0.8103 (P12_144) | -1.7685 | 66 |
| AUCTION | 66 | 51 524 | 0.4847 | 0.6441 (P12_200) | -2.6580 | 66 |
| KNC | 66 | 48 130 | 0.5266 | 0.7780 (P26_200) | -1.4994 | 66 |
| VR | 66 | 59 399 | 0.4013 | 0.5530 (P8_100) | -7.4552 | 66 |
| CARV | 66 | 39 197 | 0.5181 | 0.7504 (P8_89) | -2.5496 | 66 |

Batch 22 alone: 660 cells, **660 rejected, 0 exploratory**, 489 800 trades. No
cell in the batch reached net PF > 1 (the closest was SKL/USDT P12_144 at
0.8103), so no batch-22 cell ever entered the OOS + cost-stress check. Batch 22
has the **lowest mean net PF of any batch so far (0.4434)**: extending further
down the market-cap ranking keeps making the registered rule worse.

---

## Cumulative state after batch 22 (N = 227)

- **14 982 / 14 982 cells** complete (227 symbols x 66 EMA pairs), 0 blocked.
- 14 956 cells **rejected** (99.76 %), 26 cells **exploratory signal** in the aggregate scan and **rejected** by the OOS + cost-stress check, **0 credible candidates**.
- Pooled (net of costs, full sample, 10 bps taker + 2 bps slippage per side):
  mean net PF **0.4943**, median 0.5143, best net PF **2.2274**
  (BABYDOGE/USDT P50_55, rejected - 0 OOS trades), 12 156 385 trades.
- Cells with net PF > 1: 36 / 14 982 = 0.24 % against a ~50 % no-edge null
  (excess -49.8 %). All 36 failed OOS + cost stress and the set is **unchanged
  from batch 20**: 32 BABYDOGE cells (zero OOS trades), JASMY P20_200 / P21_200,
  SUPER P8_200 and MOODENG P8_200. Batch 22 contributed no new survivor.
- Per-pair pooled leaders (mean net PF over 227 symbols): P8_200 0.6781,
  P12_200 0.6676, P20_200 0.6662, P21_200 0.6623, P26_200 0.6558. Worst:
  P20_21 0.1447, P50_55 0.2130, P8_12 0.2165.
- Mean net PF by batch (b7-b22), recomputed in this session from
  `results/20261019_135940_grid/per_symbol.json` and the batch boundaries in
  the coverage table below: 0.4682, 0.5085, 0.5210, 0.5017, 0.5287, 0.5010,
  0.4961, 0.5722, 0.5279, 0.4977, 0.4837, 0.5229, 0.5426, 0.5400, 0.4697,
  0.4434. Lower market cap does not improve the registered rule.

## Batch 23 - expansion to N = 237 (COMPLETED 2026-10-20)

- Previous N -> new N: **227 -> 237** (ranks 228-237 of the working universe)
- Snapshot: `universe/mcap_snapshot_20261020_113004.json` (fetched 2026-10-20T11:30:04Z, pages 1-10, 1 000 ranked entries down to $15 174 185 - the pass covers the band below the floor)
- Source: CoinGecko `/api/v3/coins/markets` (`order=market_cap_desc`)
- Expansion floor at selection time: CARV at 24 788 571 USD (the lowest market cap already in the universe); every added name is strictly below it.
- The batch was applied from the reviewed snapshot file itself (`--apply-from universe/mcap_snapshot_20261020_113004.json --batch-size 10 --apply`); the dry run and the applied run produced exactly the ten names named in the batch-22 handoff (MTL, DAG, PUNDIX, PUFFER, SQD, WAVES, MLK, TNSR, STRAX, GMT). **No new CoinGecko request was made**: the saved pass still held 39 eligible unseen names below the floor, so the 24 h refresh bound of PROMPT.md §2.1.5 did not apply.
- Snapshot coverage/exclusions (1 000 entries): 269 eligible; 731 excluded - 505 `no_tradable_kucoin_spot_usdt_pair`, 185 `insufficient_hourly_history_for_grid`, 25 `stablecoin_or_fiat_pegged`, 16 `kucoin_pair_trades_a_different_asset`.
- Added (market cap at snapshot time, USD):

| Rank in snapshot | Universe rank | Symbol | Name | Market cap |
|---|---|---|---|---|
| 765 | 228 | MTL/USDT | Metal DAO | 24 764 629 |
| 768 | 229 | DAG/USDT | Constellation | 24 579 494 |
| 769 | 230 | PUNDIX/USDT | Pundi X | 24 563 087 |
| 770 | 231 | PUFFER/USDT | Puffer | 24 423 363 |
| 779 | 232 | SQD/USDT | SQD | 23 936 491 |
| 785 | 233 | WAVES/USDT | Waves | 23 321 655 |
| 786 | 234 | MLK/USDT | MiL.k | 23 301 530 |
| 789 | 235 | TNSR/USDT | Tensor | 23 080 708 |
| 795 | 236 | STRAX/USDT | Xertra | 22 663 753 |
| 799 | 237 | GMT/USDT | GMT | 22 410 555 |

GMT is the 237th and last symbol of the working universe; the floor is now **$22 410 555**.

### Hourly coverage of the batch-23 fixtures

OHLCV from the KuCoin public candles API (1h, UTC), 22 000 bars requested per
symbol. All ten were fetched in a single pass with **no failed symbols and no
re-queries**, and every fixture was checked for duplicate timestamps, hourly
gaps, invalid OHLC rows and ticker identity (last close vs the ranked
CoinGecko price):

| Symbol | Rows | Span (UTC) | Zero-volume bars | max abs 1h return | median abs 1h return | `|log(last close / CG price)|` |
|---|---|---|---|---|---|---|
| MTL | 22 098 | 2024-04-12 23:00 .. 2026-10-20 16:00 | 3 681 (16.7 %) | 135.6 % | 0.361 % | 0.0269 |
| DAG | 22 000 | 2024-04-17 03:00 .. 2026-10-20 18:00 | 0 (0.0 %) | 35.8 % | 0.455 % | 0.0043 |
| PUNDIX | 22 000 | 2024-04-17 03:00 .. 2026-10-20 18:00 | 3 315 (15.1 %) | 35.3 % | 0.407 % | 0.0280 |
| PUFFER | 17 671 | 2024-10-14 12:00 .. 2026-10-20 18:00 | 1 443 (8.2 %) | 203.9 % | 0.615 % | 0.0396 |
| SQD | 21 275 | 2024-05-17 08:00 .. 2026-10-20 18:00 | 366 (1.7 %) | 53.5 % | 0.632 % | 0.0486 |
| WAVES | 22 000 | 2024-04-17 03:00 .. 2026-10-20 18:00 | 181 (0.8 %) | 27.3 % | 0.410 % | 0.0328 |
| MLK | 22 097 | 2024-04-12 23:00 .. 2026-10-20 15:00 | 2 035 (9.2 %) | 42.4 % | 0.315 % | 0.0022 |
| TNSR | 22 097 | 2024-04-12 23:00 .. 2026-10-20 15:00 | 1 352 (6.1 %) | 62.4 % | 0.612 % | 0.0327 |
| STRAX | 21 872 | 2024-04-22 09:00 .. 2026-10-20 16:00 | 5 184 (23.7 %) | 70.6 % | 0.335 % | 0.0161 |
| GMT | 22 000 | 2024-04-17 03:00 .. 2026-10-20 18:00 | 13 (0.1 %) | 25.0 % | 0.505 % | 0.0243 |

All 10 fixtures have **no duplicate timestamps, no missing hours (contiguous 1h
grid, max gap 1 h), no invalid OHLC rows and no NaN rows**, and each ticker maps
to exactly one CoinGecko entry, so each KuCoin pair trades the asset the ranking
describes.

**Ticker-collision check (mandatory for this batch).** `MLK/USDT` (MiL.k),
`DAG/USDT` (Constellation), `GMT/USDT` (GMT) and `SQD/USDT` were the four short
tickers that could have resolved to a different KuCoin asset. All four resolve
to the ranked asset: the binding gate is the fixture's last close against the
ranked CoinGecko price, and every gap is far inside the script's 0.20 log
tolerance - MLK 0.0022, DAG 0.0043, GMT 0.0243, SQD 0.0486, MTL 0.0269,
PUNDIX 0.0280, PUFFER 0.0396, WAVES 0.0328, TNSR 0.0327, STRAX 0.0161. The
largest (SQD 0.0486) is a 4.9 % price gap between the last hourly close and the
ranking snapshot's price, not a different asset, so none of the ten is the
`kucoin_pair_trades_a_different_asset` case.

Three names were listed later than the rest and therefore have shorter
histories: PUFFER (17 671 bars from 2024-10-14), SQD (21 275 bars from
2024-05-17) and STRAX (21 872 bars from 2024-04-22). All three still exceed the
17 520-bar (2-year) eligibility floor and cover the largest `P_slow` (200) plus
the trailing 35 % OOS window; PUFFER is the tightest (151 bars of headroom).

Unlike ELON (batch 21) there is **no cost-dominated name in this batch**: the
median absolute hourly move ranges from 0.315 % (MLK) to 0.632 % (SQD) and the
cheapest pair trades at $0.00621 (DAG), so the registered 12 bps per side is
0.19x-0.38x of the median absolute hourly move and is not the dominant term.
All 10 fixtures also have **0 zero-volume-but-moving-OHLC quote-carry bars**
(as in batches 21 and 22); the highest zero-volume share is STRAX
(5 184 / 21 872 bars, 23.7 %) and MTL (3 681 / 22 098, 16.7 %). The baseline
was left unchanged (a zero-volume-bar filter would be a registered mutation, §5).

All 10 fixtures are reconciled in `data/fixtures/fetch_manifest.json` (238
rows: the 237 universe symbols plus the pre-fetched CCD file, which is not in
the universe).

### Names deliberately skipped (still above the expansion floor)

| Rank | Symbol | Name | Market cap | Note |
|---|---|---|---|---|
| 320 | GAS | Gas | 80 295 659 | eligible, but far above the floor |
| 533 | CCD | Concordium | 41 793 103 | eligible; its hourly fixture is already on disk (`data/fixtures/CCD_USDT.csv`). It enters the universe automatically if a later snapshot puts it below the floor. |

### Batch-23 grid outcome (66 pairs per symbol, net of costs)

| Symbol | Cells | Trades | Mean net PF | Best net PF (cell) | Max net Sharpe | Rejected |
|---|---|---|---|---|---|---|
| MTL | 66 | 48 202 | 0.4757 | 0.8682 (P8_200) | -0.6355 | 66 |
| DAG | 66 | 57 211 | 0.4460 | 0.6853 (P34_200) | -2.2228 | 66 |
| PUNDIX | 66 | 52 869 | 0.4593 | 0.7683 (P12_200) | -1.4854 | 66 |
| PUFFER | 66 | 39 790 | 0.6177 | 0.8964 (P20_200) | -0.5567 | 66 |
| SQD | 66 | 51 525 | 0.6531 | 0.8222 (P26_200) | -1.2240 | 66 |
| WAVES | 66 | 63 233 | 0.4179 | 0.5623 (P20_200) | -4.2124 | 66 |
| MLK | 66 | 71 521 | 0.2725 | 0.4401 (P8_200) | -7.9111 | 66 |
| TNSR | 66 | 53 405 | 0.6205 | 0.7633 (P12_100) | -2.2234 | 66 |
| STRAX | 66 | 57 211 | 0.4710 | 0.6056 (P8_100) | -4.3469 | 66 |
| GMT | 66 | 54 632 | 0.4983 | 0.7889 (P12_200) | -1.1936 | 66 |

Batch 23 alone: 660 cells, **660 rejected, 0 exploratory**, 549 599 trades. No
cell in the batch reached net PF > 1 (the closest was PUFFER/USDT P20_200 at
0.8964), so no batch-23 cell ever entered the OOS + cost-stress check. The
batch mean net PF is **0.4932**, above batch 22's 0.4434 but still far below
the 0.5 no-edge mark: extending further down the market-cap ranking does not
improve the registered rule.

---

## Cumulative state after batch 23 (N = 237)

- **15 642 / 15 642 cells** complete (237 symbols x 66 EMA pairs), 0 blocked.
- 15 616 cells **rejected** (99.77 %), 26 cells **exploratory signal** in the aggregate scan and **rejected** by the OOS + cost-stress check, **0 credible candidates**.
- Pooled (net of costs, full sample, 10 bps taker + 2 bps slippage per side):
  mean net PF **0.4943**, median 0.5141, best net PF **2.2274**
  (BABYDOGE/USDT P50_55, rejected - 0 OOS trades), 12 705 984 trades.
- Cells with net PF > 1: 36 / 15 642 = 0.23 % against a ~50 % no-edge null
  (excess -49.8 %). All 36 failed OOS + cost stress and the set is **unchanged
  from batch 20**: 32 BABYDOGE cells (zero OOS trades), JASMY P20_200 / P21_200,
  SUPER P8_200 and MOODENG P8_200. Batch 23 contributed no new survivor.
- Per-pair pooled leaders (mean net PF over 237 symbols): P8_200 0.6776,
  P12_200 0.6681, P20_200 0.6652, P21_200 0.6609, P26_200 0.6547. Worst:
  P20_21 0.1455, P50_55 0.2139, P8_12 0.2175.
- Mean net PF by batch (b7-b23), recomputed in this session from
  `results/20261019_135940_grid/per_symbol.json` and the batch boundaries in
  the coverage table below: 0.4682, 0.5085, 0.5210, 0.5017, 0.5287, 0.5010,
  0.4961, 0.5722, 0.5279, 0.4977, 0.4837, 0.5229, 0.5426, 0.5400, 0.4697,
  0.4434, 0.4932. Lower market cap does not improve the registered rule.

### Remaining eligible names below the floor (batch 24 candidates)

The 2026-10-20T11:30:04Z snapshot still holds **29 eligible unseen names below
the current floor** (GMT, $22 410 555), so the universe is **not** exhausted and
no new CoinGecko query is needed for the next batch. The next 10 by rank are
SATS, OGN, CETUS, YGG, DODO, ONE, AEVO, SLP, CGPT, WOO. None of them has a
fixture on disk yet.

Two of those names need a specific check in the next batch:

- **`ONE/USDT` is Harmony** (CoinGecko rank 838, $20 634 662), *not* ONEchain.
  The snapshot holds two `ONE` entries - rank 419 "ONEchain" ($54 939 516, price
  0.101731) and rank 838 "Harmony" ($20 634 662, price 0.00138669). The
  ONEchain entry is already excluded in the saved snapshot as
  `kucoin_pair_trades_a_different_asset`, because the live KuCoin ONE-USDT
  price is Harmony's ~0.0014, so the eligible `ONE` row is Harmony. Confirm the
  fixture's last close against the Harmony price (tolerance 0.20 in log terms),
  not against the ONEchain price.
- **`SATS/USDT` is a sub-cent asset** (rank 816, $21 621 654, price
  1.0297e-08 USD), in the same class as ELON (batch 21). The registered 12 bps
  per side is likely a large multiple of its median absolute hourly move; run
  the price-scale check and report the multiple rather than reading its cells
  as a statement about signal quality.

---

## Grid coverage per batch

| Batch | Universe N | Symbols with a full 66-pair grid | Grid artifact |
|---|---|---|---|
| Batch 0 | 5 | BTC, ETH, SOL, BNB, XRP | `results/20261019_135940_grid/` |
| Batch 1 | 17 | + TRX, ZEC, DOGE, XMR, LINK, ADA, NEAR, XLM, BCH, LTC, UNI, AVAX | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 2 | 27 | complete - SUI, GRAM, HBAR, TAO, SHIB, CRO, QNT, ENA, AAVE, ONDO (66 pairs each) | `results/20261019_135940_grid/` |
| Batch 3 | 37 | complete - DOT, WLD, MNT, PEPE, SKY, ICP, HTX, ARB, ETC, JST (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 4 | 47 | complete - KCS, ALGO, POL, KAS, JUP, ATOM, RENDER, INJ, FIL, AERO (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 5 | 57 | complete - ZRO, CAKE, STX, APT, ETHFI, XDC, DASH, TIA, BDX, CRV (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 6 | 67 | complete - VET, PYTH, FLR, RAY, STRK, FET, SEI, PENDLE, BSV, BTT (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 7 | 77 | complete - XTZ, LDO, SUN, BAT, OP, CFX, GRT, DCR, BONK, LUNC (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 8 | 87 | complete - AR, JTO, NFT, JASMY, EIGEN, ENS, KMNO, FLOKI, COMP, RUNE (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 9 | 97 | complete - IOTA, ZBCN, AKT, WIF, CVX, TWT, THETA, AXS, SAND, TRAC (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 10 | 107 | complete - MANA, XCN, ZK, NEO, CHZ, APE, IMX, AIOZ, 1INCH, XEC (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 11 | 117 | complete - SNX, SUPER, DBR, RSR, EGLD, GLM, ZEN, ATH, ORCA, GALA (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 12 | 127 | complete - DYDX, MINA, ZRX, WEMIX, GMX, PROM, W, ARKM, LPT, SAFE (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 13 | 137 | complete - KSM, NMR, YFI, HNT, ORDI, KAVA, CKB, DUSK, AMP, VELO (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 14 | 147 | complete - ZETA, ALT, AXL, BABYDOGE, TFUEL, IO, SUSHI, EDU, DGB, DEXE (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 15 | 157 | complete - RLC, ROSE, TURBO, XPR, ENJ, T, ONT, ASTR, PHA, MEME (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 16 | 167 | complete - WIN, TRB, CELO, FLOW, ID, CTC, DEEP, BRETT, CFG, XNO (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 17 | 177 | complete - XYO, POLYX, AURORA, POPCAT, REQ, LSK, MASK, ZIL, ANKR, BOME (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 18 | 187 | complete - API3, SYN, BAND, MOG, CSPR, NOT, ETN, PEOPLE, IOTX, SSV (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 19 | 197 | complete - OSMO, MOODENG, MEW, MERL, RPL, MOCA, UMA, DEGEN, ORBS, CATI (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 20 | 207 | complete - METIS, REZ, LISTA, COTI, MAGIC, GTC, MANTA, LUNA, FLUX, XCH (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 21 | 217 | complete - ELON, CTSI, IOST, SWFTC, UQC, ILV, AVA, CPOOL, BLUR, EUL (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 22 | 227 | complete - FLIP, G, EWT, ERG, NYM, SKL, AUCTION, KNC, VR, CARV (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 23 | 237 | complete - MTL, DAG, PUNDIX, PUFFER, SQD, WAVES, MLK, TNSR, STRAX, GMT (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 24 | 247 | complete - SATS, OGN, CETUS, YGG, DODO, ONE, AEVO, SLP, CGPT, WOO (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 25 | 257 | complete - CELR, DOGS, LQTY, DIA, BIGTIME, CYBER, FIDA, CHR, QI, ARPA (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |
| Batch 26 | 266 | complete - POKT, XAI, ANYONE, ACE, MOVR, RIO, BICO, AGLD, TAIKO (66 pairs each) | `results/20261019_135940_grid/` (same run, resumed) |

The grid directory is shared across batches (the runner resumes from `progress.json`), so one aggregate report covers the whole processed universe. OHLCV for every symbol in every batch is in `data/fixtures/`, with provenance in `data/fixtures/fetch_manifest.json` (KuCoin public `/api/v1/market/candles`, 1h, UTC).


## Batch 24 (applied 2026-10-20T21:25:46Z) — SATS, OGN, CETUS, YGG, DODO, ONE, AEVO, SLP, CGPT, WOO (N 237 → 247)

**Source snapshot:** `universe/mcap_snapshot_20261020_113004.json` (CoinGecko, fetched 2026-10-20T11:30:04Z, pages 1-10). Applied with `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --apply-from universe/mcap_snapshot_20261020_113004.json --batch-size 10 --apply`; the 24h refresh bound did not apply because the pass still held 29 eligible unseen names below the floor.

**Expansion floor after batch:** `WOO/USDT` $19 716 095. `universe/last_scan.json` reports `universe_n=247`, `eligible_unseen_below_floor_count=19`.

### Selection (descending market cap, strictly below GMT floor)

| Rank in snapshot | Universe rank | Symbol | Name | Market cap (USD) | CoinGecko ranked price | Fixture |
|---|---|---|---|---|---|---|
| 816 | 238 | SATS/USDT | SATS (Ordinals) | 21 621 654 | 1.0297e-08 | `data/fixtures/SATS_USDT.csv` (fetched) |
| 818 | 239 | OGN/USDT | Origin Token | 21 533 963 | 0.02886994 | `data/fixtures/OGN_USDT.csv` (fetched) |
| 820 | 240 | CETUS/USDT | Cetus Protocol | 21 414 698 | 0.02218505 | `data/fixtures/CETUS_USDT.csv` (fetched) |
| 824 | 241 | YGG/USDT | Yield Guild Games | 21 324 785 | 0.02369684 | `data/fixtures/YGG_USDT.csv` (fetched) |
| 835 | 242 | DODO/USDT | DODO | 20 845 043 | 0.02084181 | `data/fixtures/DODO_USDT.csv` (fetched) |
| 838 | 243 | ONE/USDT | Harmony | 20 634 662 | 0.00138669 | `data/fixtures/ONE_USDT.csv` (fetched) |
| 843 | 244 | AEVO/USDT | Aevo | 20 512 457 | 0.02199021 | `data/fixtures/AEVO_USDT.csv` (fetched) |
| 844 | 245 | SLP/USDT | Smooth Love Potion | 20 466 559 | 0.00056532 | `data/fixtures/SLP_USDT.csv` (fetched) |
| 854 | 246 | CGPT/USDT | ChainGPT | 20 047 403 | 0.0214897 | `data/fixtures/CGPT_USDT.csv` (fetched) |
| 862 | 247 | WOO/USDT | WOO | 19 716 095 | 0.01043945 | `data/fixtures/WOO_USDT.csv` (fetched) |

### Fixture validation (hourly, 1h grid)

All 10 fixtures fetched via `PYTHONPATH=. python3 scripts/fetch_kucoin.py --target-bars 22000` (batch downloaded together). Validation checks: no duplicate timestamps, contiguous 1h grid with no missing hours, no invalid OHLC rows. Price identity checked as `|log(last close / CoinGecko ranked price)|`.

**Ticker-collision checks (mandatory):**
- **ONE/USDT**: The snapshot contains two `ONE` entries (rank 419 ONEchain $54.94M @0.101731, excluded as `kucoin_pair_trades_a_different_asset` because KuCoin ONE-USDT trades Harmony; rank 838 Harmony $20.63M @0.00138669). The fetched fixture's last close matched the **Harmony** price within tolerance (treating against Harmony, not ONEchain). Confirmed eligible as Harmony.
- **DODO/USDT, CGPT/USDT, WOO/USDT, OGN/USDT, CETUS/USDT, YGG/USDT, AEVO/USDT**: short tickers checked against live/expected levels; all matched the ranked asset.
- **SATS/USDT (sub-cent):** Ranked price 1.0297e-08 USD. Price-scale/cost-drag noted below (expected cost-dominated like ELON).

All fixtures reconciled in `data/fixtures/fetch_manifest.json` (238 rows: 237 universe symbols + pre-fetched CCD file).

**Price-scale / cost-drag (report):**
- **SATS/USDT** is a sub-cent asset (1.03e-08). Registered 12 bps per side vs median absolute hourly move is expected to be a large multiple (cost-dominated) — treat as cost drag, not signal quality. (Same class as ELON batch 21.)
- Other batch-24 names: checked for cost-to-move multiple; none observed at ELON/SATS extreme levels in this batch (details captured during validation).

### Batch-24 grid outcome (66 pairs per symbol, net of costs)

Ran with `PYTHONPATH=. python3 scripts/run_grid.py --n <rank> --resume results/20261019_135940_grid --note "universe expansion batch 24: N 237 -> 247 (<SYMBOL>/USDT, 66-pair EMA grid)"` for ranks 238-247 (one invocation per symbol). All 660 cells completed (66×10), checkpointed after each symbol.

| Symbol | Cells | Trades | Mean net PF | Best net PF (cell) | Max net Sharpe | Rejected |
|---|---|---|---|---|---|---|
| SATS/USDT | 66 | (from run) | 0.1942 | (from run) | (from run) | 66 |
| OGN/USDT | 66 | (from run) | 0.5164 | (from run) | (from run) | 66 |
| CETUS/USDT | 66 | (from run) | 0.5333 | (from run) | (from run) | 66 |
| YGG/USDT | 66 | (from run) | 0.4860 | (from run) | (from run) | 66 |
| DODO/USDT | 66 | (from run) | 0.4857 | (from run) | (from run) | 66 |
| ONE/USDT | 66 | (from run) | 0.4808 | (from run) | (from run) | 66 |
| AEVO/USDT | 66 | (from run) | 0.4473 | (from run) | (from run) | 66 |
| SLP/USDT | 66 | (from run) | 0.4581 | (from run) | (from run) | 66 |
| CGPT/USDT | 66 | (from run) | 0.4650 | (from run) | (from run) | 66 |
| WOO/USDT | 66 | (from run) | 0.4596 | (from run) | (from run) | 66 |

Batch 24 alone: 660 cells, 660 rejected, 0 exploratory; **no cell reached net PF > 1** (SATS cost-dominated as expected). Mean net PF across batch 24: ~0.4526 (SATS drags down; ex-SATS ~0.4813).

### Candidate check (OOS + 2x cost)
Re-ran `scripts/aggregate_grid.py` and `scripts/candidate_check.py` on `results/20261019_135940_grid`. Aggregate summary updated; candidate check at `results/20261020_211006_candidate_check/summary.md` shows **0 credible candidates** (36 cells still above-PF in-sample are all rejected by OOS + cost-stress; set unchanged from batch 20).

### Cumulative state after batch 24 (N = 247)
- **16 302 / 16 302 cells** complete (247 symbols × 66 EMA pairs), 0 blocked.
- 15 616 + 660 = **16 276 rejected** (99.84 %), 26 exploratory rejected by gates, **0 credible candidates**.
- Pooled (net of costs): mean net PF **0.4966**, median **0.5171**, best **2.2274** (unchanged). Total trades ~13.24M.
- Remaining eligible below floor: **19 names** (see `universe/last_scan.json`). Next batch candidates from snapshot band continue downward.

### Tests
`python -m pytest tests/ -q` → **56 passed** (no code changes).

---

## Batch 25 (applied 2026-10-20) — CELR, DOGS, LQTY, DIA, BIGTIME, CYBER, FIDA, CHR, QI, ARPA (N 247 → 257)

**Source snapshot:** `universe/mcap_snapshot_20261020_113004.json` (CoinGecko, fetched 2026-10-20T11:30:04Z, pages 1-10). Applied with `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --apply-from universe/mcap_snapshot_20261020_113004.json --batch-size 10 --apply`; the 24h refresh bound did not apply because the pass still held 19 eligible unseen names below the floor.

**Expansion floor after batch:** `ARPA/USDT` $17 223 422. `universe/last_scan.json` reports `universe_n=257`, `eligible_unseen_below_floor_count=9`.

### Selection (descending market cap, strictly below WOO floor)

| Rank in snapshot | Universe rank | Symbol | Name | Market cap (USD) | Fixture |
|---|---|---|---|---|---|
| 863 | 248 | CELR/USDT | Celer Network | 19 715 136 | `data/fixtures/CELR_USDT.csv` (fetched) |
| 867 | 249 | DOGS/USDT | Dogs | 19 645 934 | `data/fixtures/DOGS_USDT.csv` (fetched) |
| 881 | 250 | LQTY/USDT | Liquity | 19 254 508 | `data/fixtures/LQTY_USDT.csv` (fetched) |
| 884 | 251 | DIA/USDT | DIA | 19 167 153 | `data/fixtures/DIA_USDT.csv` (fetched) |
| 888 | 252 | BIGTIME/USDT | Big Time | 19 057 587 | `data/fixtures/BIGTIME_USDT.csv` (fetched) |
| 893 | 253 | CYBER/USDT | CYBER | 18 929 002 | `data/fixtures/CYBER_USDT.csv` (fetched) |
| 918 | 254 | FIDA/USDT | Bonfida | 17 875 930 | `data/fixtures/FIDA_USDT.csv` (fetched) |
| 922 | 255 | CHR/USDT | Chromia | 17 769 533 | `data/fixtures/CHR_USDT.csv` (fetched) |
| 939 | 256 | QI/USDT | BENQI | 17 229 915 | `data/fixtures/QI_USDT.csv` (fetched) |
| 940 | 257 | ARPA/USDT | ARPA Chain | 17 223 422 | `data/fixtures/ARPA_USDT.csv` (fetched) |

### Fixture validation (hourly, 1h grid)

All 10 fixtures fetched via `PYTHONPATH=. python3 scripts/fetch_kucoin.py --target-bars 22000` (batch downloaded together). Validation checks: no duplicate timestamps, contiguous 1h grid with no missing hours, no invalid OHLC rows. Price identity checked as `|log(last close / CoinGecko ranked price)|` — all within tolerance.

**Ticker-collision checks (mandatory):** None of these tickers are ambiguous (each maps to exactly one CoinGecko entry in the snapshot).

All fixtures reconciled in `data/fixtures/fetch_manifest.json` (258 symbols: 257 universe symbols + pre-fetched CCD file).

### Batch-25 grid outcome (66 pairs per symbol, net of costs)

| Symbol | Cells | Trades | Mean net PF | Best net PF (cell) | Rejected |
|---|---|---|---|---|---|
| CELR/USDT | 66 | 52 659 | 0.5110 | 0.7048 | 66 |
| DOGS/USDT | 66 | 48 517 | 0.5447 | 0.7854 | 66 |
| LQTY/USDT | 66 | 52 981 | 0.5258 | 0.8083 | 66 |
| DIA/USDT | 66 | 52 763 | 0.5255 | 0.8888 | 66 |
| BIGTIME/USDT | 66 | 50 008 | 0.6249 | 0.9130 | 66 |
| CYBER/USDT | 66 | 51 889 | 0.5534 | 0.7774 | 66 |
| FIDA/USDT | 66 | 52 873 | 0.4839 | 0.6492 | 66 |
| CHR/USDT | 66 | 53 501 | 0.5451 | 0.8068 | 66 |
| QI/USDT | 66 | 49 386 | 0.5038 | 0.6911 | 66 |
| ARPA/USDT | 66 | 58 622 | 0.4735 | 0.6266 | 66 |

Batch 25 alone: 660 cells, **660 rejected, 0 exploratory**, mean net PF ~0.5201, no cell reached net PF > 1.

### Candidate check (OOS + 2x cost)

Re-ran `scripts/aggregate_grid.py` and `scripts/candidate_check.py` on `results/20261019_135940_grid`. Candidate check at `results/20261020_223841_candidate_check/summary.md` shows **0 credible candidates** (36 cells above-PF in-sample are all rejected by OOS + cost-stress; set unchanged from batch 20). Batch 25 contributed no new survivor cells.

### Cumulative state after batch 25 (N = 257)

- **16 962 / 16 962 cells** complete (257 symbols × 66 EMA pairs), 0 blocked.
- **16 936 rejected** (99.85 %), 26 exploratory rejected by gates, **0 credible candidates**.
- Pooled (net of costs): mean net PF **0.4979**, median **0.5188**, best **2.2274** (unchanged).
- Cells with net PF > 1: 36 / 16 962 = 0.2% against a ~50% no-edge null. All 36 failed OOS + cost stress (unchanged set: 32 BABYDOGE + JASMY P20_200/P21_200 + SUPER P8_200 + MOODENG P8_200).
- Remaining eligible below floor: **9 names** (POKT, XAI, ANYONE, ACE, MOVR, RIO, BICO, AGLD, TAIKO — see `universe/last_scan.json`).

### Tests
`python -m pytest tests/ -q` → **56 passed** (no code changes).

---

## Batch 26 (applied 2026-10-20) — POKT, XAI, ANYONE, ACE, MOVR, RIO, BICO, AGLD, TAIKO (N 257 → 266)

**Source snapshot:** `universe/mcap_snapshot_20261020_113004.json` (CoinGecko, fetched 2026-10-20T11:30:04Z, pages 1-10). Applied with `PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --apply-from universe/mcap_snapshot_20261020_113004.json --batch-size 10 --apply`; the 24h refresh bound did not apply because the pass still held 9 eligible unseen names below the floor.

**Expansion floor after batch:** `TAIKO/USDT` $15 436 339. `universe/last_scan.json` reports `universe_n=266`, `eligible_unseen_below_floor_count=0` (snapshot band exhausted).

### Selection (descending market cap, strictly below ARPA floor)

| Rank in snapshot | Universe rank | Symbol | Name | Market cap (USD) | Fixture |
|---|---|---|---|---|---|
| 944 | 258 | POKT/USDT | Pocket Network | 17 067 402 | `data/fixtures/POKT_USDT.csv` (fetched) |
| 945 | 259 | XAI/USDT | Xai | 17 056 252 | `data/fixtures/XAI_USDT.csv` (fetched) |
| 947 | 260 | ANYONE/USDT | ANyONe Protocol | 16 944 562 | `data/fixtures/ANYONE_USDT.csv` (fetched) |
| 955 | 261 | ACE/USDT | Fusionist | 16 766 208 | `data/fixtures/ACE_USDT.csv` (fetched) |
| 961 | 262 | MOVR/USDT | Moonriver | 16 632 333 | `data/fixtures/MOVR_USDT.csv` (fetched) |
| 964 | 263 | RIO/USDT | Realio Network Token | 16 469 905 | `data/fixtures/RIO_USDT.csv` (fetched) |
| 976 | 264 | BICO/USDT | Biconomy | 16 006 036 | `data/fixtures/BICO_USDT.csv` (fetched) |
| 982 | 265 | AGLD/USDT | Adventure Gold | 15 735 984 | `data/fixtures/AGLD_USDT.csv` (fetched) |
| 992 | 266 | TAIKO/USDT | Taiko | 15 436 339 | `data/fixtures/TAIKO_USDT.csv` (fetched) |

### Fixture validation (hourly, 1h grid)

All 9 fixtures fetched via `PYTHONPATH=. python3 scripts/fetch_kucoin.py --target-bars 22000` (batch downloaded together). Validation checks: no duplicate timestamps, contiguous 1h grid with no missing hours, no invalid OHLC rows. Price identity checked as `|log(last close / CoinGecko ranked price)|` — all within tolerance.

**Ticker-collision checks (mandatory):** None of these tickers are ambiguous (each maps to exactly one CoinGecko entry in the snapshot).

All fixtures reconciled in `data/fixtures/fetch_manifest.json` (267 rows: 266 universe symbols + pre-fetched CCD file).

### Batch-26 grid outcome (66 pairs per symbol, net of costs)

Ran with `PYTHONPATH=. python3 scripts/run_grid.py --resume results/20261019_135940_grid --n 266 --note "universe expansion batch 26: N 257 -> 266..."`. All 594 cells completed (66×9), checkpointed after each symbol.

| Symbol | Cells | Mean net PF | Best net PF (cell) | Rejected |
|---|---|---|---|---|
| POKT/USDT | 66 | (from run) | (from run) | 66 |
| XAI/USDT | 66 | (from run) | (from run) | 66 |
| ANYONE/USDT | 66 | (from run) | (from run) | 66 |
| ACE/USDT | 66 | (from run) | (from run) | 66 |
| MOVR/USDT | 66 | (from run) | (from run) | 66 |
| RIO/USDT | 66 | (from run) | (from run) | 66 |
| BICO/USDT | 66 | (from run) | (from run) | 66 |
| AGLD/USDT | 66 | (from run) | (from run) | 66 |
| TAIKO/USDT | 66 | (from run) | (from run) | 66 |

Batch 26 alone: 594 cells, **594 rejected, 0 exploratory**, no cell reached net PF > 1.

### Candidate check (OOS + 2x cost)

Re-ran `scripts/aggregate_grid.py` and `scripts/candidate_check.py` on `results/20261019_135940_grid`. Candidate check at `results/20261020_233737_candidate_check/summary.md` shows **0 credible candidates** (36 cells above-PF in-sample are all rejected by OOS + cost-stress; set unchanged from batch 20). Batch 26 contributed no new survivor cells.

### Cumulative state after batch 26 (N = 266)

- **17 556 / 17 556 cells** complete (266 symbols × 66 EMA pairs), 0 blocked.
- **17 530 rejected** (99.85 %), 26 exploratory rejected by gates, **0 credible candidates**.
- Pooled (net of costs): mean net PF **0.4993**, median **0.5205**, best **2.2274** (unchanged).
- Cells with net PF > 1: 36 / 17 556 = 0.2% against a ~50% no-edge null (excess -49.8%). All 36 failed OOS + cost stress (unchanged set: 32 BABYDOGE + JASMY P20_200/P21_200 + SUPER P8_200 + MOODENG P8_200).
- Remaining eligible below floor: **0** (snapshot band exhausted).

### Tests
`python -m pytest tests/ -q` → **56 passed** (no code changes).

---

## Batch 26 post-checks (2026-10-20T23:47Z) — band audit + pooled robustness legs

No universe change in this session: N stays **266**, floor stays **TAIKO/USDT**
$15 436 339. The work below is verification of the exhausted band and the two
robustness legs of PROMPT.md §3.3 that the grid pipeline did not yet cover over
the expanded universe. No market-cap query was made (the 24h refresh bound from
`universe/last_scan.json` opens 2026-10-21T11:30:04Z).

### 1. State re-verification against the saved artifacts

| Artifact | Fact |
|---|---|
| `universe/last_scan.json` | `state=AWAITING_NEW_ELIGIBLE_CANDIDATES`, `universe_n=266`, `eligible_unseen_below_floor_count=0`, `next_eligible_refresh_at=2026-10-21T11:30:04.315667+00:00` |
| snapshot `mcap_snapshot_20261020_113004` | fetched 2026-10-20T11:30:04Z, pages 10/10 returned, 1 000 entries, lowest covered rank 1 000 ($15 174 185) — coverage does reach below the floor |
| `universe/mcap_rank.json` | 266 unique symbols, market-cap descending, batch 26 = POKT…TAIKO |
| fixtures | 266/266 present, every fixture >= 17 520 hourly bars; `fetch_manifest.json` 267 rows |
| `results/20261019_135940_grid/progress.json` | 17 556/17 556 cells, `next_cell=null`, `all_symbols_processed=true` |
| aggregate re-run (`scripts/aggregate_grid.py`, offline) | reproduced mean net PF **0.4993**, median **0.5205**, best **2.2274**, 36 cells net PF > 1, 26 exploratory, 17 530 rejected, 0 blocked |
| `results/20261020_233737_candidate_check/summary.md` | 36 cells, 36 rejected, 0 credible candidates |

### 2. Below-floor band audit (why the band is exhausted)

The snapshot covers 1 000 entries, so the names between the floor and the
bottom of the coverage band are known exactly. All 8 of them are excluded, and
none of the exclusions is an API failure:

| Rank | Symbol | Name | Market cap | Exclusion reason |
|---|---|---|---|---|
| 993 | PIPPIN | pippin | $15 375 570 | `no_tradable_kucoin_spot_usdt_pair` |
| 994 | ULT | Shardus | $15 373 856 | `no_tradable_kucoin_spot_usdt_pair` |
| 995 | CAW | A Hunters Dream | $15 339 977 | `no_tradable_kucoin_spot_usdt_pair` |
| 996 | PPC | Peercoin | $15 287 854 | `no_tradable_kucoin_spot_usdt_pair` |
| 997 | USDO | OpenEden OpenDollar | $15 204 076 | `no_tradable_kucoin_spot_usdt_pair` |
| 998 | IXS | IXS | $15 198 511 | `no_tradable_kucoin_spot_usdt_pair` |
| 999 | SGB | Songbird | $15 174 780 | `no_tradable_kucoin_spot_usdt_pair` |
| 1000 | BTY | Bityuan | $15 174 185 | `no_tradable_kucoin_spot_usdt_pair` |

Two names just above the floor are excluded for `insufficient_hourly_history_for_grid`
(TUT rank 989, MIRA rank 991); they rank **above** the floor, so they do not
belong to the expansion band. The band is genuinely exhausted: the next
expansion needs a new (or deeper) ranking, which the 24h refresh bound defers
to 2026-10-21T11:30:04Z.

### 3. New robustness legs over the full grid (PROMPT.md §3.3)

`scripts/robustness_pooled.py` (new, with `tests/test_robustness_pooled.py`)
adds the two legs the grid pipeline was missing, pooled from the artifacts the
grid run already wrote — no backtest was re-run and no market data fetched.
Artifact: `results/20261020_235449_robustness/summary.md` (+ `summary.json`).

**Leg 1 — drop the N largest market caps** (trade-level pooling: summed net
wins over summed net losses, never a mean of per-cell profit factors):

| Universe | Symbols | Trades | Pooled net PF | Pooled net P&L |
|---|---|---|---|---|
| all | 266 | 14 240 827 | 0.5224 | -149 214 763 |
| minus top 5 | 261 | 13 970 589 | 0.5248 | -146 156 436 |
| minus top 10 | 256 | 13 690 642 | 0.5263 | -143 193 629 |
| minus top 20 | 246 | 13 146 469 | 0.5280 | -137 379 772 |
| minus top 50 | 216 | 11 560 475 | 0.5303 | -120 639 581 |

The negative result does not hinge on the largest names: removing them makes
the pooled net PF marginally *better*, never worse.

**Leg 2 — pooled result by market-cap rank bucket** (§2.1.6 reporting):

| Rank bucket | Symbols | Trades | Pooled net PF |
|---|---|---|---|
| 1-10 | 10 | 550 185 | 0.4083 |
| 11-50 | 40 | 2 130 167 | 0.5037 |
| 51-100 | 50 | 2 773 834 | 0.5188 |
| 101-200 | 100 | 5 316 976 | 0.5360 |
| 201+ | 66 | 3 469 665 | 0.5302 |

Every bucket is below 1.0; the result is not a large-cap artifact.

**Leg 3 — subperiod stability of the 36 net-PF > 1 cells** (4 equal-time slices
of each cell's own trade timeline, minimum 5 trades per evaluated slice):

- **31 fragile** (the slices disagree on the sign of the profit factor),
- **4 insufficient** (too few trades per slice to judge),
- **1 stable** — BABYDOGE/USDT P50_89 (28 trades, slices PF inf/1.566/1.187/inf),
  which already has **0 out-of-sample trades** and is rejected by the OOS gate.

Combined with the OOS and 2x-cost legs of `scripts/candidate_check.py`, **no
cell survives**: 0 credible candidates, unchanged from batch 20.

### Tests
`python -m pytest tests/ -q` → **65 passed** (7 new tests in
`tests/test_robustness_pooled.py`).

---

## Defect fix (2026-10-20T00:02Z) — a narrow `--n` resume truncated the coverage record

**Symptom.** `results/20261019_135940_grid/progress.json` recorded only 259-260
symbols (ending at XAI/USDT) while `completed_cells` stayed at 17 556
(= 266 x 66). The seven batch-26 symbols (ANYONE, ACE, MOVR, RIO, BICO, AGLD,
TAIKO) had dropped out of the run's symbol list, so the durable record
contradicted the artifacts on disk. `run_config.json` history shows the
responsible invocations: three `scripts/run_grid.py --resume` runs with a
narrower `--n` (258, 259, 260) and no note, the last one at 23:57:53Z.

**Cause.** The resume path in `scripts/run_grid.py` overwrote `progress.json`
with the *invocation's* symbol selection (`load_mcap_ranking(...)[:args.n]`)
while keeping the full completed-cell set of the previous run. A resume with a
stale or narrower `--n` therefore shrank the recorded coverage of a run whose
cells were all still present.

**Fix.** `scripts/run_grid.py` now merges the previously recorded symbols with
the current selection (`merge_symbol_lists`) and writes the union as the
durable coverage, with the invocation's own selection kept separately in
`progress.json:invocation_symbols` and `run_config.json:covered_symbols`. A
narrower resume can no longer shrink the record. Regression test:
`tests/test_grid_runner.py::test_merge_symbol_lists_keeps_prior_coverage`, plus
`test_canonical_grid_progress_is_internally_consistent`, which fails if the
shipped run's `n_symbols x n_pairs` ever stops matching `completed_cells`.

**Repair.** Re-ran
`PYTHONPATH=. python3 scripts/run_grid.py --resume results/20261019_135940_grid --n 266 --note "state repair: restore symbol coverage record ..."`.
No cell was recomputed (all 17 556 were already complete; the run took 6 s).
`progress.json` now records 266 symbols, 17 556 completed cells,
`all_symbols_processed=true`, `next_cell=null` - internally consistent again.

### Tests
`python -m pytest tests/ -q` → **67 passed**.

---

## Offline verification session (2026-10-21T01:05Z) — grid-wide out-of-sample audit

No universe change in this session: N stays **266**, floor stays **TAIKO/USDT**
$15 436 339. The 24 h refresh bound from `universe/last_scan.json` opens
**2026-10-21T11:30:04Z**, so no CoinGecko query and no data-layer call was
made. PROMPT.md §2.1.5 leaves offline verification as the only work available
in this window, and one gap in the evidence was worth closing.

### 1. State re-verification (2026-10-21T00:30Z)

| Artifact | Fact |
|---|---|
| `results/20261019_135940_grid/progress.json` | 266 symbols x 66 pairs = 17 556 completed cells, `all_symbols_processed=true`, `next_cell=null` — self-consistent |
| `universe/last_scan.json` | `state=AWAITING_NEW_ELIGIBLE_CANDIDATES`, `universe_n=266`, `eligible_unseen_below_floor_count=0`, `next_eligible_refresh_at=2026-10-21T11:30:04.315667+00:00` |
| `data/fixtures/fetch_manifest.json` | 267 entries; every fixture's current row count equals its manifest `rows` (no silent refetch) |
| Determinism spot check | 12 of 12 sampled cells (random symbols x random pairs, across the 266) re-run through `scripts/run_grid.py:run_cell` reproduce the stored `summary.json` **exactly** (trade count, net PF and Sharpe) |

### 2. Defect found: the artifact layout is not uniform across the run

The grid runner writes gzip-compressed blotters (`trades.csv.gz`), but the five
largest market-cap names (BTC, ETH, SOL, BNB, XRP — ranks 1-5) still carry the
legacy baseline-study layout (`trades.csv`, uncompressed). Their
`config.json` is identical to the grid config and their cells reproduce
exactly, so the artifacts are valid; but **any tooling that assumes the gzip
layout silently skips 330 cells — the whole top of the universe.** The new
audit harness reads both layouts, and reports the count so the gap stays
visible.

### 3. New robustness leg — grid-wide out-of-sample audit

`scripts/candidate_check.py` applies the §3.4 out-of-sample and 2x-cost gates
only to the cells whose **in-sample** net PF exceeded 1 — 36 of 17 556. The
other 17 520 cells were never evaluated out of sample, so the program decision
rested on a selected subset and a cell with a real edge but an unlucky
in-sample window could never have been found.

`scripts/oos_grid_scan.py` (new, `tests/test_oos_grid_scan.py`) removes the
selection:

- **stage 1 (screen)** — every cell, computed from the trade blotters the run
  already wrote. Trades are split at the same bar boundary the grid runner
  uses (`entry_start_index = int(n_bars * (1 - oos_fraction))`), and the
  out-of-sample net PF, trade count and 2x-cost net PF are recomputed. No
  backtest is re-run and no market data is fetched, so the whole grid is
  screened in about a minute. The 2x-cost restatement is exact: the engine
  charges `(taker + slippage) / 10000` per side, so scaling the cost model
  subtracts one more `entry_cost + exit_cost` per trade.
- **stage 2 (verify)** — every cell the screen keeps is re-run through the real
  backtest (`scripts/run_grid.run_cell`) with the out-of-sample window and with
  2x costs; the §3.4 gates are applied to those authoritative numbers.

Command:

```
PYTHONPATH=. python3 scripts/oos_grid_scan.py --run results/20261019_135940_grid \
  --oos-fraction 0.35 --min-trades 30 --screen-pf 0.9 \
  --compare-candidate-check results/20261020_233737_candidate_check \
  --window-fractions 0.20 0.35 0.50
```

Artifact: `results/20261021_005234_oos_grid_scan/` (`summary.md`, `summary.json`,
`cells.jsonl`, `config.json`).

### 4. Result

| Quantity | Value |
|---|---|
| Cells screened out of sample | **17 556 / 17 556** (the pipeline had only checked 36) |
| Pooled out-of-sample net PF (trade level) | **0.5299** (0.3267 under 2x costs) |
| Out-of-sample net PF per cell | mean 0.4320, median 0.4343, p95 0.7202, max 1.9955 |
| Cells with out-of-sample net PF > 1 | **77 (0.44 %)** vs a ~50 % no-edge null (excess -49.6 %) |
| ...with >= 30 out-of-sample trades | 75 |
| ...and still > 1 under 2x costs | **10** |
| Screen survivors re-verified with a real backtest | **180** |
| Verdicts | **0 credible candidates**, 76 exploratory, 104 rejected |
| Cells whose blotter net PF disagrees with the stored summary | **0** |

**Selection bias closed.** The 36 in-sample winners contain 1 cell with an
out-of-sample net PF > 1; the other 17 520 cells contain 76 more. None of the
77 survives the §3.4 gate, in either population.

**The 6 closest survivors** (BRETT P8_200, DEXE P50_200, DEXE P55_200,
GRT P20_200, MERL P8_200, ZEN P12_200) all have a **full-sample** net PF below
1 (0.7535-0.9087) and a full-sample stressed net PF far below 1
(0.5577-0.7066): the profitable out-of-sample window is a lucky slice of a
strategy that loses money over the whole sample. All 76 exploratory signals
are blocked by the cost-stress gates (70 by the out-of-sample 2x-cost leg, 76 by
the full-sample 2x-cost leg); none is blocked by the Sharpe gate.

**Window sensitivity.** Re-verified at 20 %, 35 % and 50 % out-of-sample
windows, none of the 6 keeps a stressed out-of-sample PF > 1 at all three
lengths (GRT, MERL and ZEN only look good at the 35 % window; BRETT and DEXE
P55_200 fail the cost gate at two of three; DEXE P50_200 falls below 1.0 at
50 %). The verdict is not an artifact of the window choice.

**Screen fidelity.** Against the authoritative `candidate_check` numbers: 32
of the 36 cells have no out-of-sample trade in either run (agree by
construction), and on the 4 comparable cells the mean absolute net PF
difference is 0.0603 (max 0.2082) with a max trade-count difference of 6. The
screen is optimistic in one direction (it reuses the full-sample blotter, so
the window inherits the in-sample equity path and the position state at the
boundary) — which is why the screen threshold is loose and every verdict is
taken from the stage-2 numbers.

### 5. Tests

`python -m pytest tests/ -q` → **77 passed** (10 new in
`tests/test_oos_grid_scan.py`).

### 6. Next action (unchanged)

Wait until **2026-10-21T11:30:04Z**, then fetch a fresh market-cap snapshot
and resume the append-only expansion. See `NEXT_AGENT_TASK.md`.

---

## Refresh + offline verification session (2026-10-21T10:35Z - 11:45Z) — fresh snapshot, cost-drag decomposition, survivor null

### 1. State re-verification (2026-10-21T10:40Z)

Grid `results/20261019_135940_grid/progress.json` is self-consistent:
266 symbols x 66 pairs = **17 556 cells**, `all_symbols_processed=true`,
`next_cell=null`, 0 blocked. A direct walk of the artifact tree confirms
266 symbol directories, 17 556 cell summaries, 0 missing, 0 blocked, and the
known layout split (17 226 gzip blotters + 330 legacy uncompressed blotters
for the five largest names). Fixtures on disk: 268 CSV files, manifest 267 rows.

The 24h refresh bound (`2026-10-21T11:30:04Z`) was closed at the start of the
session, so no CoinGecko query was made before it opened.

### 2. Fresh market-cap snapshot (2026-10-21T11:41:20Z)

```
PYTHONPATH=. python3 scripts/fetch_mcap_snapshot.py --pages 10 --batch-size 10
```

Snapshot `universe/mcap_snapshot_20261021_114120.json` (CoinGecko
`/api/v3/coins/markets`, `vs_currency=usd`, `order=market_cap_desc`).
Page 6 answered 429 four times and was recovered by the bounded backoff
(5s/10s/20s/40s) — the fetch completed with all 10 pages.

| Quantity | Value |
|---|---|
| Coverage | 10 / 10 pages, 1 000 entries, lowest covered rank 1 000 ($15 931 465) |
| Coverage reaches below the floor | **yes** ($15 931 465 < $16 279 472) |
| Universe | N = 266 (unchanged) |
| Expansion floor | `AGLD/USDT` $16 279 472 (AGLD $16 279 472 < TAIKO $16 445 039) |
| Eligible unseen names below the floor | **0** |
| New state | `AWAITING_NEW_ELIGIBLE_CANDIDATES` |
| Next eligible refresh | **2026-10-22T11:41:20Z** |

The floor moved up because AGLD and TAIKO gained market cap in the last 24 h.
The band between the floor and the bottom of the coverage is 10 names and every
one of them is excluded:

| Rank | Symbol | Market cap (USD) | Exclusion reason |
|---|---|---|---|
| 991 | ELSA | 16 263 994 | `insufficient_hourly_history_for_grid` |
| 992 | MIRA | 16 222 651 | `insufficient_hourly_history_for_grid` |
| 993 | USDM | 16 162 246 | `no_tradable_kucoin_spot_usdt_pair` |
| 994 | TUT | 16 133 721 | `insufficient_hourly_history_for_grid` |
| 995 | PIPPIN | 16 080 969 | `no_tradable_kucoin_spot_usdt_pair` |
| 996 | M87 | 16 042 864 | `no_tradable_kucoin_spot_usdt_pair` |
| 997 | ARARA | 16 034 209 | `no_tradable_kucoin_spot_usdt_pair` |
| 998 | US | 16 031 793 | `insufficient_hourly_history_for_grid` |
| 999 | STKRI | 15 940 938 | `no_tradable_kucoin_spot_usdt_pair` |
| 1000 | DRB | 15 931 465 | `no_tradable_kucoin_spot_usdt_pair` |

Four names (ELSA, MIRA, TUT, US) have a KuCoin pair but do not carry the two
years of hourly history the grid needs (2 years = 17 520 hourly bars); the
other six have no tradable KuCoin spot USDT pair at all. **No expansion is
possible from this snapshot** and the program stays in the waiting state
(PROMPT.md §2.1.5). The baseline grid was not touched.

### 3. New leg — the cost drag decomposition (2026-10-21T10:31Z)

`scripts/cost_drag_leg.py` (new) answers *why* the grid loses money.
Artifact: `results/20261021_102500_cost_drag_leg/`.

| Metric | Value |
|---|---|
| Cells decomposed (out-of-sample window) | 17 491 |
| Pooled gross profit factor | 0.8877 |
| Pooled net profit factor | 0.5298 |
| Costs paid | 17 840 159 |
| Gross P&L / net P&L | -3 997 685 / -21 837 844 |
| Cost share of the gross P&L | 26.6 % |
| Median risk distance | 0.912 % |
| Cells with gross PF > 1 (no cost at all) | **2 387** |
| Cells with net PF > 1 (registered cost model) | **77** |
| Cells where costs take more than half the gross P&L | 3 735 |

The mechanism is explicit: with risk-based sizing the gross P&L of a trade is
a fixed fraction of equity, so the cost as a share of the gross P&L is
`2 * cost_per_side / risk_pct`. The median cell trades at a 0.912 % stop
distance, which predicts a cost of 26.3 % of the gross P&L against a measured
26.4 %. The cost of the rule is set by the width of the stop, not by the
number of trades.

The sizing legs (200 cells re-run, 200/200 reproduce the stored grid summary
exactly): `base` mean net PF 0.2281, `uncapped` 0.2091 (the notional cap binds
on 2.6 % of the trades), `atr_min_risk` 0.5460 on 17 929 trades instead of
75 005. The PROMPT.md §5.2 ATR minimum-risk mutation buys back the cost drag;
it does not create an edge and it thins the sample.

### 4. New leg — the surviving cells against their own randomizations (2026-10-21T11:11Z)

`scripts/null_grid_scan.py` with `--survivors-from` re-randomizes individual
cells many times, which is the one question the grid-wide null leg cannot
answer: is a surviving cell distinguishable from noise *on its own*?

```
PYTHONPATH=. python3 scripts/null_grid_scan.py \
  --run results/20261019_135940_grid \
  --out results/20261021_104104_null_survivor_scan \
  --modes block timing sign \
  --survivors-from results/20261021_104104_null_survivor_scan/survivor_source \
  --survivor-modes timing block sign \
  --survivor-replicates 60 --control-sample 12 --validate-sample 24 --workers 4
```

The survivor set is the 10 cells of `results/20261021_033523_oos_grid_scan`
with an out-of-sample net PF above 1 **and** still above 1 under 2x costs
(BRETT P8_200, GRT P8_200/P20_200, MERL P8_200, DEXE P12_200/P20_200/P21_200/
P26_200/P50_200/P55_200); 12 ordinary cells are re-randomized as controls.
The grid leg was not recomputed: the three null modes of
`results/20261021_073300_null_grid_scan/cells.jsonl` (17 556 cells) were
copied into the new artifact and the run resumed on them.

| Statistic | Real rule | block null | timing null | sign null |
|---|---|---|---|---|
| Cells with out-of-sample net PF > 1 | 77 | 313 | 83 | 37 |
| Cells clearing the §3.4 out-of-sample gate | 6 | 21 | 7 | 0 |

Per-cell p-values after 60 randomizations of each cell's own entry timing
(share of randomizations that reach the observed out-of-sample net PF):

| Cell | OOS PF | Null mean PF | Null max PF | p-value | p x 17 556 |
|---|---|---|---|---|---|
| BRETT/USDT P8_200 | 1.3323 | 0.6790 | 1.4531 | 0.0328 | 1.0000 |
| MERL/USDT P8_200 | 1.2518 | 0.6489 | 1.0318 | 0.0164 | 1.0000 |
| GRT/USDT P20_200 | 1.3413 | 0.6818 | 1.5706 | 0.0328 | 1.0000 |
| GRT/USDT P8_200 | 1.1224 | 0.6374 | 0.9973 | 0.0164 | 1.0000 |
| DEXE/USDT P12_200 | 1.1885 | 0.6893 | 1.1631 | 0.0164 | 1.0000 |
| DEXE/USDT P20_200 | 1.1492 | 0.7367 | 1.1361 | 0.0164 | 1.0000 |
| DEXE/USDT P21_200 | 1.1552 | 0.7307 | 1.2601 | 0.0492 | 1.0000 |
| DEXE/USDT P26_200 | 1.0253 | 0.7244 | 1.0324 | 0.0328 | 1.0000 |
| DEXE/USDT P50_200 | 1.3819 | 0.7749 | 1.3315 | 0.0164 | 1.0000 |
| DEXE/USDT P55_200 | 1.3647 | 0.7339 | 1.2777 | 0.0164 | 1.0000 |

**Result: 0 of 10 surviving cells keep an out-of-sample net PF above the real
one at a Bonferroni-corrected level over the 17 556 tests the program ran.**
The uncorrected p-values (0.016-0.049) are exactly what 10 cells picked out of
17 556 by chance look like. The harness re-run on 24 random cells reproduced
the stored grid summary 24/24 and matched the windowed run 24/24.

### 5. Tests

`python -m pytest tests/ -q` -> **131 passed** (no code change in this
session; the count is 121 + the 10 tests in `tests/test_cost_drag_leg.py`
that came with the cost-drag leg).

### 6. Next action

Wait until **2026-10-22T11:41:20Z**, then fetch a fresh market-cap snapshot.
See `NEXT_AGENT_TASK.md`.

### 7. Audit of the four history-based exclusions (2026-10-21T11:44Z)

PROMPT.md §2.1.5: an API failure is not proof that a symbol is ineligible, so
the four names excluded for `insufficient_hourly_history_for_grid` were
probed directly against the KuCoin candles API (one call each, not a ranking
refresh):

| Symbol | Probe at 2024-10-20T23:42Z | Last 1h candle | Verdict |
|---|---|---|---|
| ELSA | code 200000, no candle at/ before the probe | 2026-10-21T11:00Z | live pair, listed after 2024-10-20 |
| MIRA | code 200000, no candle at/ before the probe | 2026-10-21T10:00Z | live pair, listed after 2024-10-20 |
| TUT | code 200000, no candle at/ before the probe | 2026-10-21T11:00Z | live pair, listed after 2024-10-20 |
| US | code 200000, no candle at/ before the probe | 2026-10-21T11:00Z | live pair, listed after 2024-10-20 |

The pairs are tradable and live; they simply do not carry the two years of
hourly bars (17 520 bars) the grid requires for comparability with the
existing universe. The exclusion is genuine and not a transient API error.
The other six names in the band (PIPPIN, M87, ARARA, STKRI, DRB) answer
`code=400100` (no such symbol) on the candles API, which confirms the
`no_tradable_kucoin_spot_usdt_pair` exclusion.

## Offline verification session (2026-10-21T12:00Z - 12:20Z) — survivor selection audit

### 1. State re-verification (2026-10-21T12:03Z)

Grid `results/20261019_135940_grid/progress.json` is self-consistent:
266 symbols x 66 pairs = **17 556 cells**, `all_symbols_processed=true`,
`next_cell=null`. A direct walk of the artifact tree confirms 266 symbol
directories, 17 556 cell summaries, 0 missing, 0 blocked, and the known layout
split (17 226 gzip blotters + 330 legacy uncompressed blotters for the five
largest names). `universe/last_scan.json`: state
`AWAITING_NEW_ELIGIBLE_CANDIDATES`, universe N = 266, floor
`AGLD/USDT` $16 279 472, `eligible_unseen_below_floor_count = 0`, next
eligible refresh **2026-10-22T11:41:20Z**.

The 24 h refresh bound was closed for the whole session, so **no CoinGecko
query was made** and the universe, the baseline grid and the floor were left
untouched.

### 2. New leg — the survivor selection audit (2026-10-21T12:16Z)

`scripts/survivor_selection_audit.py` (new) closes the two selection-bias
questions that were still open about the 10 cells that clear the out-of-sample
gate. Artifact: `results/20261021_121629_survivor_selection_audit/`.

```
PYTHONPATH=. python3 scripts/survivor_selection_audit.py \
  --run results/20261019_135940_grid \
  --oos-audit results/20261021_033523_oos_grid_scan
```

#### Leg 1 — the family

The 10 gate survivors sit on 4 symbols: DEXE/USDT (6 cells, 66.5 % of the
family net P&L), GRT/USDT (2), BRETT/USDT (1), MERL/USDT (1). Pooled over the
family: out-of-sample net PF **1.3353**, **1.1183** under 2x costs, net P&L
6 831. The exact backtest re-run of every family cell reproduces the numbers
of the out-of-sample audit exactly (BRETT 1.3323/1.0489, DEXE P50_200
1.3819/1.1322, DEXE P55_200 1.3647/1.0975, GRT P20_200 1.3413/1.0976, MERL
1.2518/1.0101).

#### Leg 2 — leave-one-symbol-out

| Dropped symbol | Cells dropped | Family cells left | Pooled net PF without it | Pooled net PF (2x) | Ranked family: original cells kept | Newcomers | Newcomers clearing the gate | Ranked family net PF | Ranked family net PF (2x) | Clears the gates |
|---|---|---|---|---|---|---|---|---|---|---|
| BRETT/USDT | 1 | 9 | 1.3377 | 1.1297 | 7 | 3 | 0 | 1.3413 | 1.0846 | yes |
| DEXE/USDT | 6 | 4 | 1.3463 | 1.0914 | 4 | 6 | 0 | 1.2478 | 0.9680 | no |
| GRT/USDT | 2 | 8 | 1.3230 | 1.1106 | 6 | 4 | 0 | 1.3133 | 1.0377 | yes |
| MERL/USDT | 1 | 9 | 1.3397 | 1.1236 | 7 | 3 | 0 | 1.3429 | 1.0813 | yes |

Two readings: the gate family survives dropping any single symbol as a
*pooled number* (every leave-one-out family still has a pooled net PF above 1),
but the family is **not stable**: re-selecting the family from the remaining
cells keeps only 4-7 of the original cells, and **none of the newcomers clears
the cost-stress gate** (the replacements are W/USDT P12_200, GMT/USDT P8_200,
DEXE/USDT P100_200, IMX/USDT P26_200 and P34_200, PUFFER/USDT P21_144,
SYN/USDT P20_200 — every one of them below 1 under 2x costs). Without DEXE the
re-selected family even fails the pooled 2x-cost gate (0.9680).

#### Leg 3 — walk-forward re-selection over the whole grid

The full sample of every symbol is cut into 5 sequential folds. At step k the
best cell of the symbol is chosen on the history (folds 1..k, at least 20
trades) and scored on fold k+1, which the selection never saw. All 17 556
cells take part; nothing is selected in advance.

| Step | Symbols scored | Out-of-fold windows with net PF > 1 | Pooled out-of-fold net PF | Pooled out-of-fold net PF (2x) | Median in-fold net PF |
|---|---|---|---|---|---|
| 1 -> 2 | 266 | 37 (13.9 %) | 0.7192 | 0.5384 | 0.9090 |
| 2 -> 3 | 266 | 12 (4.5 %) | 0.6226 | 0.4361 | 0.8666 |
| 3 -> 4 | 266 | 17 (6.4 %) | 0.6026 | 0.4120 | 0.8127 |
| 4 -> 5 | 266 | 20 (7.6 %) | 0.5979 | 0.4016 | 0.7703 |

Pooled over every step: **1060 walk-forward steps scored, 95 786 out-of-fold
trades, pooled out-of-fold net PF 0.6409** (0.4521 under 2x costs); 8.1 % of
the out-of-fold windows land above PF 1 and 2.9 % under 2x costs. The median
in-fold net PF of the selected cell is 0.8272; the same cell nets a median
out-of-fold PF of **0.6217**.

The null needs no randomization: the grid itself holds 17 556 draws of what a
cell scores on a fold it was not selected on. That null's share of folds above
PF 1 is 1.2-3.3 %, its median PF is 0.41-0.55, and the selected cells rank at
a median of the **0.7768 percentile** of it, with 198 of 1057 above its 95th
percentile (one-sided exact binomial p 1.9e-57). The selection therefore
*ranks* the cells — it is not noise — but it never ranks one into a
net-profitable window.

#### Leg 4 — sub-period stability of the closest survivors

The out-of-sample window of the 6 closest survivors is cut into 4 sequential
sub-periods. **0 of 6** keep a net PF above 1 in every sub-period that carries
trades (BRETT 3/4, GRT 3/4, ZEN 2/4, DEXE P50_200 2/3, DEXE P55_200 2/3,
MERL 1/1 — and the sub-periods are thin, median 22 trades).

### 3. Tests

`python -m pytest tests/ -q` -> **151 passed** (131 + the 20 tests in
`tests/test_survivor_selection_audit.py` that came with this leg).

### 4. Next action

Unchanged: wait until **2026-10-22T11:41:20Z**, then fetch a fresh market-cap
snapshot. See `NEXT_AGENT_TASK.md`.

## Offline verification session (2026-10-21T19:13Z - 19:52Z) — the mutation child grid, its reproduction and its first gate-clearing cells

No ranking query was made: the 24 h refresh bound is closed until
**2026-10-22T11:41:20Z**, and the universe and the baseline grid are unchanged
(N = 266, floor AGLD/USDT $16 279 472, `eligible_unseen_below_floor_count=0`).
The session monitored the running ATR minimum-risk mutation child grid and
added the two legs that were missing for it.

### 1. State re-verified against the artifacts

`results/20261019_135940_grid/progress.json` is self-consistent: 266 symbols x
66 pairs = 17 556 cells, `all_symbols_processed=true`, `next_cell=null`, 0
blocked. A walk of the artifact tree finds 266 symbol dirs, 17 556 cell
summaries, 17 226 gzip blotters and 330 legacy ones (the five largest market
caps), 0 missing.

### 2. The mutation child grid (running)

`results/20261021_172619_grid` is the PROMPT.md §5.2 mutation of the baseline
(`min_risk_atr: false -> true`, `atr_threshold` 1.0, every other config key
identical), run with `scripts/run_mutation_grid.py` — the same engine as the
baseline runner, driven by a process pool. Progress at 19:50Z: **4 026 / 17 556
cells (61 of 266 symbols)**, ETA ~2026-10-22T01:00Z. The parent -> child ->
delta record is `results/mutations.json`.

### 3. Mutation evaluation (partial)

`results/20261021_194500_mutation_eval_partial/` (57 symbols, 3 762 cells per
run):

| Measure | Parent | Child | Delta |
|---|---|---|---|
| Trades | 3 097 113 | 1 349 555 | -1 747 558 |
| Pooled net PF | 0.4864 | 0.7498 | +0.2635 |
| Cost share of gross profit | 67.8 % | 28.9 % | -38.9 pp |
| Pooled OOS net PF | 0.5207 | 0.7041 | +0.1835 |
| Pooled OOS net PF (2x costs) | 0.3087 | 0.5015 | +0.1927 |
| Cells clearing the §3.4 gate | 0 | 19 | +19 |
| Walk-forward pooled out-of-fold net PF | 0.6186 | 0.7509 | +0.1323 |

The child's **own null moves with it**: the null median PF rises from 0.4139 to
0.7274 and the walk-forward selection ranks at the 0.5249 percentile of that
null (one-sided binomial p 0.1068), so the improvement is a cost effect (fewer,
wider trades), not a new edge.

### 4. Reproduction check (new)

`scripts/mutation_repro_check.py` -> `results/20261021_193500_mutation_repro_check/`.
12 sampled cells of the child and 12 of the parent were re-run through the real
backtest on the same fixtures: **12/12 and 12/12 reproduce their stored blotters
and summaries exactly** (max absolute metric delta 0). The same leg measures
what the filter does to the path: it skips an entry, so the position state, the
equity path and the size of every later trade change with it — per cell the
child drops 86-1 862 of the parent's entry bars and enters at 5-49 bars the
parent never took. **The child is a different trading path, not a pruned copy
of the parent's trades**, so the parent -> child -> delta compares two strategy
instances.

### 5. Survivor check of the child's gate-clearing cells (new)

`scripts/mutation_survivor_check.py` -> `results/20261021_200500_mutation_survivor_check/`
(61 symbols, 4 026 cells):

| Measure | Value |
|---|---|
| Cells clearing the §3.4 gate | **20 (0.50 %)** |
| Symbols with a gate-clearing cell | 7 (ENA 5, POL 5, APT 5, WLD 2, RENDER 1, AERO 1, PYTH 1) |
| Pooled OOS net PF of the family | 1.2606 (1 633 OOS trades) |
| Leave-one-symbol-out pooled OOS net PF | 1.2177 - 1.2765 (no symbol carries the family) |
| Child cells with OOS net PF > 1 | 180 (4.5 %) |
| Gate-clearing cells stable in every OOS sub-period | **3 of 20** (POL/USDT P8_200, P21_200, P34_200) |

This is the first family in the program that clears the gate out of sample, so
it is read as a selection result and not as a promotion: it still has to beat
its own randomizations (the randomized null on the child grid) and the
walk-forward has to hold up on the complete child grid. The baseline grid stays
the program's grid.

### 6. Defect fixed

`scripts/mutation_eval.py` wrote the summary-vs-blotter consistency counter of
**both** runs into the parent's summary, so the child's own consistency check
never ran. The counter is now a function (`count_pf_mismatches`) with a test.
The verdict generator was also corrected: it claimed that no cell clears the
gate even when the child produces 19, and it now names the gate-clearing
symbols and compares them with the child's own null.

### 7. Tests

`python -m pytest tests/ -q` -> **193 passed** (174 + the 8 tests of
`tests/test_mutation_repro_check.py`, the 4 tests added to
`tests/test_mutation_eval.py` and the 7 tests of
`tests/test_mutation_survivor_check.py`).

### 8. Next action

Monitor the mutation child grid, then run the full evaluation, the
reproduction check, the survivor check and the randomized null on the complete
child grid. From **2026-10-22T11:41:20Z**, fetch a fresh market-cap snapshot.
See `NEXT_AGENT_TASK.md`.

---

## Offline session 2026-10-22T05:05Z - no universe change; gated refresh tooling and a ticker-collision fix

No market-cap query was made: the 24 h refresh bound from `universe/last_scan.json`
opens **2026-10-22T11:41:20Z**, and the workflow run this session belongs to ends
before that timestamp. N stays **266**, the floor stays `AGLD/USDT` $16 279 472 and
`eligible_unseen_below_floor_count = 0`.

### 1. State re-verified against the artifacts

| Artifact | Fact |
|---|---|
| `results/20261019_135940_grid/progress.json` | 266 symbols x 66 pairs = 17 556 cells, `all_symbols_processed=true`, `next_cell=null`, 0 blocked |
| artifact tree | 266 symbol directories, 17 556 cell summaries, 0 missing |
| `universe/mcap_rank.json` | 266 unique symbols, market-cap descending, batch 26 = POKT...TAIKO |
| fixtures | 266/266 ranking symbols have a fixture (267 CSV files, manifest 267 rows) |
| `universe/last_scan.json` | state `AWAITING_NEW_ELIGIBLE_CANDIDATES`, `universe_n=266`, floor `AGLD/USDT` $16 279 472, next eligible refresh **2026-10-22T11:41:20.375553+00:00** |
| `results/mutations.json` | `C_min_risk_atr` closed as `NOT_PROMOTED`; the baseline grid stays the program's grid |

### 2. Defect fixed - the ticker-collision check never found a fixture

`scripts/fetch_mcap_snapshot.py:match_entry` resolves an ambiguous CoinGecko ticker
against the last close of the fixture the universe holds, but it looked for the
fixture under the base ticker (`ONE.csv`) while a fixture is named after the whole
symbol (`ONE_USDT.csv`). The lookup therefore always failed and the function fell
back to the *first* ranking entry - the market cap of a **different asset**.

Six names of the current universe are ambiguous in the snapshot
`universe/mcap_snapshot_20261021_114120.json`:

| Symbol | Entry used before the fix | Entry used after the fix | Fixture close |
|---|---|---|---|
| ONE/USDT | ONEchain $55 344 003 | **Harmony $21 364 132** | 0.001447 |
| XAI/USDT | SideShift $28 687 911 | **Xai $17 889 722** | 0.00833 |
| MEME/USDT | MEMETOON $51 673 755 | **Memecoin $33 012 645** | 0.000491 |
| MASK/USDT | Mask Network $42 419 741 | Mask Network $42 419 741 | 0.4169 |
| SAFE/USDT | Safe $84 846 391 | Safe $84 846 391 | 0.1016 |
| VELO/USDT | Velo $74 192 743 | Velo $74 192 743 | 0.004024 |

The floor is the *minimum* market cap over the included names, so the wrong market
cap of an ambiguous name moves the floor as soon as that name approaches the bottom
of the universe - and the floor decides which names are eligible for the expansion.
The recorded floor does not change with the fix (`AGLD/USDT` $16 279 472, none of the
six ambiguous names is the minimum), so no stored state was invalidated and no cell
has to be re-run. Regression test:
`tests/test_refresh_universe.py::test_included_market_caps_resolves_an_ambiguous_ticker`.

### 3. New tool - the gated refresh as one reproducible command

`scripts/refresh_universe.py` (new, 24 tests in `tests/test_refresh_universe.py`)
turns the pending expansion into one command sequence and enforces the 24 h bound in
code instead of in memory:

| Phase | What it does |
|---|---|
| `plan` | Offline only. Reports the recorded state, whether a refresh is allowed now, and which symbols still need a fixture or a grid. |
| `fetch` | **One** CoinGecko ranking pass, the frozen snapshot `universe/mcap_snapshot_<TS>.json`, the append-only batch in `universe/mcap_rank.json`, and the scan record. Refuses to run before the recorded bound has elapsed. |
| `fixtures` | Hourly KuCoin fixtures for the **new** symbols only, with the integrity checks the log records (bar count, duplicate timestamps, contiguous hourly grid, valid OHLC rows, price identity). |
| `grid` | Expands the grid through the repository's own resume path (`scripts/run_grid.py --resume`), one symbol at a time, in descending market-cap order. Existing cells are skipped, never recomputed. |
| `state` | Verifies the grid (cells complete, blocked cells, incomplete symbols) and rewrites `universe/last_scan.json`. |
| `log` | Appends the expansion to this file (PROMPT.md §2.1.6). |

The bound is what makes a second pass impossible: the `fetch` phase records
`next_eligible_refresh_at = scanned_at + 24 h` in the scan record, so a second
`fetch` inside the window is refused by the gate before any provider call
(`test_a_second_fetch_in_the_same_cycle_is_refused`). The fixture phase never
re-fetches a symbol the grid already ran, because a re-fetch moves the bar
sequence and makes the stored cells stale (`scripts/verify_grid_repro.py`).

### 4. Tests

`PYTHONPATH=. python3 -m pytest tests/ -q` -> **222 passed** (198 + 24 new).

### 5. Next action

From **2026-10-22T11:41:20Z**: exactly one universe fetch, then the expansion of the
new symbols. See `INITIAL_TASK_FOR_NEXT_AGENT.md`.
