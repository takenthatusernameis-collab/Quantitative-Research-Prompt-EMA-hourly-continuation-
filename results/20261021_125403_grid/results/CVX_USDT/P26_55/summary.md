# EMA Hourly Continuation — CVX/USDT P26_55

**Symbol:** CVX/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 480 |
| net_profit_factor | 0.7149 |
| net_win_rate | 0.4854 |
| gross_profit_factor | 0.9538 |
| gross_win_rate | 0.4854 |
| sharpe_ratio | -2.4256 |
| sortino_ratio | -0.7602 |
| max_drawdown | 0.5883 |
| cagr | -0.2949 |
| net_avg_win | 62.8617 |
| net_avg_loss | -82.9506 |
| avg_hold_time_bars | 6.6833 |
| exposure | 0.1458 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
