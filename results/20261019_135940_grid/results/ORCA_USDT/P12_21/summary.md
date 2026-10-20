# EMA Hourly Continuation — ORCA/USDT P12_21

**Symbol:** ORCA/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1315 |
| net_profit_factor | 0.4653 |
| net_win_rate | 0.4517 |
| gross_profit_factor | 0.9768 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -9.5345 |
| sortino_ratio | -4.8609 |
| max_drawdown | 0.9981 |
| cagr | -0.9145 |
| net_avg_win | 14.6203 |
| net_avg_loss | -25.8858 |
| avg_hold_time_bars | 3.0540 |
| exposure | 0.1825 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
