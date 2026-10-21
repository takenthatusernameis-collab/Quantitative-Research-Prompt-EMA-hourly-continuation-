# EMA Hourly Continuation — AURORA/USDT P20_100

**Symbol:** AURORA/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.7574 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 0.9748 |
| gross_win_rate | 0.4920 |
| sharpe_ratio | -1.7347 |
| sortino_ratio | -0.4795 |
| max_drawdown | 0.4639 |
| cagr | -0.1974 |
| net_avg_win | 71.9982 |
| net_avg_loss | -92.0617 |
| avg_hold_time_bars | 24.6123 |
| exposure | 0.4184 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
