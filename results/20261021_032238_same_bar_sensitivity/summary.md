# Same-Bar SL/TP Path Sensitivity — closest survivors

**Generated:** 2026-10-21T03:23:28.594538+00:00
**Cells:** 6 (the closest survivors of `results/20261021_005234_oos_grid_scan`)
**Out-of-sample window:** trailing 35% of each symbol's bars

The baseline closes a same-bar stop/target conflict at the stop (adverse first). The favourable rule closes it at the target. A verdict that only holds under the favourable rule is an artifact of the intrabar path assumption.

| Symbol | Cell | OOS PF (conservative) | OOS PF (favourable) | Stress OOS PF (conservative) | Stress OOS PF (favourable) | Verdict (conservative) | Verdict (favourable) |
|---|---|---|---|---|---|---|---|
| BRETT/USDT | P8_200 | 1.3323 | 1.4528 | 1.0489 | 1.1313 | exploratory signal | exploratory signal |
| DEXE/USDT | P50_200 | 1.3819 | 1.4593 | 1.1322 | 1.1932 | exploratory signal | exploratory signal |
| DEXE/USDT | P55_200 | 1.3647 | 1.5368 | 1.0975 | 1.2308 | exploratory signal | exploratory signal |
| GRT/USDT | P20_200 | 1.3413 | 1.3413 | 1.0976 | 1.0976 | exploratory signal | exploratory signal |
| MERL/USDT | P8_200 | 1.2518 | 1.2518 | 1.0101 | 1.0101 | exploratory signal | exploratory signal |
| ZEN/USDT | P12_200 | 1.2739 | 1.2739 | 1.0388 | 1.0388 | exploratory signal | exploratory signal |

## Verdict

- 6 closest survivors were re-run under the conservative and the favourable same-bar path assumption.
- The §3.4 verdict changes for 0 of them; 0 are credible under the conservative rule and 0 under the favourable one.
