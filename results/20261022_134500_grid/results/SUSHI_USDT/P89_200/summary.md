# EMA Hourly Continuation — SUSHI/USDT P89_200

**Symbol:** SUSHI/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 433 |
| net_profit_factor | 0.5306 |
| net_win_rate | 0.4665 |
| gross_profit_factor | 0.8977 |
| gross_win_rate | 0.4781 |
| sharpe_ratio | -3.8088 |
| sortino_ratio | -1.1177 |
| max_drawdown | 0.7439 |
| cagr | -0.4116 |
| net_avg_win | 41.2845 |
| net_avg_loss | -68.0344 |
| avg_hold_time_bars | 9.5774 |
| exposure | 0.1877 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
