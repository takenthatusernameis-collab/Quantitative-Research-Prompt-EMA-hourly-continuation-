# EMA Hourly Continuation — SUPER/USDT P8_20

**Symbol:** SUPER/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1622 |
| net_profit_factor | 0.4563 |
| net_win_rate | 0.4470 |
| gross_profit_factor | 0.9307 |
| gross_win_rate | 0.4723 |
| sharpe_ratio | -10.2909 |
| sortino_ratio | -5.8199 |
| max_drawdown | 0.9993 |
| cagr | -0.9462 |
| net_avg_win | 11.5661 |
| net_avg_loss | -20.4893 |
| avg_hold_time_bars | 3.0506 |
| exposure | 0.2249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
