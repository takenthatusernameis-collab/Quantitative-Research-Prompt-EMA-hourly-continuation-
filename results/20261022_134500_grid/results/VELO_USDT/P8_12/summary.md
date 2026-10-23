# EMA Hourly Continuation — VELO/USDT P8_12

**Symbol:** VELO/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1838 |
| net_profit_factor | 0.3953 |
| net_win_rate | 0.3945 |
| gross_profit_factor | 0.8113 |
| gross_win_rate | 0.4211 |
| sharpe_ratio | -15.7000 |
| sortino_ratio | -9.5479 |
| max_drawdown | 1.0000 |
| cagr | -0.9938 |
| net_avg_win | 9.0174 |
| net_avg_loss | -14.8586 |
| avg_hold_time_bars | 1.8286 |
| exposure | 0.1528 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
