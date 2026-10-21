# EMA Hourly Continuation — POL/USDT P55_100

**Symbol:** POL/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.6563 |
| net_win_rate | 0.4942 |
| gross_profit_factor | 0.9062 |
| gross_win_rate | 0.4942 |
| sharpe_ratio | -2.0300 |
| sortino_ratio | -0.5381 |
| max_drawdown | 0.4698 |
| cagr | -0.2184 |
| net_avg_win | 52.1487 |
| net_avg_loss | -77.6194 |
| avg_hold_time_bars | 9.7515 |
| exposure | 0.1516 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
