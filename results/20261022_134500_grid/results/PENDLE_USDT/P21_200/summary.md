# EMA Hourly Continuation — PENDLE/USDT P21_200

**Symbol:** PENDLE/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.5955 |
| net_win_rate | 0.4379 |
| gross_profit_factor | 0.8063 |
| gross_win_rate | 0.4379 |
| sharpe_ratio | -3.1171 |
| sortino_ratio | -0.7802 |
| max_drawdown | 0.6322 |
| cagr | -0.3141 |
| net_avg_win | 63.9039 |
| net_avg_loss | -83.5975 |
| avg_hold_time_bars | 48.6180 |
| exposure | 0.7116 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
