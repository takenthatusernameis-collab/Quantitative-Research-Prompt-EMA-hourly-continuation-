# EMA Hourly Continuation — LUNC/USDT P12_21

**Symbol:** LUNC/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1575 |
| net_profit_factor | 0.2488 |
| net_win_rate | 0.3708 |
| gross_profit_factor | 0.7523 |
| gross_win_rate | 0.4013 |
| sharpe_ratio | -16.0746 |
| sortino_ratio | -9.2347 |
| max_drawdown | 1.0000 |
| cagr | -0.9921 |
| net_avg_win | 5.6717 |
| net_avg_loss | -13.4331 |
| avg_hold_time_bars | 2.0413 |
| exposure | 0.1461 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
