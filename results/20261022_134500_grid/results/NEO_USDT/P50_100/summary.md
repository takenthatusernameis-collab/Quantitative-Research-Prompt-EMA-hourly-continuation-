# EMA Hourly Continuation — NEO/USDT P50_100

**Symbol:** NEO/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 646 |
| net_profit_factor | 0.4379 |
| net_win_rate | 0.4396 |
| gross_profit_factor | 0.8416 |
| gross_win_rate | 0.4690 |
| sharpe_ratio | -6.0838 |
| sortino_ratio | -2.1975 |
| max_drawdown | 0.9310 |
| cagr | -0.6509 |
| net_avg_win | 25.4767 |
| net_avg_loss | -45.6461 |
| avg_hold_time_bars | 6.1486 |
| exposure | 0.1805 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
