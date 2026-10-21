# EMA Hourly Continuation — TURBO/USDT P20_200

**Symbol:** TURBO/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 253 |
| net_profit_factor | 0.7543 |
| net_win_rate | 0.4664 |
| gross_profit_factor | 0.8739 |
| gross_win_rate | 0.4664 |
| sharpe_ratio | -1.6231 |
| sortino_ratio | -0.4006 |
| max_drawdown | 0.3871 |
| cagr | -0.1695 |
| net_avg_win | 83.8136 |
| net_avg_loss | -97.1178 |
| avg_hold_time_bars | 46.1186 |
| exposure | 0.6365 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
