# EMA Hourly Continuation — DEXE/USDT P21_55

**Symbol:** DEXE/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 903 |
| net_profit_factor | 0.4422 |
| net_win_rate | 0.4286 |
| gross_profit_factor | 0.7947 |
| gross_win_rate | 0.4419 |
| sharpe_ratio | -7.4795 |
| sortino_ratio | -3.1536 |
| max_drawdown | 0.9809 |
| cagr | -0.7909 |
| net_avg_win | 20.0799 |
| net_avg_loss | -34.0591 |
| avg_hold_time_bars | 8.1550 |
| exposure | 0.3347 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
