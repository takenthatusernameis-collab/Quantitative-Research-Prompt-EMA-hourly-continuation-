# EMA Hourly Continuation — ARPA/USDT P26_100

**Symbol:** ARPA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 531 |
| net_profit_factor | 0.6513 |
| net_win_rate | 0.4652 |
| gross_profit_factor | 0.8668 |
| gross_win_rate | 0.4652 |
| sharpe_ratio | -3.1744 |
| sortino_ratio | -1.0399 |
| max_drawdown | 0.7253 |
| cagr | -0.3797 |
| net_avg_win | 52.9441 |
| net_avg_loss | -70.7019 |
| avg_hold_time_bars | 14.2411 |
| exposure | 0.3422 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
