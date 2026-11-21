# EMA Hourly Continuation — HTR/USDT P21_100

**Symbol:** HTR/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 756 |
| net_profit_factor | 0.5084 |
| net_win_rate | 0.4101 |
| gross_profit_factor | 0.7394 |
| gross_win_rate | 0.4167 |
| sharpe_ratio | -6.5195 |
| sortino_ratio | -2.5090 |
| max_drawdown | 0.9552 |
| cagr | -0.7071 |
| net_avg_win | 31.8325 |
| net_avg_loss | -43.5208 |
| avg_hold_time_bars | 11.4021 |
| exposure | 0.3918 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
