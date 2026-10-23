# EMA Hourly Continuation — SLP/USDT P26_50

**Symbol:** SLP/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1092 |
| net_profit_factor | 0.5080 |
| net_win_rate | 0.4222 |
| gross_profit_factor | 0.9111 |
| gross_win_rate | 0.4368 |
| sharpe_ratio | -9.3885 |
| sortino_ratio | -4.4083 |
| max_drawdown | 0.9960 |
| cagr | -0.8875 |
| net_avg_win | 22.3081 |
| net_avg_loss | -32.0803 |
| avg_hold_time_bars | 3.4020 |
| exposure | 0.1689 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
