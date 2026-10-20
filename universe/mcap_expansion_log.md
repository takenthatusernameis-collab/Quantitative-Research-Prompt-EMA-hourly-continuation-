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
| SUPER/USDT | P8_200 | 1.0377 | +0.2611 | 0.9536 | -0.4627 | 78 | 0.8093 | 0.6975 | rejected |

**Every cell that has ever reached net PF > 1 in this program failed both
out-of-sample and cost stress**, so all of them are rejected rather than
promoted (PROMPT.md §3.4). The program's cumulative credible-candidate count
stays at **0** after 7 722 grid cells: an in-sample profit factor of ~1.03-1.04
is scan noise, exactly as the multiple-testing expectation predicted (0.04 % of
cells above 1.0 against a ~50 % null).

---

## Cumulative state after batch 11 (N = 117)

- **7 722 / 7 722 cells** complete (117 symbols x 66 EMA pairs), 0 blocked.
- 7 719 cells **rejected** (99.96 %), 3 cells **exploratory signal** in the
  aggregate scan and **rejected** by the OOS + cost-stress check above,
  **0 credible candidates**.
- Pooled (net of costs, full sample, 10 bps taker + 2 bps slippage per side):
  mean net PF **0.4807**, median 0.5023, best net PF **1.0377**
  (SUPER/USDT P8_200, rejected OOS), 6 353 224 trades.
- Cells with net PF > 1: 3 / 7 722 = 0.04 % against a ~50 % no-edge null
  (excess -49.96 %).
- Per-pair pooled leaders (mean net PF over 117 symbols): P8_200 0.6790,
  P20_200 0.6686, P12_200 0.6650, P21_200 0.6617. Worst: P20_21 0.1300,
  P50_55 0.1892, P8_12 0.1920.
- The shape of the result is stable across every batch: mean net PF per batch
  0.4682 (b7), 0.5085 (b8), 0.5210 (b9), 0.5017 (b10), 0.5287 (b11). Lower
  market cap does not improve the registered rule, and the pooled mean net PF
  is drifting *up* only because the smaller names trade less often per bar.

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

The grid directory is shared across batches (the runner resumes from
`progress.json`), so one aggregate report covers the whole processed universe.
OHLCV for every symbol in every batch is in `data/fixtures/`, with provenance in
`data/fixtures/fetch_manifest.json` (KuCoin public `/api/v1/market/candles`,
1h, UTC).
