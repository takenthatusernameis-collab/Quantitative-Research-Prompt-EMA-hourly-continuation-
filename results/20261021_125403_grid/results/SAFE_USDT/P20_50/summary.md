# EMA Hourly Continuation — SAFE/USDT P20_50

**Symbol:** SAFE/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 531 |
| net_profit_factor | 0.7162 |
| net_win_rate | 0.4859 |
| gross_profit_factor | 0.9423 |
| gross_win_rate | 0.4859 |
| sharpe_ratio | -2.4743 |
| sortino_ratio | -0.8181 |
| max_drawdown | 0.6266 |
| cagr | -0.3127 |
| net_avg_win | 59.4013 |
| net_avg_loss | -78.3842 |
| avg_hold_time_bars | 8.1959 |
| exposure | 0.1993 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
