# EMA Hourly Continuation — LUNC/USDT P8_21

**Symbol:** LUNC/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 486 |
| net_profit_factor | 0.7039 |
| net_win_rate | 0.4918 |
| gross_profit_factor | 0.9981 |
| gross_win_rate | 0.4918 |
| sharpe_ratio | -2.6441 |
| sortino_ratio | -0.8367 |
| max_drawdown | 0.6359 |
| cagr | -0.3180 |
| net_avg_win | 61.4134 |
| net_avg_loss | -84.4269 |
| avg_hold_time_bars | 5.0432 |
| exposure | 0.1114 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
