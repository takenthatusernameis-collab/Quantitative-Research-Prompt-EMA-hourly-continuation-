# EMA Hourly Continuation — OSMO/USDT P21_55

**Symbol:** OSMO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.6634 |
| net_win_rate | 0.4620 |
| gross_profit_factor | 0.9181 |
| gross_win_rate | 0.4620 |
| sharpe_ratio | -3.4133 |
| sortino_ratio | -1.1166 |
| max_drawdown | 0.7379 |
| cagr | -0.4020 |
| net_avg_win | 58.8046 |
| net_avg_loss | -76.1152 |
| avg_hold_time_bars | 9.2662 |
| exposure | 0.2215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
