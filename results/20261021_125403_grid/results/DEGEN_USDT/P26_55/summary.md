# EMA Hourly Continuation — DEGEN/USDT P26_55

**Symbol:** DEGEN/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.7910 |
| net_win_rate | 0.4966 |
| gross_profit_factor | 0.9933 |
| gross_win_rate | 0.4966 |
| sharpe_ratio | -1.6509 |
| sortino_ratio | -0.4942 |
| max_drawdown | 0.4454 |
| cagr | -0.2040 |
| net_avg_win | 75.9643 |
| net_avg_loss | -94.7308 |
| avg_hold_time_bars | 6.9634 |
| exposure | 0.1385 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
