# EMA Hourly Continuation — TWT/USDT P21_34

**Symbol:** TWT/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.6620 |
| net_win_rate | 0.5251 |
| gross_profit_factor | 1.0660 |
| gross_win_rate | 0.5251 |
| sharpe_ratio | -2.2422 |
| sortino_ratio | -0.6139 |
| max_drawdown | 0.5289 |
| cagr | -0.2430 |
| net_avg_win | 52.3957 |
| net_avg_loss | -87.5282 |
| avg_hold_time_bars | 5.1257 |
| exposure | 0.0834 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
