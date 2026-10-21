# Selection Granularity — EMA Hourly Continuation

**Generated:** 2026-10-21T14:01:52.734331+00:00
**Folds:** 5 | **Minimum history trades per symbol:** 20 | **Market-cap buckets:** 5
**Cost model:** 10.0 bps taker + 2.0 bps slippage per side (stress leg: 2.0x)

## Why this leg exists

The survivor selection audit walks the selection forward over the whole grid and reports a pooled out-of-fold net PF of 0.6409 for the per-symbol selection (266 independent selections per step). A negative result at one granularity does not settle the question: a fine selection can manufacture a bad result out of noise, and a coarse one can hide a good one. This leg re-runs the identical protocol at several granularities and reports the same yardstick for each.

## The ladder

| Arm | Unit | Cells per unit (K) | Units | Out-of-fold trades | Pooled out-of-fold net PF | Pooled out-of-fold net PF (2x) | Out-of-fold windows above PF 1 | Median in-fold PF | Median out-of-fold PF |
|---|---|---|---|---|---|---|---|---|---|
| parent | symbol | 1 | 266 | 95786 | 0.6409 | 0.4521 | 86 (8.1%) | 0.8272 | 0.6217 |
| parent | symbol | 3 | 266 | 295969 | 0.6368 | 0.4480 | 44 (4.1%) | 0.8272 | 0.6258 |
| parent | symbol | 10 | 266 | 1067577 | 0.6266 | 0.4368 | 14 (1.3%) | 0.8272 | 0.6223 |
| parent | bucket | 1 | 5 | 82188 | 0.6609 | 0.4776 | 0 (0.0%) | 0.7059 | 0.6404 |
| parent | bucket | 3 | 5 | 254355 | 0.6590 | 0.4752 | 0 (0.0%) | 0.7059 | 0.6349 |
| parent | bucket | 10 | 5 | 952682 | 0.6489 | 0.4632 | 0 (0.0%) | 0.7059 | 0.6228 |
| parent | global | 1 | 1 | 81254 | 0.6649 | 0.4818 | 0 (0.0%) | 0.7004 | 0.6358 |
| parent | global | 3 | 1 | 246168 | 0.6613 | 0.4788 | 0 (0.0%) | 0.7004 | 0.6272 |
| parent | global | 10 | 1 | 938974 | 0.6493 | 0.4639 | 0 (0.0%) | 0.7004 | 0.6175 |
| child | symbol | 1 | 266 | 60853 | 0.7390 | 0.5731 | 175 (16.5%) | 1.0906 | 0.7347 |
| child | symbol | 3 | 266 | 202172 | 0.7389 | 0.5740 | 123 (11.6%) | 1.0906 | 0.7427 |
| child | symbol | 10 | 266 | 760619 | 0.7428 | 0.5791 | 71 (6.7%) | 1.0906 | 0.7477 |
| child | bucket | 1 | 5 | 67893 | 0.8069 | 0.6704 | 0 (0.0%) | 0.8928 | 0.7932 |
| child | bucket | 3 | 5 | 213671 | 0.8018 | 0.6636 | 0 (0.0%) | 0.8928 | 0.7864 |
| child | bucket | 10 | 5 | 785691 | 0.7893 | 0.6461 | 0 (0.0%) | 0.8928 | 0.7777 |
| child | global | 1 | 1 | 65885 | 0.8030 | 0.6681 | 0 (0.0%) | 0.8841 | 0.7857 |
| child | global | 3 | 1 | 205664 | 0.8070 | 0.6698 | 0 (0.0%) | 0.8841 | 0.7779 |
| child | global | 10 | 1 | 775831 | 0.7937 | 0.6507 | 0 (0.0%) | 0.8841 | 0.7630 |

## The selected cells against the grid's own null

The null needs no randomization: the grid holds 17 556 draws of what a cell scores on a fold it was not selected on. It is comparable with the out-of-fold number only where that number is a per-cell number, i.e. for the `symbol` unit.

