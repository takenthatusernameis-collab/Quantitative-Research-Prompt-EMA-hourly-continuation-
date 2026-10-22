# EMA Hourly Continuation — PIXEL/USDT P20_100

**Symbol:** PIXEL/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 589 |
| net_profit_factor | 0.7424 |
| net_win_rate | 0.4907 |
| gross_profit_factor | 1.0132 |
| gross_win_rate | 0.4992 |
| sharpe_ratio | -2.4616 |
| sortino_ratio | -0.8462 |
| max_drawdown | 0.6708 |
| cagr | -0.3280 |
| net_avg_win | 63.1492 |
| net_avg_loss | -81.9389 |
| avg_hold_time_bars | 18.3311 |
| exposure | 0.4886 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
