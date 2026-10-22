# EMA Hourly Continuation — PUFFER/USDT P55_89

**Symbol:** PUFFER/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 275 |
| net_profit_factor | 0.7475 |
| net_win_rate | 0.4909 |
| gross_profit_factor | 0.9695 |
| gross_win_rate | 0.4909 |
| sharpe_ratio | -1.7272 |
| sortino_ratio | -0.4574 |
| max_drawdown | 0.3973 |
| cagr | -0.1891 |
| net_avg_win | 75.6154 |
| net_avg_loss | -97.5388 |
| avg_hold_time_bars | 8.3491 |
| exposure | 0.1299 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
