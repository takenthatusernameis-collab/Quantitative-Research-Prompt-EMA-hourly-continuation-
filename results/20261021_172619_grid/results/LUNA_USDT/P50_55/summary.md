# EMA Hourly Continuation — LUNA/USDT P50_55

**Symbol:** LUNA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 79 |
| net_profit_factor | 0.8909 |
| net_win_rate | 0.5570 |
| gross_profit_factor | 1.2390 |
| gross_win_rate | 0.5570 |
| sharpe_ratio | -0.2810 |
| sortino_ratio | -0.0363 |
| max_drawdown | 0.1097 |
| cagr | -0.0172 |
| net_avg_win | 79.2322 |
| net_avg_loss | -111.8061 |
| avg_hold_time_bars | 7.2532 |
| exposure | 0.0260 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
