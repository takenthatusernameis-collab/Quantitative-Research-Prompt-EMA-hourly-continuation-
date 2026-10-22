# EMA Hourly Continuation — KNC/USDT P26_34

**Symbol:** KNC/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.5184 |
| net_win_rate | 0.4665 |
| gross_profit_factor | 0.9064 |
| gross_win_rate | 0.4665 |
| sharpe_ratio | -4.0804 |
| sortino_ratio | -1.1118 |
| max_drawdown | 0.7371 |
| cagr | -0.4032 |
| net_avg_win | 46.8300 |
| net_avg_loss | -78.9784 |
| avg_hold_time_bars | 5.4190 |
| exposure | 0.0882 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
