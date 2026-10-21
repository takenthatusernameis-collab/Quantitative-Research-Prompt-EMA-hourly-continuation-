# EMA Hourly Continuation — HNT/USDT P26_144

**Symbol:** HNT/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 367 |
| net_profit_factor | 0.6763 |
| net_win_rate | 0.4523 |
| gross_profit_factor | 0.7952 |
| gross_win_rate | 0.4523 |
| sharpe_ratio | -2.1782 |
| sortino_ratio | -0.5903 |
| max_drawdown | 0.5410 |
| cagr | -0.2387 |
| net_avg_win | 62.4105 |
| net_avg_loss | -76.2137 |
| avg_hold_time_bars | 27.3896 |
| exposure | 0.4569 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
