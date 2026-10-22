# EMA Hourly Continuation — IOTA/USDT P34_89

**Symbol:** IOTA/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 705 |
| net_profit_factor | 0.5188 |
| net_win_rate | 0.4482 |
| gross_profit_factor | 0.8728 |
| gross_win_rate | 0.4567 |
| sharpe_ratio | -5.6453 |
| sortino_ratio | -2.1008 |
| max_drawdown | 0.9292 |
| cagr | -0.6413 |
| net_avg_win | 31.5170 |
| net_avg_loss | -49.3515 |
| avg_hold_time_bars | 7.0624 |
| exposure | 0.2263 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
