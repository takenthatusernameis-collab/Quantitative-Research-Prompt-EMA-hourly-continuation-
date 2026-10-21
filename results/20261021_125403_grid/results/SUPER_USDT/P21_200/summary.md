# EMA Hourly Continuation — SUPER/USDT P21_200

**Symbol:** SUPER/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 306 |
| net_profit_factor | 0.9677 |
| net_win_rate | 0.5359 |
| gross_profit_factor | 1.1600 |
| gross_win_rate | 0.5392 |
| sharpe_ratio | -0.1275 |
| sortino_ratio | -0.0322 |
| max_drawdown | 0.2218 |
| cagr | -0.0200 |
| net_avg_win | 90.2049 |
| net_avg_loss | -107.6606 |
| avg_hold_time_bars | 44.8660 |
| exposure | 0.6240 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
