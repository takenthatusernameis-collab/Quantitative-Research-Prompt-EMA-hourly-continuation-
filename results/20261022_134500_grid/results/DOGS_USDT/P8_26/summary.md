# EMA Hourly Continuation — DOGS/USDT P8_26

**Symbol:** DOGS/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1359 |
| net_profit_factor | 0.4632 |
| net_win_rate | 0.4430 |
| gross_profit_factor | 0.7813 |
| gross_win_rate | 0.4562 |
| sharpe_ratio | -9.7087 |
| sortino_ratio | -5.4440 |
| max_drawdown | 0.9969 |
| cagr | -0.9320 |
| net_avg_win | 14.2888 |
| net_avg_loss | -24.5325 |
| avg_hold_time_bars | 3.7255 |
| exposure | 0.2686 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
