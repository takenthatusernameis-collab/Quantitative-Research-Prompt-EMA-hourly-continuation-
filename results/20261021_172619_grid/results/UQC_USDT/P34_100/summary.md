# EMA Hourly Continuation — UQC/USDT P34_100

**Symbol:** UQC/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 249 |
| net_profit_factor | 0.3074 |
| net_win_rate | 0.2771 |
| gross_profit_factor | 0.4598 |
| gross_win_rate | 0.2932 |
| sharpe_ratio | -6.1208 |
| sortino_ratio | -1.3525 |
| max_drawdown | 0.8231 |
| cagr | -0.4968 |
| net_avg_win | 52.9465 |
| net_avg_loss | -66.0249 |
| avg_hold_time_bars | 41.2892 |
| exposure | 0.4653 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
