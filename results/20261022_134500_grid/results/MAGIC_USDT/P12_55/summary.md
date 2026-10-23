# EMA Hourly Continuation — MAGIC/USDT P12_55

**Symbol:** MAGIC/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 900 |
| net_profit_factor | 0.6899 |
| net_win_rate | 0.4844 |
| gross_profit_factor | 1.0465 |
| gross_win_rate | 0.4933 |
| sharpe_ratio | -4.3828 |
| sortino_ratio | -1.8620 |
| max_drawdown | 0.8973 |
| cagr | -0.5838 |
| net_avg_win | 45.3709 |
| net_avg_loss | -61.8001 |
| avg_hold_time_bars | 10.6211 |
| exposure | 0.4345 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
