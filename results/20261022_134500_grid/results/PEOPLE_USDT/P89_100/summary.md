# EMA Hourly Continuation — PEOPLE/USDT P89_100

**Symbol:** PEOPLE/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 608 |
| net_profit_factor | 0.4041 |
| net_win_rate | 0.4342 |
| gross_profit_factor | 0.8313 |
| gross_win_rate | 0.4638 |
| sharpe_ratio | -7.1777 |
| sortino_ratio | -2.5249 |
| max_drawdown | 0.9593 |
| cagr | -0.7163 |
| net_avg_win | 24.6131 |
| net_avg_loss | -46.7476 |
| avg_hold_time_bars | 2.5115 |
| exposure | 0.0691 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
