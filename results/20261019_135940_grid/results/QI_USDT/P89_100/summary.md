# EMA Hourly Continuation — QI/USDT P89_100

**Symbol:** QI/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 530 |
| net_profit_factor | 0.2272 |
| net_win_rate | 0.3736 |
| gross_profit_factor | 0.7064 |
| gross_win_rate | 0.4340 |
| sharpe_ratio | -8.7417 |
| sortino_ratio | -2.9283 |
| max_drawdown | 0.9778 |
| cagr | -0.7789 |
| net_avg_win | 14.5170 |
| net_avg_loss | -38.1087 |
| avg_hold_time_bars | 3.1585 |
| exposure | 0.0758 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
