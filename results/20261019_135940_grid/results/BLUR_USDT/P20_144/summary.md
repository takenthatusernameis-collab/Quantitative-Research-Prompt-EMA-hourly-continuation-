# EMA Hourly Continuation — BLUR/USDT P20_144

**Symbol:** BLUR/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.7642 |
| net_win_rate | 0.5033 |
| gross_profit_factor | 1.0730 |
| gross_win_rate | 0.5165 |
| sharpe_ratio | -1.8834 |
| sortino_ratio | -0.5668 |
| max_drawdown | 0.5152 |
| cagr | -0.2368 |
| net_avg_win | 69.9447 |
| net_avg_loss | -92.7386 |
| avg_hold_time_bars | 30.1363 |
| exposure | 0.6205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