| Arm | Unit | K | Selected cells scored | Median percentile | Above the null p95 | Expected under a null pick | One-sided exact binomial p |
|---|---|---|---|---|---|---|---|
| parent | symbol | 1 | 1057 | 0.7768 | 198 | 52.9 | 1.893e-57 |
| parent | symbol | 3 | n/a (pooled number, not comparable with a per-cell null) | n/a | n/a | n/a | n/a |
| parent | symbol | 10 | n/a (pooled number, not comparable with a per-cell null) | n/a | n/a | n/a | n/a |
| parent | bucket | 1 | n/a (pooled number, not comparable with a per-cell null) | n/a | n/a | n/a | n/a |
| parent | bucket | 3 | n/a (pooled number, not comparable with a per-cell null) | n/a | n/a | n/a | n/a |
| parent | bucket | 10 | n/a (pooled number, not comparable with a per-cell null) | n/a | n/a | n/a | n/a |
| parent | global | 1 | n/a (pooled number, not comparable with a per-cell null) | n/a | n/a | n/a | n/a |
| parent | global | 3 | n/a (pooled number, not comparable with a per-cell null) | n/a | n/a | n/a | n/a |
| parent | global | 10 | n/a (pooled number, not comparable with a per-cell null) | n/a | n/a | n/a | n/a |
| child | symbol | 1 | 1059 | 0.5565 | 106 | 53.0 | 2.241e-11 |
| child | symbol | 3 | n/a (pooled number, not comparable with a per-cell null) | n/a | n/a | n/a | n/a |
| child | symbol | 10 | n/a (pooled number, not comparable with a per-cell null) | n/a | n/a | n/a | n/a |
| child | bucket | 1 | n/a (pooled number, not comparable with a per-cell null) | n/a | n/a | n/a | n/a |
| child | bucket | 3 | n/a (pooled number, not comparable with a per-cell null) | n/a | n/a | n/a | n/a |
| child | bucket | 10 | n/a (pooled number, not comparable with a per-cell null) | n/a | n/a | n/a | n/a |
| child | global | 1 | n/a (pooled number, not comparable with a per-cell null) | n/a | n/a | n/a | n/a |
| child | global | 3 | n/a (pooled number, not comparable with a per-cell null) | n/a | n/a | n/a | n/a |
| child | global | 10 | n/a (pooled number, not comparable with a per-cell null) | n/a | n/a | n/a | n/a |

## Arm `parent` — what each granularity selects

Source: `results/20261021_121629_survivor_selection_audit/cells.jsonl` (17556 cells, 266 symbols)

