# EMA Hourly Continuation — PIXEL/USDT P12_200

**Symbol:** PIXEL/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.7834 |
| net_win_rate | 0.4966 |
| gross_profit_factor | 1.0364 |
| gross_win_rate | 0.5069 |
| sharpe_ratio | -1.3923 |
| sortino_ratio | -0.3334 |
| max_drawdown | 0.3858 |
| cagr | -0.1475 |
| net_avg_win | 83.2004 |
| net_avg_loss | -104.7549 |
| avg_hold_time_bars | 61.4069 |
| exposure | 0.8058 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
