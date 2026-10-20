# EMA Hourly Continuation — EUL/USDT P8_55

**Symbol:** EUL/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 989 |
| net_profit_factor | 0.4683 |
| net_win_rate | 0.4479 |
| gross_profit_factor | 0.7320 |
| gross_win_rate | 0.4520 |
| sharpe_ratio | -6.0765 |
| sortino_ratio | -2.6785 |
| max_drawdown | 0.9640 |
| cagr | -0.7283 |
| net_avg_win | 19.1283 |
| net_avg_loss | -33.1406 |
| avg_hold_time_bars | 11.0243 |
| exposure | 0.4956 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
