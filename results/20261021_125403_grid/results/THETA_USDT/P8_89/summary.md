# EMA Hourly Continuation — THETA/USDT P8_89

**Symbol:** THETA/USDT  |  **P_fast:** 8  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.8624 |
| net_win_rate | 0.5092 |
| gross_profit_factor | 1.0321 |
| gross_win_rate | 0.5092 |
| sharpe_ratio | -0.9900 |
| sortino_ratio | -0.3135 |
| max_drawdown | 0.3660 |
| cagr | -0.1375 |
| net_avg_win | 78.4248 |
| net_avg_loss | -94.3628 |
| avg_hold_time_bars | 29.2710 |
| exposure | 0.6480 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
