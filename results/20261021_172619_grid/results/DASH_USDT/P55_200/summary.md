# EMA Hourly Continuation — DASH/USDT P55_200

**Symbol:** DASH/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 309 |
| net_profit_factor | 0.6299 |
| net_win_rate | 0.4498 |
| gross_profit_factor | 0.8006 |
| gross_win_rate | 0.4498 |
| sharpe_ratio | -2.3773 |
| sortino_ratio | -0.5930 |
| max_drawdown | 0.5296 |
| cagr | -0.2387 |
| net_avg_win | 60.7221 |
| net_avg_loss | -78.8203 |
| avg_hold_time_bars | 22.8738 |
| exposure | 0.3213 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
