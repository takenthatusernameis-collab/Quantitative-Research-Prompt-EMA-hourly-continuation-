# EMA Hourly Continuation — PHA/USDT P50_55

**Symbol:** PHA/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 108 |
| net_profit_factor | 0.6775 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 0.9352 |
| gross_win_rate | 0.4815 |
| sharpe_ratio | -1.2760 |
| sortino_ratio | -0.1900 |
| max_drawdown | 0.2130 |
| cagr | -0.0826 |
| net_avg_win | 78.6749 |
| net_avg_loss | -107.8293 |
| avg_hold_time_bars | 4.0093 |
| exposure | 0.0197 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
