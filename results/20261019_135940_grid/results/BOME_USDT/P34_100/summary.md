# EMA Hourly Continuation — BOME/USDT P34_100

**Symbol:** BOME/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.5640 |
| net_win_rate | 0.4754 |
| gross_profit_factor | 0.8298 |
| gross_win_rate | 0.4815 |
| sharpe_ratio | -3.6645 |
| sortino_ratio | -1.3088 |
| max_drawdown | 0.8061 |
| cagr | -0.4692 |
| net_avg_win | 33.3395 |
| net_avg_loss | -53.5608 |
| avg_hold_time_bars | 9.2400 |
| exposure | 0.2730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
