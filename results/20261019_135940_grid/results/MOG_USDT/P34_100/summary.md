# EMA Hourly Continuation — MOG/USDT P34_100

**Symbol:** MOG/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 594 |
| net_profit_factor | 0.6622 |
| net_win_rate | 0.4714 |
| gross_profit_factor | 0.8968 |
| gross_win_rate | 0.4731 |
| sharpe_ratio | -3.6146 |
| sortino_ratio | -1.2936 |
| max_drawdown | 0.7594 |
| cagr | -0.4604 |
| net_avg_win | 53.0261 |
| net_avg_loss | -71.4083 |
| avg_hold_time_bars | 8.4125 |
| exposure | 0.2484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
