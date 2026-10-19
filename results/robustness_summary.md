# Robustness Summary (Child C tuned config)

Config: rr=1.5, min_risk_atr=True, atr_threshold=0.75, stricter_trend=False.

## Threshold sweep (n=5, pooled)
| atr_threshold | trades | net PF | net WR | Sharpe |
|---|---|---|---|---|
| 0.70 | 39 | 0.3680 | 0.3846 | -9.3864 |
| 0.75 | 36 | 0.4257 | 0.3889 | -7.9898 |
| 0.80 | 34 | 0.4171 | 0.3824 | -8.0183 |

0.75 remains best among tested.

## Walk-forward (BTC/USDT, expanding windows)
All 4 test windows produced 0 trades (windows too short / no qualifying signals). No OOS trades to evaluate; indicates need larger OOS windows or pooled cross-symbol OOS.

## OOS split (pooled, last 20%)
0 trades. Same limitation.

## stricter_trend variation
No change in metrics vs base Child C (36 trades, net PF 0.4257).

## Conclusion
Tuned config improves vs unfiltered but remains negative Sharpe; OOS validation inconclusive due to sparse signals. Next: pooled OOS with larger test windows and per-symbol OOS aggregation.
