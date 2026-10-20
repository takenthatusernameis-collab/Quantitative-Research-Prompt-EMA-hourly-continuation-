# EMA Hourly Continuation — BLUR/USDT P26_200

**Symbol:** BLUR/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.7891 |
| net_win_rate | 0.5141 |
| gross_profit_factor | 1.1090 |
| gross_win_rate | 0.5282 |
| sharpe_ratio | -1.3711 |
| sortino_ratio | -0.3621 |
| max_drawdown | 0.3769 |
| cagr | -0.1604 |
| net_avg_win | 73.3325 |
| net_avg_loss | -98.3346 |
| avg_hold_time_bars | 40.1638 |
| exposure | 0.6434 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