| Unit | Step | Unit name | Symbols | Cells selected | History net PF | Out-of-fold trades | Out-of-fold net PF |
|---|---|---|---|---|---|---|---|
| bucket | 1 | B00 | 54 | P20_200 | 0.6698 | 3864 | 0.7256 |
| bucket | 1 | B01 | 53 | P21_200 | 0.7178 | 3967 | 0.7186 |
| bucket | 1 | B02 | 53 | P20_200 | 0.7080 | 3938 | 0.7617 |
| bucket | 1 | B03 | 53 | P12_200 | 0.7349 | 3532 | 0.7589 |
| bucket | 1 | B04 | 53 | P12_200 | 0.7277 | 3847 | 0.7599 |
| bucket | 2 | B00 | 54 | P12_200 | 0.7037 | 4214 | 0.5951 |
| bucket | 2 | B01 | 53 | P8_200 | 0.7250 | 4525 | 0.6544 |
| bucket | 2 | B02 | 53 | P8_200 | 0.7438 | 4241 | 0.6183 |
| bucket | 2 | B03 | 53 | P8_200 | 0.7677 | 4328 | 0.6412 |
| bucket | 2 | B04 | 53 | P12_200 | 0.7414 | 4316 | 0.6138 |
| bucket | 3 | B00 | 54 | P20_200 | 0.6771 | 3962 | 0.6285 |
| bucket | 3 | B01 | 53 | P8_200 | 0.7026 | 3485 | 0.6815 |
| bucket | 3 | B02 | 53 | P26_200 | 0.7098 | 4193 | 0.6310 |
| bucket | 3 | B03 | 53 | P8_200 | 0.7250 | 4195 | 0.6250 |
| bucket | 3 | B04 | 53 | P12_200 | 0.7014 | 4152 | 0.6064 |
| bucket | 4 | B00 | 54 | P8_200 | 0.6697 | 3901 | 0.5771 |
| bucket | 4 | B01 | 53 | P8_200 | 0.6993 | 4179 | 0.6637 |
| bucket | 4 | B02 | 53 | P26_200 | 0.6934 | 4513 | 0.6477 |
| bucket | 4 | B03 | 53 | P8_200 | 0.7038 | 4328 | 0.6397 |
| bucket | 4 | B04 | 53 | P12_200 | 0.6826 | 4508 | 0.6149 |
| bucket | 1 | B00 | 54 | P20_200, P21_200, P12_200 | 0.6698 | 11442 | 0.7400 |
| bucket | 1 | B01 | 53 | P21_200, P20_200, P8_200 | 0.7178 | 11876 | 0.7417 |
| bucket | 1 | B02 | 53 | P20_200, P26_200, P21_200 | 0.7080 | 11894 | 0.7686 |
| bucket | 1 | B03 | 53 | P12_200, P12_144, P20_144 | 0.7349 | 12860 | 0.7248 |
| bucket | 1 | B04 | 53 | P12_200, P12_144, P20_200 | 0.7277 | 12847 | 0.7447 |
| bucket | 2 | B00 | 54 | P12_200, P20_200, P8_200 | 0.7037 | 12722 | 0.6262 |
| bucket | 2 | B01 | 53 | P8_200, P20_200, P21_200 | 0.7250 | 13324 | 0.6396 |
| bucket | 2 | B02 | 53 | P8_200, P26_200, P12_200 | 0.7438 | 12827 | 0.6249 |
| bucket | 2 | B03 | 53 | P8_200, P12_200, P21_200 | 0.7677 | 12951 | 0.6365 |
| bucket | 2 | B04 | 53 | P12_200, P12_144, P8_200 | 0.7414 | 13685 | 0.6162 |
| bucket | 3 | B00 | 54 | P20_200, P8_200, P12_200 | 0.6771 | 11097 | 0.6332 |
| bucket | 3 | B01 | 53 | P8_200, P20_200, P21_200 | 0.7026 | 11477 | 0.6598 |
| bucket | 3 | B02 | 53 | P26_200, P34_200, P8_200 | 0.7098 | 12190 | 0.6188 |
| bucket | 3 | B03 | 53 | P8_200, P12_200, P21_200 | 0.7250 | 13082 | 0.6171 |
| bucket | 3 | B04 | 53 | P12_200, P12_144, P8_144 | 0.7014 | 15332 | 0.5734 |
| bucket | 4 | B00 | 54 | P8_200, P20_200, P12_200 | 0.6697 | 11784 | 0.5884 |
| bucket | 4 | B01 | 53 | P8_200, P20_200, P21_200 | 0.6993 | 12951 | 0.6561 |
| bucket | 4 | B02 | 53 | P26_200, P34_200, P8_200 | 0.6934 | 13103 | 0.6509 |
| bucket | 4 | B03 | 53 | P8_200, P12_200, P21_200 | 0.7038 | 13318 | 0.6214 |
| bucket | 4 | B04 | 53 | P12_200, P8_200, P20_200 | 0.6826 | 13593 | 0.6186 |
| bucket | 1 | B00 | 54 | P20_200, P21_200, P12_200, P8_200, P26_200, P8_144, P12_144, P20_144, P21_144, P12_100 | 0.6698 | 45547 | 0.7043 |
| bucket | 1 | B01 | 53 | P21_200, P20_200, P8_200, P12_144, P12_200, P21_144, P20_144, P8_144, P26_200, P12_100 | 0.7178 | 46992 | 0.7110 |
| bucket | 1 | B02 | 53 | P20_200, P26_200, P21_200, P8_200, P21_144, P20_144, P12_200, P8_144, P26_144, P12_89 | 0.7080 | 47267 | 0.7445 |
| bucket | 1 | B03 | 53 | P12_200, P12_144, P20_144, P8_200, P21_144, P21_200, P20_200, P8_144, P26_144, P8_100 | 0.7349 | 44058 | 0.7383 |
| bucket | 1 | B04 | 53 | P12_200, P12_144, P20_200, P21_200, P8_100, P20_144, P8_144, P21_144, P8_200, P12_100 | 0.7277 | 49559 | 0.7304 |
| bucket | 2 | B00 | 54 | P12_200, P20_200, P8_200, P21_200, P26_200, P12_144, P8_144, P20_144, P34_200, P21_144 | 0.7037 | 47627 | 0.6187 |
| bucket | 2 | B01 | 53 | P8_200, P20_200, P21_200, P12_200, P12_144, P26_200, P8_144, P20_144, P21_144, P34_200 | 0.7250 | 47566 | 0.6472 |
| bucket | 2 | B02 | 53 | P8_200, P26_200, P12_200, P20_200, P21_200, P8_144, P34_200, P12_144, P21_144, P20_144 | 0.7438 | 46998 | 0.6217 |
| bucket | 2 | B03 | 53 | P8_200, P12_200, P21_200, P20_200, P8_144, P12_144, P20_144, P34_200, P21_144, P26_200 | 0.7677 | 46592 | 0.6280 |
| bucket | 2 | B04 | 53 | P12_200, P12_144, P8_200, P20_200, P21_200, P8_144, P8_100, P26_200, P34_200, P20_144 | 0.7414 | 47408 | 0.6097 |
| bucket | 3 | B00 | 54 | P20_200, P8_200, P12_200, P21_200, P26_200, P8_144, P12_144, P34_200, P20_144, P21_144 | 0.6771 | 44033 | 0.6126 |
| bucket | 3 | B01 | 53 | P8_200, P20_200, P21_200, P12_144, P12_200, P8_144, P20_144, P21_144, P34_200, P26_200 | 0.7026 | 44775 | 0.6355 |
| bucket | 3 | B02 | 53 | P26_200, P34_200, P8_200, P8_144, P12_200, P20_200, P21_200, P12_144, P21_144, P26_144 | 0.7098 | 46168 | 0.6052 |
| bucket | 3 | B03 | 53 | P8_200, P12_200, P21_200, P20_200, P8_144, P34_200, P12_144, P20_144, P26_200, P8_100 | 0.7250 | 50553 | 0.6024 |
| bucket | 3 | B04 | 53 | P12_200, P12_144, P8_144, P8_200, P8_100, P20_200, P21_200, P34_200, P26_200, P8_89 | 0.7014 | 52028 | 0.5912 |
| bucket | 4 | B00 | 54 | P8_200, P20_200, P12_200, P21_200, P26_200, P8_144, P34_200, P12_144, P20_144, P21_144 | 0.6697 | 45821 | 0.5782 |
| bucket | 4 | B01 | 53 | P8_200, P20_200, P21_200, P12_200, P12_144, P26_200, P8_144, P34_200, P20_144, P21_144 | 0.6993 | 49075 | 0.6239 |
| bucket | 4 | B02 | 53 | P26_200, P34_200, P8_200, P12_200, P21_200, P20_200, P8_144, P12_144, P26_144, P21_144 | 0.6934 | 48299 | 0.6434 |
| bucket | 4 | B03 | 53 | P8_200, P12_200, P21_200, P20_200, P34_200, P8_144, P26_200, P12_144, P50_200, P20_144 | 0.7038 | 48113 | 0.6030 |
| bucket | 4 | B04 | 53 | P12_200, P8_200, P20_200, P34_200, P12_144, P8_144, P26_200, P21_200, P8_100, P8_89 | 0.6826 | 54203 | 0.5988 |
| global | 1 | GLOBAL | 266 | P20_200 | 0.7015 | 19423 | 0.7448 |
| global | 2 | GLOBAL | 266 | P8_200 | 0.7292 | 21431 | 0.6338 |
| global | 3 | GLOBAL | 266 | P8_200 | 0.6994 | 19160 | 0.6250 |
| global | 4 | GLOBAL | 266 | P8_200 | 0.6856 | 21240 | 0.6378 |
| global | 1 | GLOBAL | 266 | P20_200, P21_200, P12_200 | 0.7015 | 57601 | 0.7519 |
| global | 2 | GLOBAL | 266 | P8_200, P12_200, P20_200 | 0.7292 | 64640 | 0.6241 |
| global | 3 | GLOBAL | 266 | P8_200, P12_200, P20_200 | 0.6994 | 59668 | 0.6249 |
| global | 4 | GLOBAL | 266 | P8_200, P12_200, P20_200 | 0.6856 | 64259 | 0.6294 |
| global | 1 | GLOBAL | 266 | P20_200, P21_200, P12_200, P8_200, P12_144, P20_144, P21_144, P8_144, P26_200, P12_100 | 0.7015 | 228667 | 0.7278 |
| global | 2 | GLOBAL | 266 | P8_200, P12_200, P20_200, P21_200, P12_144, P8_144, P26_200, P34_200, P20_144, P21_144 | 0.7292 | 235205 | 0.6247 |
| global | 3 | GLOBAL | 266 | P8_200, P12_200, P20_200, P21_200, P8_144, P12_144, P26_200, P34_200, P20_144, P21_144 | 0.6994 | 232823 | 0.6092 |
| global | 4 | GLOBAL | 266 | P8_200, P12_200, P20_200, P21_200, P26_200, P34_200, P8_144, P12_144, P20_144, P21_144 | 0.6856 | 242279 | 0.6104 |

