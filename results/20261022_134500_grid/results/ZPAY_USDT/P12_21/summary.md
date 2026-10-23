# EMA Hourly Continuation — ZPAY/USDT P12_21

**Symbol:** ZPAY/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1047 |
| net_profit_factor | 0.3519 |
| net_win_rate | 0.3286 |
| gross_profit_factor | 0.6684 |
| gross_win_rate | 0.3391 |
| sharpe_ratio | -11.0086 |
| sortino_ratio | -4.9773 |
| max_drawdown | 0.9978 |
| cagr | -0.9110 |
| net_avg_win | 15.7489 |
| net_avg_loss | -21.8993 |
| avg_hold_time_bars | 5.0172 |
| exposure | 0.2377 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
