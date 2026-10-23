# EMA Hourly Continuation — BAND/USDT P20_34

**Symbol:** BAND/USDT  |  **P_fast:** 20  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1059 |
| net_profit_factor | 0.4292 |
| net_win_rate | 0.4410 |
| gross_profit_factor | 0.9325 |
| gross_win_rate | 0.4655 |
| sharpe_ratio | -9.1001 |
| sortino_ratio | -4.1662 |
| max_drawdown | 0.9952 |
| cagr | -0.8782 |
| net_avg_win | 16.0240 |
| net_avg_loss | -29.4491 |
| avg_hold_time_bars | 3.6195 |
| exposure | 0.1734 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
