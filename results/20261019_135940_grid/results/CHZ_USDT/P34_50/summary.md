# EMA Hourly Continuation — CHZ/USDT P34_50

**Symbol:** CHZ/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 917 |
| net_profit_factor | 0.3112 |
| net_win_rate | 0.4100 |
| gross_profit_factor | 0.6787 |
| gross_win_rate | 0.4308 |
| sharpe_ratio | -9.9588 |
| sortino_ratio | -4.3053 |
| max_drawdown | 0.9959 |
| cagr | -0.8881 |
| net_avg_win | 11.9685 |
| net_avg_loss | -26.7270 |
| avg_hold_time_bars | 2.8528 |
| exposure | 0.1189 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
