# EMA Hourly Continuation — CPOOL/USDT P8_50

**Symbol:** CPOOL/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1150 |
| net_profit_factor | 0.6541 |
| net_win_rate | 0.4704 |
| gross_profit_factor | 0.8917 |
| gross_win_rate | 0.4800 |
| sharpe_ratio | -5.1610 |
| sortino_ratio | -2.4517 |
| max_drawdown | 0.9499 |
| cagr | -0.6935 |
| net_avg_win | 33.1544 |
| net_avg_loss | -45.0298 |
| avg_hold_time_bars | 7.9896 |
| exposure | 0.4176 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
