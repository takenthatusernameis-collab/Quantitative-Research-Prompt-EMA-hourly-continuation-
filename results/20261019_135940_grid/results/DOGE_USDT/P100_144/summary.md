# EMA Hourly Continuation — DOGE/USDT P100_144

**Symbol:** DOGE/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.4223 |
| net_win_rate | 0.4356 |
| gross_profit_factor | 0.8980 |
| gross_win_rate | 0.4772 |
| sharpe_ratio | -6.4714 |
| sortino_ratio | -2.0592 |
| max_drawdown | 0.9287 |
| cagr | -0.6494 |
| net_avg_win | 30.8309 |
| net_avg_loss | -56.3624 |
| avg_hold_time_bars | 3.7683 |
| exposure | 0.0865 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
