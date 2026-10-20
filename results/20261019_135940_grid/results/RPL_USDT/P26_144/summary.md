# EMA Hourly Continuation — RPL/USDT P26_144

**Symbol:** RPL/USDT  |  **P_fast:** 26  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.7325 |
| net_win_rate | 0.4979 |
| gross_profit_factor | 0.9978 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.0073 |
| sortino_ratio | -0.6109 |
| max_drawdown | 0.5339 |
| cagr | -0.2519 |
| net_avg_win | 60.9867 |
| net_avg_loss | -82.5542 |
| avg_hold_time_bars | 23.8205 |
| exposure | 0.5045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
