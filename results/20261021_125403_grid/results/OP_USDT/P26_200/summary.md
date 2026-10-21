# EMA Hourly Continuation — OP/USDT P26_200

**Symbol:** OP/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 257 |
| net_profit_factor | 0.7982 |
| net_win_rate | 0.4864 |
| gross_profit_factor | 0.9405 |
| gross_win_rate | 0.4864 |
| sharpe_ratio | -1.1290 |
| sortino_ratio | -0.2577 |
| max_drawdown | 0.3042 |
| cagr | -0.1125 |
| net_avg_win | 81.9802 |
| net_avg_loss | -97.2542 |
| avg_hold_time_bars | 51.7743 |
| exposure | 0.6048 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
