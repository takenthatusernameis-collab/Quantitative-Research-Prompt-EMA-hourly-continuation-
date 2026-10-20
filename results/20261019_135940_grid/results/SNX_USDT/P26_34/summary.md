# EMA Hourly Continuation — SNX/USDT P26_34

**Symbol:** SNX/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1067 |
| net_profit_factor | 0.3042 |
| net_win_rate | 0.4180 |
| gross_profit_factor | 0.8576 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -10.8679 |
| sortino_ratio | -5.0799 |
| max_drawdown | 0.9986 |
| cagr | -0.9257 |
| net_avg_win | 9.7879 |
| net_avg_loss | -23.1098 |
| avg_hold_time_bars | 2.0131 |
| exposure | 0.0972 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
