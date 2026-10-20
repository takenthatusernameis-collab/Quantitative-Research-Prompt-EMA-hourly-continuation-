# EMA Hourly Continuation — DOGS/USDT P89_144

**Symbol:** DOGS/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.5287 |
| net_win_rate | 0.4502 |
| gross_profit_factor | 0.8393 |
| gross_win_rate | 0.4525 |
| sharpe_ratio | -4.7351 |
| sortino_ratio | -1.5119 |
| max_drawdown | 0.8058 |
| cagr | -0.5228 |
| net_avg_win | 44.9027 |
| net_avg_loss | -69.5499 |
| avg_hold_time_bars | 4.8032 |
| exposure | 0.1126 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
