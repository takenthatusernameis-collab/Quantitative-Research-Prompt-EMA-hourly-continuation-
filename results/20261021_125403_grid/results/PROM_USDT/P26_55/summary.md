# EMA Hourly Continuation — PROM/USDT P26_55

**Symbol:** PROM/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 492 |
| net_profit_factor | 0.5769 |
| net_win_rate | 0.4492 |
| gross_profit_factor | 0.8293 |
| gross_win_rate | 0.4512 |
| sharpe_ratio | -3.8477 |
| sortino_ratio | -1.2146 |
| max_drawdown | 0.7562 |
| cagr | -0.4299 |
| net_avg_win | 46.6459 |
| net_avg_loss | -65.9436 |
| avg_hold_time_bars | 6.7967 |
| exposure | 0.1520 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
