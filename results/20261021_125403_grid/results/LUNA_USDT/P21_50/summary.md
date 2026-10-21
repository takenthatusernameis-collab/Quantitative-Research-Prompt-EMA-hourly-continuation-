# EMA Hourly Continuation — LUNA/USDT P21_50

**Symbol:** LUNA/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 425 |
| net_profit_factor | 0.7163 |
| net_win_rate | 0.4847 |
| gross_profit_factor | 0.9685 |
| gross_win_rate | 0.4847 |
| sharpe_ratio | -2.3726 |
| sortino_ratio | -0.7004 |
| max_drawdown | 0.5566 |
| cagr | -0.2748 |
| net_avg_win | 67.8654 |
| net_avg_loss | -89.1205 |
| avg_hold_time_bars | 7.0776 |
| exposure | 0.1367 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
