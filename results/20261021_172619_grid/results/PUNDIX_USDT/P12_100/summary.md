# EMA Hourly Continuation — PUNDIX/USDT P12_100

**Symbol:** PUNDIX/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 532 |
| net_profit_factor | 0.7253 |
| net_win_rate | 0.4793 |
| gross_profit_factor | 0.9471 |
| gross_win_rate | 0.4793 |
| sharpe_ratio | -2.5829 |
| sortino_ratio | -0.8494 |
| max_drawdown | 0.6411 |
| cagr | -0.3237 |
| net_avg_win | 64.7639 |
| net_avg_loss | -82.2005 |
| avg_hold_time_bars | 23.5038 |
| exposure | 0.5684 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
