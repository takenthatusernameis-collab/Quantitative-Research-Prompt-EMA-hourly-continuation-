# EMA Hourly Continuation — QI/USDT P34_100

**Symbol:** QI/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.9242 |
| net_win_rate | 0.5545 |
| gross_profit_factor | 1.2312 |
| gross_win_rate | 0.5545 |
| sharpe_ratio | -0.4299 |
| sortino_ratio | -0.1252 |
| max_drawdown | 0.1895 |
| cagr | -0.0605 |
| net_avg_win | 79.2597 |
| net_avg_loss | -106.7223 |
| avg_hold_time_bars | 14.5124 |
| exposure | 0.2653 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
