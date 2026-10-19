# EMA Hourly Continuation — NEAR/USDT P8_12

**Symbol:** NEAR/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1869 |
| net_profit_factor | 0.2487 |
| net_win_rate | 0.3719 |
| gross_profit_factor | 0.7340 |
| gross_win_rate | 0.4024 |
| sharpe_ratio | -17.5824 |
| sortino_ratio | -10.9767 |
| max_drawdown | 1.0000 |
| cagr | -0.9971 |
| net_avg_win | 4.7619 |
| net_avg_loss | -11.3369 |
| avg_hold_time_bars | 1.6581 |
| exposure | 0.1409 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
