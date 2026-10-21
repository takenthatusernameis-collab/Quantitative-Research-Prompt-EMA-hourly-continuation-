# EMA Hourly Continuation — ZETA/USDT P26_100

**Symbol:** ZETA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 455 |
| net_profit_factor | 0.8630 |
| net_win_rate | 0.5165 |
| gross_profit_factor | 1.0794 |
| gross_win_rate | 0.5165 |
| sharpe_ratio | -1.0771 |
| sortino_ratio | -0.3294 |
| max_drawdown | 0.4535 |
| cagr | -0.1431 |
| net_avg_win | 86.4433 |
| net_avg_loss | -107.0000 |
| avg_hold_time_bars | 17.6681 |
| exposure | 0.3638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