## Arm `child` — what each granularity selects

Source: `results/20261021_135500_mutation_comparison/child_fold_stats.jsonl` (17556 cells, 266 symbols)

| Unit | Step | Unit name | Symbols | Cells selected | History net PF | Out-of-fold trades | Out-of-fold net PF |
|---|---|---|---|---|---|---|---|
| bucket | 1 | B00 | 54 | P8_200 | 0.9228 | 2815 | 0.9683 |
| bucket | 1 | B01 | 53 | P20_200 | 0.8954 | 3025 | 0.8933 |
| bucket | 1 | B02 | 53 | P12_89 | 0.8886 | 5071 | 0.8464 |
| bucket | 1 | B03 | 53 | P12_144 | 0.9351 | 3440 | 0.8949 |
| bucket | 1 | B04 | 53 | P12_144 | 0.9005 | 3792 | 0.9002 |
| bucket | 2 | B00 | 54 | P12_200 | 0.9512 | 3190 | 0.7788 |
| bucket | 2 | B01 | 53 | P8_200 | 0.9100 | 3456 | 0.8077 |
| bucket | 2 | B02 | 53 | P8_200 | 0.9277 | 3368 | 0.7386 |
| bucket | 2 | B03 | 53 | P8_200 | 0.9482 | 3380 | 0.7581 |
| bucket | 2 | B04 | 53 | P8_144 | 0.9125 | 4004 | 0.7429 |
| bucket | 3 | B00 | 54 | P8_200 | 0.9082 | 2756 | 0.8280 |
| bucket | 3 | B01 | 53 | P8_200 | 0.8740 | 2507 | 0.8256 |
| bucket | 3 | B02 | 53 | P8_200 | 0.8612 | 2803 | 0.7487 |
| bucket | 3 | B03 | 53 | P8_200 | 0.8769 | 3244 | 0.7364 |
| bucket | 3 | B04 | 53 | P8_144 | 0.8556 | 4055 | 0.7231 |
| bucket | 4 | B00 | 54 | P8_200 | 0.8901 | 2862 | 0.7787 |
| bucket | 4 | B01 | 53 | P8_200 | 0.8647 | 3087 | 0.8210 |
| bucket | 4 | B02 | 53 | P8_200 | 0.8378 | 3343 | 0.8154 |
| bucket | 4 | B03 | 53 | P8_200 | 0.8420 | 3395 | 0.7781 |
| bucket | 4 | B04 | 53 | P8_144 | 0.8245 | 4300 | 0.7695 |
| bucket | 1 | B00 | 54 | P8_200, P12_200, P20_200 | 0.9228 | 8613 | 0.9526 |
| bucket | 1 | B01 | 53 | P20_200, P21_200, P21_144 | 0.8954 | 9790 | 0.8686 |
| bucket | 1 | B02 | 53 | P12_89, P12_100, P8_200 | 0.8886 | 12771 | 0.8898 |
| bucket | 1 | B03 | 53 | P12_144, P20_144, P8_89 | 0.9351 | 12090 | 0.8782 |
| bucket | 1 | B04 | 53 | P12_144, P8_144, P12_89 | 0.9005 | 12887 | 0.8808 |
| bucket | 2 | B00 | 54 | P12_200, P8_200, P12_144 | 0.9512 | 10419 | 0.7986 |
| bucket | 2 | B01 | 53 | P8_200, P20_200, P12_200 | 0.9100 | 10270 | 0.7845 |
| bucket | 2 | B02 | 53 | P8_200, P12_200, P8_144 | 0.9277 | 10855 | 0.7370 |
| bucket | 2 | B03 | 53 | P8_200, P12_144, P8_144 | 0.9482 | 11271 | 0.7579 |
| bucket | 2 | B04 | 53 | P8_144, P8_200, P12_200 | 0.9125 | 10685 | 0.7335 |
| bucket | 3 | B00 | 54 | P8_200, P12_200, P8_144 | 0.9082 | 9010 | 0.8146 |
| bucket | 3 | B01 | 53 | P8_200, P8_144, P12_144 | 0.8740 | 9585 | 0.7883 |
| bucket | 3 | B02 | 53 | P8_200, P8_144, P12_200 | 0.8612 | 9627 | 0.7523 |
| bucket | 3 | B03 | 53 | P8_200, P8_144, P12_144 | 0.8769 | 11554 | 0.7193 |
| bucket | 3 | B04 | 53 | P8_144, P8_200, P12_144 | 0.8556 | 11565 | 0.7214 |
| bucket | 4 | B00 | 54 | P8_200, P12_200, P8_144 | 0.8901 | 9506 | 0.7804 |
| bucket | 4 | B01 | 53 | P8_200, P12_200, P20_200 | 0.8647 | 9414 | 0.8088 |
| bucket | 4 | B02 | 53 | P8_200, P12_200, P8_144 | 0.8378 | 10824 | 0.8116 |
| bucket | 4 | B03 | 53 | P8_200, P12_144, P8_144 | 0.8420 | 11873 | 0.7624 |
| bucket | 4 | B04 | 53 | P8_144, P8_200, P12_200 | 0.8245 | 11062 | 0.7795 |
| bucket | 1 | B00 | 54 | P8_200, P12_200, P20_200, P21_200, P20_144, P21_144, P12_144, P26_200, P26_144, P12_100 | 0.9228 | 33762 | 0.8917 |
| bucket | 1 | B01 | 53 | P20_200, P21_200, P21_144, P8_200, P20_144, P8_100, P12_144, P8_144, P12_100, P8_89 | 0.8954 | 38744 | 0.8716 |
| bucket | 1 | B02 | 53 | P12_89, P12_100, P8_200, P8_89, P20_144, P21_144, P20_100, P20_200, P8_144, P20_89 | 0.8886 | 42203 | 0.8802 |
| bucket | 1 | B03 | 53 | P12_144, P20_144, P8_89, P21_144, P8_100, P12_200, P12_89, P12_100, P8_144, P8_200 | 0.9351 | 39082 | 0.8865 |
| bucket | 1 | B04 | 53 | P12_144, P8_144, P12_89, P20_144, P20_89, P12_100, P8_100, P21_89, P8_89, P20_100 | 0.9005 | 47486 | 0.8445 |
| bucket | 2 | B00 | 54 | P12_200, P8_200, P12_144, P20_200, P8_144, P21_200, P26_200, P20_144, P21_144, P26_144 | 0.9512 | 36595 | 0.7994 |
| bucket | 2 | B01 | 53 | P8_200, P20_200, P12_200, P21_200, P8_100, P12_144, P8_144, P8_89, P20_144, P21_144 | 0.9100 | 39818 | 0.7919 |
| bucket | 2 | B02 | 53 | P8_200, P12_200, P8_144, P20_200, P26_200, P21_200, P12_144, P12_100, P21_144, P20_144 | 0.9277 | 38732 | 0.7209 |
| bucket | 2 | B03 | 53 | P8_200, P12_144, P8_144, P8_89, P12_200, P8_100, P20_144, P20_200, P21_200, P12_89 | 0.9482 | 40518 | 0.7542 |
| bucket | 2 | B04 | 53 | P8_144, P8_200, P12_200, P12_144, P8_100, P21_200, P8_89, P20_200, P12_100, P20_144 | 0.9125 | 40584 | 0.7222 |
| bucket | 3 | B00 | 54 | P8_200, P12_200, P8_144, P20_200, P21_200, P12_144, P26_200, P8_100, P20_144, P21_144 | 0.9082 | 34142 | 0.7972 |
| bucket | 3 | B01 | 53 | P8_200, P8_144, P12_144, P8_100, P12_200, P20_200, P8_89, P21_144, P20_144, P21_200 | 0.8740 | 35712 | 0.7784 |
| bucket | 3 | B02 | 53 | P8_200, P8_144, P12_200, P26_200, P8_100, P8_89, P34_200, P12_144, P20_200, P12_100 | 0.8612 | 38925 | 0.7393 |
| bucket | 3 | B03 | 53 | P8_200, P8_144, P12_144, P8_100, P8_89, P12_200, P20_144, P20_200, P21_200, P21_144 | 0.8769 | 41589 | 0.7214 |
| bucket | 3 | B04 | 53 | P8_144, P8_200, P12_144, P12_200, P8_100, P8_89, P12_100, P34_200, P20_144, P20_200 | 0.8556 | 42095 | 0.7352 |
| bucket | 4 | B00 | 54 | P8_200, P12_200, P8_144, P20_200, P21_200, P26_200, P12_144, P8_100, P20_144, P21_144 | 0.8901 | 35265 | 0.7681 |
| bucket | 4 | B01 | 53 | P8_200, P12_200, P20_200, P8_144, P12_144, P21_200, P8_100, P21_144, P26_200, P8_89 | 0.8647 | 38666 | 0.7770 |
| bucket | 4 | B02 | 53 | P8_200, P12_200, P8_144, P26_200, P34_200, P20_200, P21_200, P8_89, P8_100, P12_144 | 0.8378 | 39988 | 0.7864 |
| bucket | 4 | B03 | 53 | P8_200, P12_144, P8_144, P12_200, P20_200, P8_100, P21_200, P8_89, P20_144, P26_200 | 0.8420 | 41403 | 0.7417 |
| bucket | 4 | B04 | 53 | P8_144, P8_200, P12_200, P8_89, P8_100, P12_144, P34_200, P20_200, P21_200, P26_200 | 0.8245 | 40382 | 0.7431 |
| global | 1 | GLOBAL | 266 | P20_144 | 0.8952 | 18758 | 0.8552 |
| global | 2 | GLOBAL | 266 | P8_200 | 0.9265 | 16599 | 0.7747 |
| global | 3 | GLOBAL | 266 | P8_200 | 0.8731 | 14451 | 0.7724 |
| global | 4 | GLOBAL | 266 | P8_200 | 0.8510 | 16077 | 0.7967 |
| global | 1 | GLOBAL | 266 | P20_144, P12_144, P8_200 | 0.8952 | 51265 | 0.9055 |
| global | 2 | GLOBAL | 266 | P8_200, P12_200, P8_144 | 0.9265 | 53309 | 0.7680 |
| global | 3 | GLOBAL | 266 | P8_200, P8_144, P12_200 | 0.8731 | 48479 | 0.7615 |
| global | 4 | GLOBAL | 266 | P8_200, P12_200, P8_144 | 0.8510 | 52611 | 0.7877 |
| global | 1 | GLOBAL | 266 | P20_144, P12_144, P8_200, P21_144, P12_100, P12_200, P20_200, P8_100, P8_144, P8_89 | 0.8952 | 191524 | 0.8904 |
| global | 2 | GLOBAL | 266 | P8_200, P12_200, P8_144, P12_144, P20_200, P21_200, P8_100, P20_144, P8_89, P26_200 | 0.9265 | 195713 | 0.7611 |
| global | 3 | GLOBAL | 266 | P8_200, P8_144, P12_200, P12_144, P8_100, P20_200, P8_89, P21_200, P20_144, P21_144 | 0.8731 | 193740 | 0.7506 |
| global | 4 | GLOBAL | 266 | P8_200, P12_200, P8_144, P20_200, P26_200, P21_200, P12_144, P8_100, P34_200, P8_89 | 0.8510 | 194854 | 0.7650 |

