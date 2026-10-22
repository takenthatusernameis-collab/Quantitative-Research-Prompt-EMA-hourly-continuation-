# EMA Hourly Continuation — ELON/USDT P26_55

**Symbol:** ELON/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 364 |
| net_profit_factor | 0.6075 |
| net_win_rate | 0.4560 |
| gross_profit_factor | 0.8344 |
| gross_win_rate | 0.4560 |
| sharpe_ratio | -2.9983 |
| sortino_ratio | -0.8162 |
| max_drawdown | 0.6129 |
| cagr | -0.3125 |
| net_avg_win | 56.8452 |
| net_avg_loss | -78.4506 |
| avg_hold_time_bars | 8.1648 |
| exposure | 0.1351 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
