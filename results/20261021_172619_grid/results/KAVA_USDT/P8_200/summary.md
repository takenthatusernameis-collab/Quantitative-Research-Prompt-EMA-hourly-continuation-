# EMA Hourly Continuation — KAVA/USDT P8_200

**Symbol:** KAVA/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.7620 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9569 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -1.5341 |
| sortino_ratio | -0.3973 |
| max_drawdown | 0.3983 |
| cagr | -0.1678 |
| net_avg_win | 73.4826 |
| net_avg_loss | -92.4134 |
| avg_hold_time_bars | 53.5289 |
| exposure | 0.8005 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
