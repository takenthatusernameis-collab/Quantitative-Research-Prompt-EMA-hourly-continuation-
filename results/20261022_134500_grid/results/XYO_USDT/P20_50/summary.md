# EMA Hourly Continuation — XYO/USDT P20_50

**Symbol:** XYO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1093 |
| net_profit_factor | 0.3933 |
| net_win_rate | 0.3861 |
| gross_profit_factor | 0.7531 |
| gross_win_rate | 0.4035 |
| sharpe_ratio | -10.7199 |
| sortino_ratio | -5.0273 |
| max_drawdown | 0.9983 |
| cagr | -0.9194 |
| net_avg_win | 15.3379 |
| net_avg_loss | -24.5233 |
| avg_hold_time_bars | 5.1116 |
| exposure | 0.2528 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
