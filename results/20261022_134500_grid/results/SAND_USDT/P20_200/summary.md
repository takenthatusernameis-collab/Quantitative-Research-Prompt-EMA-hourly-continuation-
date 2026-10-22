# EMA Hourly Continuation — SAND/USDT P20_200

**Symbol:** SAND/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.6125 |
| net_win_rate | 0.4537 |
| gross_profit_factor | 0.9053 |
| gross_win_rate | 0.4630 |
| sharpe_ratio | -3.0183 |
| sortino_ratio | -0.7555 |
| max_drawdown | 0.6228 |
| cagr | -0.3081 |
| net_avg_win | 64.8871 |
| net_avg_loss | -87.9834 |
| avg_hold_time_bars | 45.5802 |
| exposure | 0.6713 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
