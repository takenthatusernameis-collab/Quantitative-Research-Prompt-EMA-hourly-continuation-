# EMA Hourly Continuation — CELR/USDT P12_55

**Symbol:** CELR/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 700 |
| net_profit_factor | 0.6609 |
| net_win_rate | 0.4543 |
| gross_profit_factor | 0.8533 |
| gross_win_rate | 0.4543 |
| sharpe_ratio | -3.7420 |
| sortino_ratio | -1.4040 |
| max_drawdown | 0.8114 |
| cagr | -0.4754 |
| net_avg_win | 49.2605 |
| net_avg_loss | -62.0441 |
| avg_hold_time_bars | 11.6557 |
| exposure | 0.3692 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
