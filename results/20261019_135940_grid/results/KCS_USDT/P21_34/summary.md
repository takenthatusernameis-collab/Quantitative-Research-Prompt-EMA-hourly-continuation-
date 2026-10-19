# EMA Hourly Continuation — KCS/USDT P21_34

**Symbol:** KCS/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1134 |
| net_profit_factor | 0.1009 |
| net_win_rate | 0.2390 |
| gross_profit_factor | 0.6126 |
| gross_win_rate | 0.3633 |
| sharpe_ratio | -19.1982 |
| sortino_ratio | -10.2662 |
| max_drawdown | 1.0000 |
| cagr | -0.9963 |
| net_avg_win | 4.1405 |
| net_avg_loss | -12.8877 |
| avg_hold_time_bars | 2.7928 |
| exposure | 0.1440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
