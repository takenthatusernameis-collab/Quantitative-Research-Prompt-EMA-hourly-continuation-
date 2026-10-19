# EMA Hourly Continuation — ADA/USDT P21_50

**Symbol:** ADA/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 947 |
| net_profit_factor | 0.4466 |
| net_win_rate | 0.4604 |
| gross_profit_factor | 0.9306 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -7.4771 |
| sortino_ratio | -3.2485 |
| max_drawdown | 0.9824 |
| cagr | -0.7985 |
| net_avg_win | 18.1805 |
| net_avg_loss | -34.7315 |
| avg_hold_time_bars | 4.7254 |
| exposure | 0.2034 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
