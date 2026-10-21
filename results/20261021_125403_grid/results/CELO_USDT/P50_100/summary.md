# EMA Hourly Continuation — CELO/USDT P50_100

**Symbol:** CELO/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.9386 |
| net_win_rate | 0.5556 |
| gross_profit_factor | 1.2483 |
| gross_win_rate | 0.5556 |
| sharpe_ratio | -0.3332 |
| sortino_ratio | -0.0928 |
| max_drawdown | 0.1931 |
| cagr | -0.0464 |
| net_avg_win | 84.2776 |
| net_avg_loss | -112.2366 |
| avg_hold_time_bars | 9.3360 |
| exposure | 0.1559 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
