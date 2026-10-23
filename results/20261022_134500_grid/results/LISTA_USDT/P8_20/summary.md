# EMA Hourly Continuation — LISTA/USDT P8_20

**Symbol:** LISTA/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1333 |
| net_profit_factor | 0.6113 |
| net_win_rate | 0.4419 |
| gross_profit_factor | 1.0608 |
| gross_win_rate | 0.4651 |
| sharpe_ratio | -8.8674 |
| sortino_ratio | -4.7205 |
| max_drawdown | 0.9957 |
| cagr | -0.9013 |
| net_avg_win | 26.5754 |
| net_avg_loss | -34.4194 |
| avg_hold_time_bars | 3.9160 |
| exposure | 0.2552 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
