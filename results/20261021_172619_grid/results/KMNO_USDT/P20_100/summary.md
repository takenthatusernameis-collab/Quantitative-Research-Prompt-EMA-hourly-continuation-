# EMA Hourly Continuation — KMNO/USDT P20_100

**Symbol:** KMNO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.8211 |
| net_win_rate | 0.5036 |
| gross_profit_factor | 1.0097 |
| gross_win_rate | 0.5036 |
| sharpe_ratio | -1.2700 |
| sortino_ratio | -0.3712 |
| max_drawdown | 0.3816 |
| cagr | -0.1593 |
| net_avg_win | 77.3510 |
| net_avg_loss | -95.5847 |
| avg_hold_time_bars | 21.4793 |
| exposure | 0.4076 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
