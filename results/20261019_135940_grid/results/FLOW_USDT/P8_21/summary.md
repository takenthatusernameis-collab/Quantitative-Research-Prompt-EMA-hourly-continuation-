# EMA Hourly Continuation — FLOW/USDT P8_21

**Symbol:** FLOW/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1749 |
| net_profit_factor | 0.2714 |
| net_win_rate | 0.4071 |
| gross_profit_factor | 0.6749 |
| gross_win_rate | 0.4380 |
| sharpe_ratio | -13.4938 |
| sortino_ratio | -8.0102 |
| max_drawdown | 1.0000 |
| cagr | -0.9822 |
| net_avg_win | 5.2323 |
| net_avg_loss | -13.2353 |
| avg_hold_time_bars | 2.9240 |
| exposure | 0.2325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
