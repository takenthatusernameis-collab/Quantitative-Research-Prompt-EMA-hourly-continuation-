# EMA Hourly Continuation — IMX/USDT P21_200

**Symbol:** IMX/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 288 |
| net_profit_factor | 1.0431 |
| net_win_rate | 0.5486 |
| gross_profit_factor | 1.2162 |
| gross_win_rate | 0.5486 |
| sharpe_ratio | 0.2636 |
| sortino_ratio | 0.0648 |
| max_drawdown | 0.1419 |
| cagr | 0.0226 |
| net_avg_win | 89.0081 |
| net_avg_loss | -103.7081 |
| avg_hold_time_bars | 51.1493 |
| exposure | 0.6666 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
