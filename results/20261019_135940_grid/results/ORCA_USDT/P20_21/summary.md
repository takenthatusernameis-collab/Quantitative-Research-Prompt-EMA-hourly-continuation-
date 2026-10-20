# EMA Hourly Continuation — ORCA/USDT P20_21

**Symbol:** ORCA/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1111 |
| net_profit_factor | 0.1963 |
| net_win_rate | 0.3375 |
| gross_profit_factor | 0.7322 |
| gross_win_rate | 0.4275 |
| sharpe_ratio | -15.1762 |
| sortino_ratio | -7.4991 |
| max_drawdown | 1.0000 |
| cagr | -0.9845 |
| net_avg_win | 6.5113 |
| net_avg_loss | -16.9042 |
| avg_hold_time_bars | 2.2061 |
| exposure | 0.1114 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
