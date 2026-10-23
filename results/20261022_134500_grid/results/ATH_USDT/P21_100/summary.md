# EMA Hourly Continuation — ATH/USDT P21_100

**Symbol:** ATH/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 654 |
| net_profit_factor | 0.7084 |
| net_win_rate | 0.5031 |
| gross_profit_factor | 1.0233 |
| gross_win_rate | 0.5046 |
| sharpe_ratio | -2.9722 |
| sortino_ratio | -1.1123 |
| max_drawdown | 0.7222 |
| cagr | -0.4081 |
| net_avg_win | 52.3578 |
| net_avg_loss | -74.8243 |
| avg_hold_time_bars | 11.9786 |
| exposure | 0.3797 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
