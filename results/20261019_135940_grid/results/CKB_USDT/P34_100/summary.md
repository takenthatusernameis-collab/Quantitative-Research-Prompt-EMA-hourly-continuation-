# EMA Hourly Continuation — CKB/USDT P34_100

**Symbol:** CKB/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 652 |
| net_profit_factor | 0.5795 |
| net_win_rate | 0.4540 |
| gross_profit_factor | 0.8971 |
| gross_win_rate | 0.4678 |
| sharpe_ratio | -4.9383 |
| sortino_ratio | -1.7764 |
| max_drawdown | 0.8876 |
| cagr | -0.5752 |
| net_avg_win | 41.1286 |
| net_avg_loss | -59.0152 |
| avg_hold_time_bars | 9.2239 |
| exposure | 0.2734 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
