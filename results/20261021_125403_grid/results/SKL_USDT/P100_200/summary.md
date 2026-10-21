# EMA Hourly Continuation — SKL/USDT P100_200

**Symbol:** SKL/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 258 |
| net_profit_factor | 1.1007 |
| net_win_rate | 0.5814 |
| gross_profit_factor | 1.3767 |
| gross_win_rate | 0.5814 |
| sharpe_ratio | 0.5233 |
| sortino_ratio | 0.1233 |
| max_drawdown | 0.1412 |
| cagr | 0.0489 |
| net_avg_win | 92.7566 |
| net_avg_loss | -117.0378 |
| avg_hold_time_bars | 13.4845 |
| exposure | 0.1581 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
