# EMA Hourly Continuation — SAND/USDT P12_100

**Symbol:** SAND/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.6906 |
| net_win_rate | 0.4593 |
| gross_profit_factor | 0.8637 |
| gross_win_rate | 0.4593 |
| sharpe_ratio | -2.5746 |
| sortino_ratio | -0.7687 |
| max_drawdown | 0.5982 |
| cagr | -0.2983 |
| net_avg_win | 64.7840 |
| net_avg_loss | -79.6763 |
| avg_hold_time_bars | 27.9525 |
| exposure | 0.5616 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
