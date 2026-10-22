# EMA Hourly Continuation — MLK/USDT P26_55

**Symbol:** MLK/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.3852 |
| net_win_rate | 0.3653 |
| gross_profit_factor | 0.6038 |
| gross_win_rate | 0.3707 |
| sharpe_ratio | -5.5474 |
| sortino_ratio | -1.5244 |
| max_drawdown | 0.8401 |
| cagr | -0.5101 |
| net_avg_win | 38.1764 |
| net_avg_loss | -57.0473 |
| avg_hold_time_bars | 7.9413 |
| exposure | 0.1348 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
