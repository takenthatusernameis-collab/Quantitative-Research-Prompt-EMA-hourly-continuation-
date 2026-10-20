# EMA Hourly Continuation — SYN/USDT P21_34

**Symbol:** SYN/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1103 |
| net_profit_factor | 0.4030 |
| net_win_rate | 0.4252 |
| gross_profit_factor | 0.7837 |
| gross_win_rate | 0.4451 |
| sharpe_ratio | -8.9639 |
| sortino_ratio | -4.1857 |
| max_drawdown | 0.9948 |
| cagr | -0.8770 |
| net_avg_win | 14.3196 |
| net_avg_loss | -26.2840 |
| avg_hold_time_bars | 2.9275 |
| exposure | 0.1468 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
