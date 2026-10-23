# EMA Hourly Continuation — GMX/USDT P8_100

**Symbol:** GMX/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 720 |
| net_profit_factor | 0.6212 |
| net_win_rate | 0.4625 |
| gross_profit_factor | 0.9025 |
| gross_win_rate | 0.4694 |
| sharpe_ratio | -4.2952 |
| sortino_ratio | -1.6213 |
| max_drawdown | 0.8563 |
| cagr | -0.5365 |
| net_avg_win | 42.1090 |
| net_avg_loss | -58.3257 |
| avg_hold_time_bars | 19.4514 |
| exposure | 0.6366 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
