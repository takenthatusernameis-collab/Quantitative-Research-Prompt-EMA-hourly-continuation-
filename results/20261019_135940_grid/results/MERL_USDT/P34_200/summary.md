# EMA Hourly Continuation — MERL/USDT P34_200

**Symbol:** MERL/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.6809 |
| net_win_rate | 0.4587 |
| gross_profit_factor | 0.9021 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -2.5838 |
| sortino_ratio | -0.7038 |
| max_drawdown | 0.5916 |
| cagr | -0.2826 |
| net_avg_win | 70.0501 |
| net_avg_loss | -87.1736 |
| avg_hold_time_bars | 29.8187 |
| exposure | 0.5097 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
