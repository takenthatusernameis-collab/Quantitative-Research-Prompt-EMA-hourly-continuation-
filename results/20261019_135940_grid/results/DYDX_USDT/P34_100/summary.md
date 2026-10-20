# EMA Hourly Continuation — DYDX/USDT P34_100

**Symbol:** DYDX/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 679 |
| net_profit_factor | 0.6672 |
| net_win_rate | 0.4831 |
| gross_profit_factor | 1.0030 |
| gross_win_rate | 0.4919 |
| sharpe_ratio | -3.8620 |
| sortino_ratio | -1.4182 |
| max_drawdown | 0.8298 |
| cagr | -0.4907 |
| net_avg_win | 49.8948 |
| net_avg_loss | -69.8814 |
| avg_hold_time_bars | 8.8071 |
| exposure | 0.2718 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
