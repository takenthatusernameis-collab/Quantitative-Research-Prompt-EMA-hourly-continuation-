# EMA Hourly Continuation — CPOOL/USDT P55_100

**Symbol:** CPOOL/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 687 |
| net_profit_factor | 0.5604 |
| net_win_rate | 0.4425 |
| gross_profit_factor | 0.8555 |
| gross_win_rate | 0.4498 |
| sharpe_ratio | -5.6694 |
| sortino_ratio | -2.0804 |
| max_drawdown | 0.9295 |
| cagr | -0.6410 |
| net_avg_win | 38.7364 |
| net_avg_loss | -54.8635 |
| avg_hold_time_bars | 4.0611 |
| exposure | 0.1268 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
