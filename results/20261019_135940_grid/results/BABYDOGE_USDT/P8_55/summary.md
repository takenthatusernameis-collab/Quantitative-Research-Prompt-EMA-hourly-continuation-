# EMA Hourly Continuation — BABYDOGE/USDT P8_55

**Symbol:** BABYDOGE/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 87 |
| net_profit_factor | 0.9012 |
| net_win_rate | 0.4943 |
| gross_profit_factor | 0.9697 |
| gross_win_rate | 0.4943 |
| sharpe_ratio | -0.2819 |
| sortino_ratio | -0.0375 |
| max_drawdown | 0.0873 |
| cagr | -0.0181 |
| net_avg_win | 95.7794 |
| net_avg_loss | -103.8620 |
| avg_hold_time_bars | 32.4943 |
| exposure | 0.1279 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
