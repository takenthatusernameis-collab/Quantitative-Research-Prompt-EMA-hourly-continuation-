# EMA Hourly Continuation — LUNC/USDT P8_50

**Symbol:** LUNC/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1243 |
| net_profit_factor | 0.4112 |
| net_win_rate | 0.4191 |
| gross_profit_factor | 0.7697 |
| gross_win_rate | 0.4328 |
| sharpe_ratio | -9.3902 |
| sortino_ratio | -4.6594 |
| max_drawdown | 0.9969 |
| cagr | -0.8989 |
| net_avg_win | 13.3599 |
| net_avg_loss | -23.4472 |
| avg_hold_time_bars | 7.8753 |
| exposure | 0.4450 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
