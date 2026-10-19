# EMA Hourly Continuation — SEI/USDT P21_100

**Symbol:** SEI/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 610 |
| net_profit_factor | 0.7262 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 1.0446 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -3.0235 |
| sortino_ratio | -1.0526 |
| max_drawdown | 0.7587 |
| cagr | -0.3953 |
| net_avg_win | 63.2025 |
| net_avg_loss | -84.7784 |
| avg_hold_time_bars | 15.6672 |
| exposure | 0.4344 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
