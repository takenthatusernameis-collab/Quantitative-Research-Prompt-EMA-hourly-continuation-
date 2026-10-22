# EMA Hourly Continuation — ETN/USDT P8_26

**Symbol:** ETN/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 499 |
| net_profit_factor | 0.4906 |
| net_win_rate | 0.4068 |
| gross_profit_factor | 0.6369 |
| gross_win_rate | 0.4068 |
| sharpe_ratio | -4.9730 |
| sortino_ratio | -1.7163 |
| max_drawdown | 0.8199 |
| cagr | -0.5499 |
| net_avg_win | 38.5801 |
| net_avg_loss | -53.9298 |
| avg_hold_time_bars | 7.2766 |
| exposure | 0.1972 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
