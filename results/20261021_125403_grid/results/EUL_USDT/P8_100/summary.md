# EMA Hourly Continuation — EUL/USDT P8_100

**Symbol:** EUL/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 485 |
| net_profit_factor | 0.8470 |
| net_win_rate | 0.5052 |
| gross_profit_factor | 1.0049 |
| gross_win_rate | 0.5052 |
| sharpe_ratio | -1.0205 |
| sortino_ratio | -0.3221 |
| max_drawdown | 0.3337 |
| cagr | -0.1404 |
| net_avg_win | 71.4497 |
| net_avg_loss | -86.1110 |
| avg_hold_time_bars | 28.4412 |
| exposure | 0.6270 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
