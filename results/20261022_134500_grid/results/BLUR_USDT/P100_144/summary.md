# EMA Hourly Continuation — BLUR/USDT P100_144

**Symbol:** BLUR/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 484 |
| net_profit_factor | 0.5814 |
| net_win_rate | 0.4959 |
| gross_profit_factor | 1.0277 |
| gross_win_rate | 0.5103 |
| sharpe_ratio | -3.5534 |
| sortino_ratio | -1.1100 |
| max_drawdown | 0.7359 |
| cagr | -0.4081 |
| net_avg_win | 42.4633 |
| net_avg_loss | -71.8346 |
| avg_hold_time_bars | 4.6756 |
| exposure | 0.1024 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
