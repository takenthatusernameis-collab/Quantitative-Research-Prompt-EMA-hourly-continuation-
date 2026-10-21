# EMA Hourly Continuation — RSR/USDT P50_55

**Symbol:** RSR/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 110 |
| net_profit_factor | 0.7367 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9880 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -0.9671 |
| sortino_ratio | -0.1456 |
| max_drawdown | 0.1888 |
| cagr | -0.0645 |
| net_avg_win | 78.4054 |
| net_avg_loss | -106.4243 |
| avg_hold_time_bars | 5.0091 |
| exposure | 0.0250 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
