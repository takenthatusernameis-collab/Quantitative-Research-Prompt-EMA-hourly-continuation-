# EMA Hourly Continuation — KMNO/USDT P50_200

**Symbol:** KMNO/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.7744 |
| net_win_rate | 0.4823 |
| gross_profit_factor | 0.9423 |
| gross_win_rate | 0.4823 |
| sharpe_ratio | -1.5041 |
| sortino_ratio | -0.3806 |
| max_drawdown | 0.3705 |
| cagr | -0.1621 |
| net_avg_win | 81.0642 |
| net_avg_loss | -97.5283 |
| avg_hold_time_bars | 25.3505 |
| exposure | 0.3640 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
