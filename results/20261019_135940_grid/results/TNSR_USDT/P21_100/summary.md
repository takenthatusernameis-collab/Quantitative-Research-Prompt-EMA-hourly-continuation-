# EMA Hourly Continuation — TNSR/USDT P21_100

**Symbol:** TNSR/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 650 |
| net_profit_factor | 0.7111 |
| net_win_rate | 0.4862 |
| gross_profit_factor | 0.9954 |
| gross_win_rate | 0.4938 |
| sharpe_ratio | -3.1303 |
| sortino_ratio | -1.1204 |
| max_drawdown | 0.7621 |
| cagr | -0.4134 |
| net_avg_win | 57.6104 |
| net_avg_loss | -76.6475 |
| avg_hold_time_bars | 14.3985 |
| exposure | 0.4235 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
