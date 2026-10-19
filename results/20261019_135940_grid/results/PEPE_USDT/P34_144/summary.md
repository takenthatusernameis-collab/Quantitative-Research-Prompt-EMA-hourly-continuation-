# EMA Hourly Continuation — PEPE/USDT P34_144

**Symbol:** PEPE/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 483 |
| net_profit_factor | 0.6179 |
| net_win_rate | 0.4700 |
| gross_profit_factor | 0.8948 |
| gross_win_rate | 0.4741 |
| sharpe_ratio | -3.3973 |
| sortino_ratio | -1.0568 |
| max_drawdown | 0.7164 |
| cagr | -0.3923 |
| net_avg_win | 50.8391 |
| net_avg_loss | -72.9597 |
| avg_hold_time_bars | 17.3499 |
| exposure | 0.3809 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
