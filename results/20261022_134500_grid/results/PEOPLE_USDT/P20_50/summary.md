# EMA Hourly Continuation — PEOPLE/USDT P20_50

**Symbol:** PEOPLE/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 962 |
| net_profit_factor | 0.5219 |
| net_win_rate | 0.4439 |
| gross_profit_factor | 0.8191 |
| gross_win_rate | 0.4553 |
| sharpe_ratio | -6.5289 |
| sortino_ratio | -2.8392 |
| max_drawdown | 0.9687 |
| cagr | -0.7468 |
| net_avg_win | 24.7658 |
| net_avg_loss | -37.8731 |
| avg_hold_time_bars | 4.9335 |
| exposure | 0.2148 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
