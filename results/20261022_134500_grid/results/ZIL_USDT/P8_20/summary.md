# EMA Hourly Continuation — ZIL/USDT P8_20

**Symbol:** ZIL/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1691 |
| net_profit_factor | 0.3028 |
| net_win_rate | 0.4234 |
| gross_profit_factor | 0.8530 |
| gross_win_rate | 0.4571 |
| sharpe_ratio | -13.0555 |
| sortino_ratio | -7.6471 |
| max_drawdown | 0.9999 |
| cagr | -0.9790 |
| net_avg_win | 6.0644 |
| net_avg_loss | -14.7092 |
| avg_hold_time_bars | 2.8468 |
| exposure | 0.2188 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
