# EMA Hourly Continuation — CTSI/USDT P26_100

**Symbol:** CTSI/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 719 |
| net_profit_factor | 0.6009 |
| net_win_rate | 0.4451 |
| gross_profit_factor | 0.9246 |
| gross_win_rate | 0.4506 |
| sharpe_ratio | -5.2660 |
| sortino_ratio | -1.9776 |
| max_drawdown | 0.9161 |
| cagr | -0.6171 |
| net_avg_win | 42.8223 |
| net_avg_loss | -57.1568 |
| avg_hold_time_bars | 10.7191 |
| exposure | 0.3503 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