## Verdict

- Arm `parent`: the control (per-symbol selection, one cell per symbol) gives a pooled out-of-fold net PF of 0.6409 over 95786 out-of-fold trades.
- Arm `parent`: the best granularity on this ladder is `global` with K = 1: pooled out-of-fold net PF 0.6649 (0.4818 under 2x costs) over 81254 out-of-fold trades.
- Arm `parent`: no granularity clears PF 1 out of sample. The rule has no edge at the per-symbol, per-family or global selection granularity, so the negative result of the finest selection is a property of the rule, not of the selection granularity.
- Arm `parent`: a coarser selection does not rescue the procedure - the per-family and global selections score 0.6649 against the per-symbol control's 0.6409.
- Arm `child`: the control (per-symbol selection, one cell per symbol) gives a pooled out-of-fold net PF of 0.7390 over 60853 out-of-fold trades.
- Arm `child`: the best granularity on this ladder is `global` with K = 3: pooled out-of-fold net PF 0.8070 (0.6698 under 2x costs) over 205664 out-of-fold trades.
- Arm `child`: no granularity clears PF 1 out of sample. The rule has no edge at the per-symbol, per-family or global selection granularity, so the negative result of the finest selection is a property of the rule, not of the selection granularity.
- Arm `child`: a coarser selection does not rescue the procedure - the per-family and global selections score 0.8070 against the per-symbol control's 0.7390.
- The arms are read against each other on the same yardstick: the pooled out-of-fold net PF of the trades the procedure actually takes.
