# EMA Hourly Continuation — CETUS/USDT P21_50

**Symbol:** CETUS/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 987 |
| net_profit_factor | 0.5807 |
| net_win_rate | 0.4428 |
| gross_profit_factor | 0.9579 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -6.8909 |
| sortino_ratio | -3.0538 |
| max_drawdown | 0.9764 |
| cagr | -0.7688 |
| net_avg_win | 30.9059 |
| net_avg_loss | -42.2857 |
| avg_hold_time_bars | 4.7416 |
| exposure | 0.2118 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
