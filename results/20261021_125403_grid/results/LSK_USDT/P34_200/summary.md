# EMA Hourly Continuation — LSK/USDT P34_200

**Symbol:** LSK/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 307 |
| net_profit_factor | 0.7644 |
| net_win_rate | 0.4951 |
| gross_profit_factor | 0.9710 |
| gross_win_rate | 0.4951 |
| sharpe_ratio | -1.4139 |
| sortino_ratio | -0.3536 |
| max_drawdown | 0.4301 |
| cagr | -0.1512 |
| net_avg_win | 72.0366 |
| net_avg_loss | -92.4157 |
| avg_hold_time_bars | 36.0879 |
| exposure | 0.5036 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
