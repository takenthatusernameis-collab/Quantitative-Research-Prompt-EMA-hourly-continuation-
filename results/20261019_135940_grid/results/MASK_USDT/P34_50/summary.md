# EMA Hourly Continuation — MASK/USDT P34_50

**Symbol:** MASK/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 930 |
| net_profit_factor | 0.2792 |
| net_win_rate | 0.4075 |
| gross_profit_factor | 0.7377 |
| gross_win_rate | 0.4505 |
| sharpe_ratio | -10.4488 |
| sortino_ratio | -4.5540 |
| max_drawdown | 0.9973 |
| cagr | -0.9052 |
| net_avg_win | 10.1905 |
| net_avg_loss | -25.1094 |
| avg_hold_time_bars | 3.1699 |
| exposure | 0.1340 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
