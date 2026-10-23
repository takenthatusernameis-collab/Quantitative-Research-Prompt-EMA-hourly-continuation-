# EMA Hourly Continuation — PHA/USDT P8_50

**Symbol:** PHA/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1112 |
| net_profit_factor | 0.5844 |
| net_win_rate | 0.4676 |
| gross_profit_factor | 0.9340 |
| gross_win_rate | 0.4748 |
| sharpe_ratio | -5.6268 |
| sortino_ratio | -2.6254 |
| max_drawdown | 0.9602 |
| cagr | -0.7209 |
| net_avg_win | 25.9444 |
| net_avg_loss | -38.9956 |
| avg_hold_time_bars | 9.0180 |
| exposure | 0.4558 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
