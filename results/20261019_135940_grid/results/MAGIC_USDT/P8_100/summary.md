# EMA Hourly Continuation — MAGIC/USDT P8_100

**Symbol:** MAGIC/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 588 |
| net_profit_factor | 0.7391 |
| net_win_rate | 0.4932 |
| gross_profit_factor | 1.0449 |
| gross_win_rate | 0.5051 |
| sharpe_ratio | -2.5816 |
| sortino_ratio | -0.8868 |
| max_drawdown | 0.6862 |
| cagr | -0.3411 |
| net_avg_win | 63.4342 |
| net_avg_loss | -83.5179 |
| avg_hold_time_bars | 25.8622 |
| exposure | 0.6912 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
