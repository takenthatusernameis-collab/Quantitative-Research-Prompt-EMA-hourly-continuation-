# EMA Hourly Continuation — PHA/USDT P26_200

**Symbol:** PHA/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 448 |
| net_profit_factor | 0.5701 |
| net_win_rate | 0.4397 |
| gross_profit_factor | 0.7777 |
| gross_win_rate | 0.4420 |
| sharpe_ratio | -3.4817 |
| sortino_ratio | -1.0375 |
| max_drawdown | 0.7093 |
| cagr | -0.3866 |
| net_avg_win | 47.5967 |
| net_avg_loss | -65.5232 |
| avg_hold_time_bars | 25.9375 |
| exposure | 0.5282 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
