# EMA Hourly Continuation — AAVE/USDT P8_55

**Symbol:** AAVE/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1029 |
| net_profit_factor | 0.5772 |
| net_win_rate | 0.4529 |
| gross_profit_factor | 0.9120 |
| gross_win_rate | 0.4606 |
| sharpe_ratio | -6.3788 |
| sortino_ratio | -2.8712 |
| max_drawdown | 0.9705 |
| cagr | -0.7516 |
| net_avg_win | 28.4136 |
| net_avg_loss | -40.7423 |
| avg_hold_time_bars | 10.6569 |
| exposure | 0.4985 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
