# EMA Hourly Continuation — AAVE/USDT P8_100

**Symbol:** AAVE/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 659 |
| net_profit_factor | 0.5322 |
| net_win_rate | 0.4461 |
| gross_profit_factor | 0.8244 |
| gross_win_rate | 0.4552 |
| sharpe_ratio | -4.8871 |
| sortino_ratio | -1.7463 |
| max_drawdown | 0.8880 |
| cagr | -0.5755 |
| net_avg_win | 34.1977 |
| net_avg_loss | -51.7578 |
| avg_hold_time_bars | 22.1320 |
| exposure | 0.6630 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
