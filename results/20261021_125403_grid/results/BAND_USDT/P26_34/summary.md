# EMA Hourly Continuation — BAND/USDT P26_34

**Symbol:** BAND/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 396 |
| net_profit_factor | 0.6059 |
| net_win_rate | 0.4975 |
| gross_profit_factor | 0.9935 |
| gross_win_rate | 0.5025 |
| sharpe_ratio | -3.0965 |
| sortino_ratio | -0.8873 |
| max_drawdown | 0.6506 |
| cagr | -0.3315 |
| net_avg_win | 49.7751 |
| net_avg_loss | -81.3283 |
| avg_hold_time_bars | 4.5960 |
| exposure | 0.0824 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
