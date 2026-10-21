# EMA Hourly Continuation — DUSK/USDT P55_100

**Symbol:** DUSK/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 410 |
| net_profit_factor | 0.7133 |
| net_win_rate | 0.4829 |
| gross_profit_factor | 0.9161 |
| gross_win_rate | 0.4829 |
| sharpe_ratio | -2.0309 |
| sortino_ratio | -0.5875 |
| max_drawdown | 0.5081 |
| cagr | -0.2364 |
| net_avg_win | 61.8296 |
| net_avg_loss | -80.9555 |
| avg_hold_time_bars | 7.2390 |
| exposure | 0.1349 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
