# EMA Hourly Continuation — JTO/USDT P8_144

**Symbol:** JTO/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.8168 |
| net_win_rate | 0.4840 |
| gross_profit_factor | 0.9320 |
| gross_win_rate | 0.4840 |
| sharpe_ratio | -1.1767 |
| sortino_ratio | -0.3253 |
| max_drawdown | 0.3803 |
| cagr | -0.1406 |
| net_avg_win | 77.5796 |
| net_avg_loss | -89.0998 |
| avg_hold_time_bars | 43.3245 |
| exposure | 0.7405 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
