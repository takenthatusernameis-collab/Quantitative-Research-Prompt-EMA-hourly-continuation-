# EMA Hourly Continuation — CHR/USDT P55_200

**Symbol:** CHR/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 405 |
| net_profit_factor | 0.7639 |
| net_win_rate | 0.5086 |
| gross_profit_factor | 1.0346 |
| gross_win_rate | 0.5086 |
| sharpe_ratio | -1.7475 |
| sortino_ratio | -0.5004 |
| max_drawdown | 0.4921 |
| cagr | -0.2091 |
| net_avg_win | 70.1452 |
| net_avg_loss | -95.0556 |
| avg_hold_time_bars | 21.8617 |
| exposure | 0.4007 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
