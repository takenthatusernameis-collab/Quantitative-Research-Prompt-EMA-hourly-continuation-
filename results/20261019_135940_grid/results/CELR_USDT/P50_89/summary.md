# EMA Hourly Continuation — CELR/USDT P50_89

**Symbol:** CELR/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 680 |
| net_profit_factor | 0.5206 |
| net_win_rate | 0.4544 |
| gross_profit_factor | 0.8789 |
| gross_win_rate | 0.4750 |
| sharpe_ratio | -5.1473 |
| sortino_ratio | -1.8987 |
| max_drawdown | 0.9012 |
| cagr | -0.5942 |
| net_avg_win | 31.5269 |
| net_avg_loss | -50.4417 |
| avg_hold_time_bars | 5.2824 |
| exposure | 0.1625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
