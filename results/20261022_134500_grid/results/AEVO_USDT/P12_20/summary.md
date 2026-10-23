# EMA Hourly Continuation — AEVO/USDT P12_20

**Symbol:** AEVO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1446 |
| net_profit_factor | 0.3995 |
| net_win_rate | 0.4219 |
| gross_profit_factor | 0.8502 |
| gross_win_rate | 0.4454 |
| sharpe_ratio | -11.6299 |
| sortino_ratio | -6.2406 |
| max_drawdown | 0.9997 |
| cagr | -0.9572 |
| net_avg_win | 10.9022 |
| net_avg_loss | -19.9124 |
| avg_hold_time_bars | 2.6542 |
| exposure | 0.1737 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
