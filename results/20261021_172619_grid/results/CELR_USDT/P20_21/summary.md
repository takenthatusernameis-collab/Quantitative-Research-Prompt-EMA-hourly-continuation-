# EMA Hourly Continuation — CELR/USDT P20_21

**Symbol:** CELR/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 261 |
| net_profit_factor | 0.5583 |
| net_win_rate | 0.4636 |
| gross_profit_factor | 0.8511 |
| gross_win_rate | 0.4636 |
| sharpe_ratio | -2.8605 |
| sortino_ratio | -0.6612 |
| max_drawdown | 0.5710 |
| cagr | -0.2626 |
| net_avg_win | 56.0229 |
| net_avg_loss | -86.7288 |
| avg_hold_time_bars | 4.2720 |
| exposure | 0.0505 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
