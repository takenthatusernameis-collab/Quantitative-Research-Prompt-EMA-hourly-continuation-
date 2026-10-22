# EMA Hourly Continuation — COTI/USDT P34_200

**Symbol:** COTI/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 286 |
| net_profit_factor | 1.0781 |
| net_win_rate | 0.5594 |
| gross_profit_factor | 1.2583 |
| gross_win_rate | 0.5594 |
| sharpe_ratio | 0.4590 |
| sortino_ratio | 0.1132 |
| max_drawdown | 0.1833 |
| cagr | 0.0441 |
| net_avg_win | 98.6441 |
| net_avg_loss | -116.1847 |
| avg_hold_time_bars | 39.6434 |
| exposure | 0.5154 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
