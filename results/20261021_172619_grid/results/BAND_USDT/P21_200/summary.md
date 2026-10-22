# EMA Hourly Continuation — BAND/USDT P21_200

**Symbol:** BAND/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 317 |
| net_profit_factor | 0.8276 |
| net_win_rate | 0.5047 |
| gross_profit_factor | 1.0071 |
| gross_win_rate | 0.5047 |
| sharpe_ratio | -1.0297 |
| sortino_ratio | -0.2616 |
| max_drawdown | 0.3072 |
| cagr | -0.1149 |
| net_avg_win | 79.5339 |
| net_avg_loss | -97.9396 |
| avg_hold_time_bars | 43.6467 |
| exposure | 0.6261 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
