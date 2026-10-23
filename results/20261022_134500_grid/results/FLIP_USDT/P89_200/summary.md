# EMA Hourly Continuation — FLIP/USDT P89_200

**Symbol:** FLIP/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 259 |
| net_profit_factor | 0.4588 |
| net_win_rate | 0.4093 |
| gross_profit_factor | 0.7068 |
| gross_win_rate | 0.4208 |
| sharpe_ratio | -3.7683 |
| sortino_ratio | -0.8526 |
| max_drawdown | 0.6506 |
| cagr | -0.3327 |
| net_avg_win | 51.0226 |
| net_avg_loss | -77.0395 |
| avg_hold_time_bars | 20.1892 |
| exposure | 0.2377 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
