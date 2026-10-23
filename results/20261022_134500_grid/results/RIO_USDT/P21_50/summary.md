# EMA Hourly Continuation — RIO/USDT P21_50

**Symbol:** RIO/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1115 |
| net_profit_factor | 0.4756 |
| net_win_rate | 0.4009 |
| gross_profit_factor | 0.7208 |
| gross_win_rate | 0.4054 |
| sharpe_ratio | -8.4515 |
| sortino_ratio | -3.9873 |
| max_drawdown | 0.9921 |
| cagr | -0.8563 |
| net_avg_win | 20.1302 |
| net_avg_loss | -28.3201 |
| avg_hold_time_bars | 4.2404 |
| exposure | 0.2171 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
