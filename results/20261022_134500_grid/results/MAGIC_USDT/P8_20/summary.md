# EMA Hourly Continuation — MAGIC/USDT P8_20

**Symbol:** MAGIC/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1509 |
| net_profit_factor | 0.4809 |
| net_win_rate | 0.4407 |
| gross_profit_factor | 0.9575 |
| gross_win_rate | 0.4619 |
| sharpe_ratio | -10.1576 |
| sortino_ratio | -5.5677 |
| max_drawdown | 0.9990 |
| cagr | -0.9356 |
| net_avg_win | 13.9190 |
| net_avg_loss | -22.8032 |
| avg_hold_time_bars | 3.8045 |
| exposure | 0.2610 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
