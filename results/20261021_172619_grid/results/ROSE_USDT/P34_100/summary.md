# EMA Hourly Continuation — ROSE/USDT P34_100

**Symbol:** ROSE/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.8537 |
| net_win_rate | 0.5172 |
| gross_profit_factor | 1.0669 |
| gross_win_rate | 0.5172 |
| sharpe_ratio | -1.0556 |
| sortino_ratio | -0.3164 |
| max_drawdown | 0.3810 |
| cagr | -0.1377 |
| net_avg_win | 80.5418 |
| net_avg_loss | -101.0846 |
| avg_hold_time_bars | 13.6989 |
| exposure | 0.2709 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
