# EMA Hourly Continuation — CVX/USDT P21_100

**Symbol:** CVX/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 506 |
| net_profit_factor | 0.7801 |
| net_win_rate | 0.4921 |
| gross_profit_factor | 0.9555 |
| gross_win_rate | 0.4921 |
| sharpe_ratio | -1.6731 |
| sortino_ratio | -0.5378 |
| max_drawdown | 0.4811 |
| cagr | -0.2202 |
| net_avg_win | 66.2054 |
| net_avg_loss | -82.2210 |
| avg_hold_time_bars | 15.7925 |
| exposure | 0.3632 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
