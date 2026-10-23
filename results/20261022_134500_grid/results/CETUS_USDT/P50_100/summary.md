# EMA Hourly Continuation — CETUS/USDT P50_100

**Symbol:** CETUS/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 631 |
| net_profit_factor | 0.6132 |
| net_win_rate | 0.4723 |
| gross_profit_factor | 0.9475 |
| gross_win_rate | 0.4849 |
| sharpe_ratio | -4.1060 |
| sortino_ratio | -1.4585 |
| max_drawdown | 0.8272 |
| cagr | -0.4988 |
| net_avg_win | 43.8864 |
| net_avg_loss | -64.0463 |
| avg_hold_time_bars | 6.1933 |
| exposure | 0.1768 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
