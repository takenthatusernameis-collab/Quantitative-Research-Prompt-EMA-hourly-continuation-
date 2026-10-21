# EMA Hourly Continuation — SUSHI/USDT P21_89

**Symbol:** SUSHI/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.7831 |
| net_win_rate | 0.4940 |
| gross_profit_factor | 0.9849 |
| gross_win_rate | 0.4940 |
| sharpe_ratio | -1.8047 |
| sortino_ratio | -0.5751 |
| max_drawdown | 0.5349 |
| cagr | -0.2330 |
| net_avg_win | 71.5975 |
| net_avg_loss | -89.2548 |
| avg_hold_time_bars | 16.6667 |
| exposure | 0.3756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
