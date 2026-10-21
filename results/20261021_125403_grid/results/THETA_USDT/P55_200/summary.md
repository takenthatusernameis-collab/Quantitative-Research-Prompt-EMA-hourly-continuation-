# EMA Hourly Continuation — THETA/USDT P55_200

**Symbol:** THETA/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.8427 |
| net_win_rate | 0.5143 |
| gross_profit_factor | 1.0358 |
| gross_win_rate | 0.5143 |
| sharpe_ratio | -0.7920 |
| sortino_ratio | -0.1904 |
| max_drawdown | 0.2417 |
| cagr | -0.0857 |
| net_avg_win | 74.9277 |
| net_avg_loss | -94.1423 |
| avg_hold_time_bars | 29.5857 |
| exposure | 0.3765 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
