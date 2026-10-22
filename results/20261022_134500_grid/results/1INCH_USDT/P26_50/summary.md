# EMA Hourly Continuation — 1INCH/USDT P26_50

**Symbol:** 1INCH/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1031 |
| net_profit_factor | 0.4469 |
| net_win_rate | 0.4306 |
| gross_profit_factor | 0.8801 |
| gross_win_rate | 0.4636 |
| sharpe_ratio | -8.7901 |
| sortino_ratio | -4.0198 |
| max_drawdown | 0.9929 |
| cagr | -0.8601 |
| net_avg_win | 18.0662 |
| net_avg_loss | -30.5788 |
| avg_hold_time_bars | 3.6731 |
| exposure | 0.1721 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
