# EMA Hourly Continuation — SAND/USDT P26_200

**Symbol:** SAND/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 352 |
| net_profit_factor | 0.6274 |
| net_win_rate | 0.4688 |
| gross_profit_factor | 0.9089 |
| gross_win_rate | 0.4744 |
| sharpe_ratio | -2.7011 |
| sortino_ratio | -0.7106 |
| max_drawdown | 0.5907 |
| cagr | -0.2879 |
| net_avg_win | 58.5425 |
| net_avg_loss | -82.3339 |
| avg_hold_time_bars | 36.8494 |
| exposure | 0.5896 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
