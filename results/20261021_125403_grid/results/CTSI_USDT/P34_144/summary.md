# EMA Hourly Continuation — CTSI/USDT P34_144

**Symbol:** CTSI/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.6968 |
| net_win_rate | 0.4623 |
| gross_profit_factor | 0.8773 |
| gross_win_rate | 0.4623 |
| sharpe_ratio | -2.4534 |
| sortino_ratio | -0.7073 |
| max_drawdown | 0.5646 |
| cagr | -0.2774 |
| net_avg_win | 67.4476 |
| net_avg_loss | -83.2220 |
| avg_hold_time_bars | 23.2263 |
| exposure | 0.4339 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
