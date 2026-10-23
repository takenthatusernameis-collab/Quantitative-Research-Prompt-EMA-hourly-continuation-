# EMA Hourly Continuation — DOGS/USDT P21_55

**Symbol:** DOGS/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 875 |
| net_profit_factor | 0.4627 |
| net_win_rate | 0.4389 |
| gross_profit_factor | 0.7324 |
| gross_win_rate | 0.4503 |
| sharpe_ratio | -7.2837 |
| sortino_ratio | -3.2709 |
| max_drawdown | 0.9674 |
| cagr | -0.7963 |
| net_avg_win | 21.6955 |
| net_avg_loss | -36.6704 |
| avg_hold_time_bars | 4.6754 |
| exposure | 0.2170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
