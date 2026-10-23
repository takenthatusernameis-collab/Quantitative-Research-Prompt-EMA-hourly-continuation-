# EMA Hourly Continuation — IO/USDT P89_200

**Symbol:** IO/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.6070 |
| net_win_rate | 0.4662 |
| gross_profit_factor | 0.8587 |
| gross_win_rate | 0.4662 |
| sharpe_ratio | -3.2095 |
| sortino_ratio | -0.9263 |
| max_drawdown | 0.6643 |
| cagr | -0.3605 |
| net_avg_win | 54.1003 |
| net_avg_loss | -77.8286 |
| avg_hold_time_bars | 11.1905 |
| exposure | 0.2162 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
