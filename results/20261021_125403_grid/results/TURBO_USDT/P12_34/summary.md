# EMA Hourly Continuation — TURBO/USDT P12_34

**Symbol:** TURBO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.8415 |
| net_win_rate | 0.5195 |
| gross_profit_factor | 1.0753 |
| gross_win_rate | 0.5195 |
| sharpe_ratio | -1.3497 |
| sortino_ratio | -0.4697 |
| max_drawdown | 0.4117 |
| cagr | -0.1964 |
| net_avg_win | 77.0343 |
| net_avg_loss | -98.9819 |
| avg_hold_time_bars | 6.3758 |
| exposure | 0.1694 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
