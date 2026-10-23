# EMA Hourly Continuation — ELON/USDT P34_100

**Symbol:** ELON/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 660 |
| net_profit_factor | 0.4316 |
| net_win_rate | 0.4394 |
| gross_profit_factor | 0.7127 |
| gross_win_rate | 0.4409 |
| sharpe_ratio | -5.8359 |
| sortino_ratio | -2.1141 |
| max_drawdown | 0.9281 |
| cagr | -0.6414 |
| net_avg_win | 24.1949 |
| net_avg_loss | -43.9333 |
| avg_hold_time_bars | 7.8409 |
| exposure | 0.2352 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
