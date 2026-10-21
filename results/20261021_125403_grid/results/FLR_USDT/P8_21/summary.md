# EMA Hourly Continuation — FLR/USDT P8_21

**Symbol:** FLR/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 550 |
| net_profit_factor | 0.5480 |
| net_win_rate | 0.4455 |
| gross_profit_factor | 0.7809 |
| gross_win_rate | 0.4455 |
| sharpe_ratio | -4.4809 |
| sortino_ratio | -1.5018 |
| max_drawdown | 0.8294 |
| cagr | -0.4993 |
| net_avg_win | 40.7695 |
| net_avg_loss | -59.7648 |
| avg_hold_time_bars | 5.3291 |
| exposure | 0.1332 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
