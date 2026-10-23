# EMA Hourly Continuation — DYDX/USDT P55_144

**Symbol:** DYDX/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 521 |
| net_profit_factor | 0.6293 |
| net_win_rate | 0.4702 |
| gross_profit_factor | 0.9585 |
| gross_win_rate | 0.4779 |
| sharpe_ratio | -3.5710 |
| sortino_ratio | -1.1515 |
| max_drawdown | 0.7542 |
| cagr | -0.4205 |
| net_avg_win | 51.6927 |
| net_avg_loss | -72.9145 |
| avg_hold_time_bars | 10.4798 |
| exposure | 0.2482 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
