# EMA Hourly Continuation — CGPT/USDT P20_100

**Symbol:** CGPT/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 623 |
| net_profit_factor | 0.6298 |
| net_win_rate | 0.4703 |
| gross_profit_factor | 0.9189 |
| gross_win_rate | 0.4751 |
| sharpe_ratio | -3.8898 |
| sortino_ratio | -1.3534 |
| max_drawdown | 0.8183 |
| cagr | -0.4859 |
| net_avg_win | 47.1458 |
| net_avg_loss | -66.4629 |
| avg_hold_time_bars | 14.9920 |
| exposure | 0.4245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
