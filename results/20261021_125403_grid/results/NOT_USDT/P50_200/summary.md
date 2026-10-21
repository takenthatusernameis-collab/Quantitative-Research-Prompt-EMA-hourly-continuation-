# EMA Hourly Continuation — NOT/USDT P50_200

**Symbol:** NOT/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 282 |
| net_profit_factor | 0.7997 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9500 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -1.1700 |
| sortino_ratio | -0.2852 |
| max_drawdown | 0.2840 |
| cagr | -0.1241 |
| net_avg_win | 79.6441 |
| net_avg_loss | -95.4375 |
| avg_hold_time_bars | 29.2766 |
| exposure | 0.3878 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
