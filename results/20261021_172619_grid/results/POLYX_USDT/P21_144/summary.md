# EMA Hourly Continuation — POLYX/USDT P21_144

**Symbol:** POLYX/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 399 |
| net_profit_factor | 0.8037 |
| net_win_rate | 0.5013 |
| gross_profit_factor | 0.9953 |
| gross_win_rate | 0.5013 |
| sharpe_ratio | -1.3720 |
| sortino_ratio | -0.3917 |
| max_drawdown | 0.4099 |
| cagr | -0.1664 |
| net_avg_win | 75.0849 |
| net_avg_loss | -93.8987 |
| avg_hold_time_bars | 28.5514 |
| exposure | 0.5178 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
