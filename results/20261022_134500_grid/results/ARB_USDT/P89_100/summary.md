# EMA Hourly Continuation — ARB/USDT P89_100

**Symbol:** ARB/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 583 |
| net_profit_factor | 0.2819 |
| net_win_rate | 0.4151 |
| gross_profit_factor | 0.8090 |
| gross_win_rate | 0.4563 |
| sharpe_ratio | -8.2385 |
| sortino_ratio | -2.8670 |
| max_drawdown | 0.9753 |
| cagr | -0.7708 |
| net_avg_win | 15.8198 |
| net_avg_loss | -39.8269 |
| avg_hold_time_bars | 2.3019 |
| exposure | 0.0610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
