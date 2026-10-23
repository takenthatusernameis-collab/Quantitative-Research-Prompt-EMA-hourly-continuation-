# EMA Hourly Continuation — BAND/USDT P20_200

**Symbol:** BAND/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 355 |
| net_profit_factor | 0.7496 |
| net_win_rate | 0.4958 |
| gross_profit_factor | 0.9827 |
| gross_win_rate | 0.5014 |
| sharpe_ratio | -1.6448 |
| sortino_ratio | -0.4389 |
| max_drawdown | 0.4223 |
| cagr | -0.1854 |
| net_avg_win | 68.6974 |
| net_avg_loss | -90.1094 |
| avg_hold_time_bars | 40.4901 |
| exposure | 0.6504 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
