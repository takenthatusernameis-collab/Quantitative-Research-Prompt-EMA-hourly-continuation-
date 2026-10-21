# EMA Hourly Continuation — RSR/USDT P12_100

**Symbol:** RSR/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 516 |
| net_profit_factor | 0.8165 |
| net_win_rate | 0.4922 |
| gross_profit_factor | 0.9645 |
| gross_win_rate | 0.4922 |
| sharpe_ratio | -1.4382 |
| sortino_ratio | -0.4667 |
| max_drawdown | 0.4882 |
| cagr | -0.1951 |
| net_avg_win | 73.5864 |
| net_avg_loss | -87.3775 |
| avg_hold_time_bars | 22.8081 |
| exposure | 0.5350 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
