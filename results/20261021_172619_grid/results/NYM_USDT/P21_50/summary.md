# EMA Hourly Continuation — NYM/USDT P21_50

**Symbol:** NYM/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.4843 |
| net_win_rate | 0.4425 |
| gross_profit_factor | 0.8200 |
| gross_win_rate | 0.4425 |
| sharpe_ratio | -4.3574 |
| sortino_ratio | -1.2431 |
| max_drawdown | 0.7651 |
| cagr | -0.4380 |
| net_avg_win | 40.5818 |
| net_avg_loss | -66.5070 |
| avg_hold_time_bars | 12.1100 |
| exposure | 0.2202 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
