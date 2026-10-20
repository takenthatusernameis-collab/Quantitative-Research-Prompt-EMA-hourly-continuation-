# EMA Hourly Continuation — ASTR/USDT P144_200

**Symbol:** ASTR/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.4620 |
| net_win_rate | 0.4533 |
| gross_profit_factor | 0.8511 |
| gross_win_rate | 0.4720 |
| sharpe_ratio | -4.3109 |
| sortino_ratio | -1.1848 |
| max_drawdown | 0.7655 |
| cagr | -0.4316 |
| net_avg_win | 38.3606 |
| net_avg_loss | -68.8608 |
| avg_hold_time_bars | 6.6587 |
| exposure | 0.1130 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
