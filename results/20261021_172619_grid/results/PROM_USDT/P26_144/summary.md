# EMA Hourly Continuation — PROM/USDT P26_144

**Symbol:** PROM/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.5717 |
| net_win_rate | 0.4386 |
| gross_profit_factor | 0.7769 |
| gross_win_rate | 0.4434 |
| sharpe_ratio | -3.4582 |
| sortino_ratio | -0.9946 |
| max_drawdown | 0.6949 |
| cagr | -0.3709 |
| net_avg_win | 50.4413 |
| net_avg_loss | -68.9181 |
| avg_hold_time_bars | 22.7494 |
| exposure | 0.4291 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
