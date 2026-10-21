# EMA Hourly Continuation — BOME/USDT P8_21

**Symbol:** BOME/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 533 |
| net_profit_factor | 0.8512 |
| net_win_rate | 0.5253 |
| gross_profit_factor | 1.0945 |
| gross_win_rate | 0.5253 |
| sharpe_ratio | -1.1133 |
| sortino_ratio | -0.3708 |
| max_drawdown | 0.4207 |
| cagr | -0.1589 |
| net_avg_win | 72.0197 |
| net_avg_loss | -93.6362 |
| avg_hold_time_bars | 5.6585 |
| exposure | 0.1371 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
