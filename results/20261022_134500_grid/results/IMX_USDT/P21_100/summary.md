# EMA Hourly Continuation — IMX/USDT P21_100

**Symbol:** IMX/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 610 |
| net_profit_factor | 0.6468 |
| net_win_rate | 0.4787 |
| gross_profit_factor | 0.9163 |
| gross_win_rate | 0.4869 |
| sharpe_ratio | -3.1488 |
| sortino_ratio | -1.0959 |
| max_drawdown | 0.7342 |
| cagr | -0.4043 |
| net_avg_win | 45.7380 |
| net_avg_loss | -64.9321 |
| avg_hold_time_bars | 15.5656 |
| exposure | 0.4297 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
