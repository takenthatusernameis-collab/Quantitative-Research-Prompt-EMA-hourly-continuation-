# EMA Hourly Continuation — MERL/USDT P50_100

**Symbol:** MERL/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 609 |
| net_profit_factor | 0.6397 |
| net_win_rate | 0.4844 |
| gross_profit_factor | 0.9281 |
| gross_win_rate | 0.4877 |
| sharpe_ratio | -3.3195 |
| sortino_ratio | -1.1640 |
| max_drawdown | 0.7621 |
| cagr | -0.4196 |
| net_avg_win | 44.7707 |
| net_avg_loss | -65.7557 |
| avg_hold_time_bars | 6.5944 |
| exposure | 0.1831 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
