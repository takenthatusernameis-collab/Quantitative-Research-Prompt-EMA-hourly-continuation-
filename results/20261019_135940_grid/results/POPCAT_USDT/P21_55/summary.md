# EMA Hourly Continuation — POPCAT/USDT P21_55

**Symbol:** POPCAT/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 834 |
| net_profit_factor | 0.5269 |
| net_win_rate | 0.4317 |
| gross_profit_factor | 0.7632 |
| gross_win_rate | 0.4376 |
| sharpe_ratio | -6.6974 |
| sortino_ratio | -2.9317 |
| max_drawdown | 0.9532 |
| cagr | -0.7576 |
| net_avg_win | 29.4870 |
| net_avg_loss | -42.5051 |
| avg_hold_time_bars | 5.2962 |
| exposure | 0.2333 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
