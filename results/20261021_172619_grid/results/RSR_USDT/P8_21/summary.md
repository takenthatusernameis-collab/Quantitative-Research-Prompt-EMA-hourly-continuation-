# EMA Hourly Continuation — RSR/USDT P8_21

**Symbol:** RSR/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 582 |
| net_profit_factor | 0.7591 |
| net_win_rate | 0.5017 |
| gross_profit_factor | 0.9974 |
| gross_win_rate | 0.5017 |
| sharpe_ratio | -2.0625 |
| sortino_ratio | -0.7141 |
| max_drawdown | 0.5933 |
| cagr | -0.2792 |
| net_avg_win | 60.4927 |
| net_avg_loss | -80.2375 |
| avg_hold_time_bars | 5.8694 |
| exposure | 0.1553 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
