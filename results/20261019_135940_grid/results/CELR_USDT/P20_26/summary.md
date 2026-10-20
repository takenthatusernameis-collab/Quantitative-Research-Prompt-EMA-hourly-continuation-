# EMA Hourly Continuation — CELR/USDT P20_26

**Symbol:** CELR/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1188 |
| net_profit_factor | 0.2546 |
| net_win_rate | 0.3822 |
| gross_profit_factor | 0.8565 |
| gross_win_rate | 0.4352 |
| sharpe_ratio | -12.6316 |
| sortino_ratio | -6.2627 |
| max_drawdown | 0.9997 |
| cagr | -0.9579 |
| net_avg_win | 7.5209 |
| net_avg_loss | -18.2712 |
| avg_hold_time_bars | 2.4562 |
| exposure | 0.1320 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
