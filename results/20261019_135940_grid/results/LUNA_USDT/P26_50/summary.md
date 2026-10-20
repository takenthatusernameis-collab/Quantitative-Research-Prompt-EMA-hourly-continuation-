# EMA Hourly Continuation — LUNA/USDT P26_50

**Symbol:** LUNA/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1065 |
| net_profit_factor | 0.4690 |
| net_win_rate | 0.4225 |
| gross_profit_factor | 0.9585 |
| gross_win_rate | 0.4441 |
| sharpe_ratio | -9.9702 |
| sortino_ratio | -4.6359 |
| max_drawdown | 0.9971 |
| cagr | -0.9029 |
| net_avg_win | 19.5746 |
| net_avg_loss | -30.5365 |
| avg_hold_time_bars | 3.1493 |
| exposure | 0.1525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
