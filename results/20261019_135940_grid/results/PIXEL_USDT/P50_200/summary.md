# EMA Hourly Continuation — PIXEL/USDT P50_200

**Symbol:** PIXEL/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 356 |
| net_profit_factor | 0.7789 |
| net_win_rate | 0.5028 |
| gross_profit_factor | 1.0319 |
| gross_win_rate | 0.5084 |
| sharpe_ratio | -1.5087 |
| sortino_ratio | -0.4037 |
| max_drawdown | 0.4183 |
| cagr | -0.1727 |
| net_avg_win | 74.8122 |
| net_avg_loss | -97.1364 |
| avg_hold_time_bars | 27.5871 |
| exposure | 0.4444 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
