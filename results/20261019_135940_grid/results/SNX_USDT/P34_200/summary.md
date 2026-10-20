# EMA Hourly Continuation — SNX/USDT P34_200

**Symbol:** SNX/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 419 |
| net_profit_factor | 0.7113 |
| net_win_rate | 0.4869 |
| gross_profit_factor | 0.9998 |
| gross_win_rate | 0.4916 |
| sharpe_ratio | -2.3985 |
| sortino_ratio | -0.6936 |
| max_drawdown | 0.5799 |
| cagr | -0.2766 |
| net_avg_win | 67.4115 |
| net_avg_loss | -89.9237 |
| avg_hold_time_bars | 24.5298 |
| exposure | 0.4651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
