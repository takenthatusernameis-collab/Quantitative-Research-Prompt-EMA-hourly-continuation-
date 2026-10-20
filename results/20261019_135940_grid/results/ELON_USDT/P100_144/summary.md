# EMA Hourly Continuation — ELON/USDT P100_144

**Symbol:** ELON/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 489 |
| net_profit_factor | 0.4352 |
| net_win_rate | 0.4499 |
| gross_profit_factor | 0.8001 |
| gross_win_rate | 0.4581 |
| sharpe_ratio | -5.2410 |
| sortino_ratio | -1.6641 |
| max_drawdown | 0.8638 |
| cagr | -0.5424 |
| net_avg_win | 30.1073 |
| net_avg_loss | -56.5790 |
| avg_hold_time_bars | 3.8650 |
| exposure | 0.0859 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
