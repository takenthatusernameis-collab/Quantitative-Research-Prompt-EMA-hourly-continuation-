# EMA Hourly Continuation — ATH/USDT P34_100

**Symbol:** ATH/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 642 |
| net_profit_factor | 0.6368 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 0.9559 |
| gross_win_rate | 0.5016 |
| sharpe_ratio | -3.3971 |
| sortino_ratio | -1.2558 |
| max_drawdown | 0.7631 |
| cagr | -0.4491 |
| net_avg_win | 41.3291 |
| net_avg_loss | -64.5019 |
| avg_hold_time_bars | 8.2383 |
| exposure | 0.2564 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
