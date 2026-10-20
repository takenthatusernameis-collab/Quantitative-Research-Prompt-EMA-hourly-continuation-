# EMA Hourly Continuation — ARPA/USDT P89_144

**Symbol:** ARPA/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.4318 |
| net_win_rate | 0.4091 |
| gross_profit_factor | 0.7620 |
| gross_win_rate | 0.4218 |
| sharpe_ratio | -6.4504 |
| sortino_ratio | -2.1549 |
| max_drawdown | 0.9265 |
| cagr | -0.6435 |
| net_avg_win | 31.2718 |
| net_avg_loss | -50.1374 |
| avg_hold_time_bars | 5.7145 |
| exposure | 0.1422 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
