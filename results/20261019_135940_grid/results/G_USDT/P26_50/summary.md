# EMA Hourly Continuation — G/USDT P26_50

**Symbol:** G/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 752 |
| net_profit_factor | 0.4848 |
| net_win_rate | 0.4495 |
| gross_profit_factor | 0.9292 |
| gross_win_rate | 0.4681 |
| sharpe_ratio | -7.1081 |
| sortino_ratio | -2.9784 |
| max_drawdown | 0.9559 |
| cagr | -0.7625 |
| net_avg_win | 26.6067 |
| net_avg_loss | -44.8112 |
| avg_hold_time_bars | 5.2168 |
| exposure | 0.2063 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
