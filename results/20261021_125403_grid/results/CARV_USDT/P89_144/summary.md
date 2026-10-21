# EMA Hourly Continuation — CARV/USDT P89_144

**Symbol:** CARV/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 230 |
| net_profit_factor | 0.6168 |
| net_win_rate | 0.4609 |
| gross_profit_factor | 0.8524 |
| gross_win_rate | 0.4609 |
| sharpe_ratio | -2.4928 |
| sortino_ratio | -0.6001 |
| max_drawdown | 0.4441 |
| cagr | -0.2396 |
| net_avg_win | 64.7269 |
| net_avg_loss | -89.7025 |
| avg_hold_time_bars | 8.1565 |
| exposure | 0.1056 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
