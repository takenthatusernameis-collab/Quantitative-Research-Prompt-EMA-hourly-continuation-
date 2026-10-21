# EMA Hourly Continuation — CARV/USDT P34_100

**Symbol:** CARV/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.6172 |
| net_win_rate | 0.4479 |
| gross_profit_factor | 0.7966 |
| gross_win_rate | 0.4479 |
| sharpe_ratio | -2.9364 |
| sortino_ratio | -0.8381 |
| max_drawdown | 0.5751 |
| cagr | -0.3200 |
| net_avg_win | 59.9350 |
| net_avg_loss | -78.7628 |
| avg_hold_time_bars | 12.6074 |
| exposure | 0.2313 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
