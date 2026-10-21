# EMA Hourly Continuation — CKB/USDT P50_144

**Symbol:** CKB/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.7485 |
| net_win_rate | 0.4879 |
| gross_profit_factor | 0.9552 |
| gross_win_rate | 0.4879 |
| sharpe_ratio | -1.8273 |
| sortino_ratio | -0.5041 |
| max_drawdown | 0.4625 |
| cagr | -0.2078 |
| net_avg_win | 72.3973 |
| net_avg_loss | -92.1702 |
| avg_hold_time_bars | 14.9196 |
| exposure | 0.2530 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
