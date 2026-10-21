# EMA Hourly Continuation — CKB/USDT P55_100

**Symbol:** CKB/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 351 |
| net_profit_factor | 0.7736 |
| net_win_rate | 0.5100 |
| gross_profit_factor | 1.0553 |
| gross_win_rate | 0.5100 |
| sharpe_ratio | -1.6360 |
| sortino_ratio | -0.4405 |
| max_drawdown | 0.4297 |
| cagr | -0.1832 |
| net_avg_win | 76.0702 |
| net_avg_loss | -102.3289 |
| avg_hold_time_bars | 7.5527 |
| exposure | 0.1205 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
