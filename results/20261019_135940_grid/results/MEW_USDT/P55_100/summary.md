# EMA Hourly Continuation — MEW/USDT P55_100

**Symbol:** MEW/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 628 |
| net_profit_factor | 0.5219 |
| net_win_rate | 0.4379 |
| gross_profit_factor | 0.8049 |
| gross_win_rate | 0.4459 |
| sharpe_ratio | -5.5505 |
| sortino_ratio | -1.9525 |
| max_drawdown | 0.9112 |
| cagr | -0.6131 |
| net_avg_win | 36.0322 |
| net_avg_loss | -53.7894 |
| avg_hold_time_bars | 5.6927 |
| exposure | 0.1625 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
