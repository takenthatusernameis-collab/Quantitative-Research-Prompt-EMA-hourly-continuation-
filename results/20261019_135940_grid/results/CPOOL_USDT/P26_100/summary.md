# EMA Hourly Continuation — CPOOL/USDT P26_100

**Symbol:** CPOOL/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 757 |
| net_profit_factor | 0.6491 |
| net_win_rate | 0.4782 |
| gross_profit_factor | 0.8848 |
| gross_win_rate | 0.4808 |
| sharpe_ratio | -3.7766 |
| sortino_ratio | -1.4666 |
| max_drawdown | 0.8534 |
| cagr | -0.5000 |
| net_avg_win | 42.1368 |
| net_avg_loss | -59.4916 |
| avg_hold_time_bars | 7.8151 |
| exposure | 0.2689 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
