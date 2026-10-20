# EMA Hourly Continuation — MEME/USDT P8_50

**Symbol:** MEME/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1125 |
| net_profit_factor | 0.6408 |
| net_win_rate | 0.4738 |
| gross_profit_factor | 0.9735 |
| gross_win_rate | 0.4844 |
| sharpe_ratio | -5.1378 |
| sortino_ratio | -2.4341 |
| max_drawdown | 0.9464 |
| cagr | -0.6835 |
| net_avg_win | 31.6049 |
| net_avg_loss | -44.4073 |
| avg_hold_time_bars | 8.8498 |
| exposure | 0.4525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
