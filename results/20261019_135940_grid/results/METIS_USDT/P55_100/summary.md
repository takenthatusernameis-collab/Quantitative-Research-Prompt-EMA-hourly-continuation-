# EMA Hourly Continuation — METIS/USDT P55_100

**Symbol:** METIS/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 651 |
| net_profit_factor | 0.4194 |
| net_win_rate | 0.4117 |
| gross_profit_factor | 0.7444 |
| gross_win_rate | 0.4270 |
| sharpe_ratio | -6.7053 |
| sortino_ratio | -2.4231 |
| max_drawdown | 0.9494 |
| cagr | -0.6931 |
| net_avg_win | 25.5676 |
| net_avg_loss | -42.6559 |
| avg_hold_time_bars | 4.9508 |
| exposure | 0.1465 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
