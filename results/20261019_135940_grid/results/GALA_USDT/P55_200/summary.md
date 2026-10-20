# EMA Hourly Continuation — GALA/USDT P55_200

**Symbol:** GALA/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.5912 |
| net_win_rate | 0.4548 |
| gross_profit_factor | 0.8604 |
| gross_win_rate | 0.4636 |
| sharpe_ratio | -2.8821 |
| sortino_ratio | -0.7461 |
| max_drawdown | 0.6136 |
| cagr | -0.3029 |
| net_avg_win | 55.2337 |
| net_avg_loss | -77.9415 |
| avg_hold_time_bars | 26.3673 |
| exposure | 0.4111 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
