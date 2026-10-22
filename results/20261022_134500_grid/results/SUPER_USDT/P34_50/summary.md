# EMA Hourly Continuation — SUPER/USDT P34_50

**Symbol:** SUPER/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 905 |
| net_profit_factor | 0.3976 |
| net_win_rate | 0.4431 |
| gross_profit_factor | 0.7642 |
| gross_win_rate | 0.4685 |
| sharpe_ratio | -7.7208 |
| sortino_ratio | -3.3119 |
| max_drawdown | 0.9823 |
| cagr | -0.7971 |
| net_avg_win | 16.1622 |
| net_avg_loss | -32.3393 |
| avg_hold_time_bars | 3.2818 |
| exposure | 0.1350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
