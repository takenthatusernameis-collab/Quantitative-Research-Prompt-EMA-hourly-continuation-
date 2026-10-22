# EMA Hourly Continuation — LUNA/USDT P26_100

**Symbol:** LUNA/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 415 |
| net_profit_factor | 0.7699 |
| net_win_rate | 0.4916 |
| gross_profit_factor | 0.9802 |
| gross_win_rate | 0.4916 |
| sharpe_ratio | -1.8026 |
| sortino_ratio | -0.5253 |
| max_drawdown | 0.4881 |
| cagr | -0.2148 |
| net_avg_win | 74.6797 |
| net_avg_loss | -93.7778 |
| avg_hold_time_bars | 15.4096 |
| exposure | 0.2907 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
