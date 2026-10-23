# EMA Hourly Continuation — MINA/USDT P21_50

**Symbol:** MINA/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 974 |
| net_profit_factor | 0.5740 |
| net_win_rate | 0.4784 |
| gross_profit_factor | 1.0432 |
| gross_win_rate | 0.4990 |
| sharpe_ratio | -5.9014 |
| sortino_ratio | -2.6053 |
| max_drawdown | 0.9591 |
| cagr | -0.7133 |
| net_avg_win | 27.6612 |
| net_avg_loss | -44.2047 |
| avg_hold_time_bars | 5.3799 |
| exposure | 0.2382 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
