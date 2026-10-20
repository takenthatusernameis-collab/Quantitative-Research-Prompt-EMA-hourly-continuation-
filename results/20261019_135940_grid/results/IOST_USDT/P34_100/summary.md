# EMA Hourly Continuation — IOST/USDT P34_100

**Symbol:** IOST/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 634 |
| net_profit_factor | 0.5446 |
| net_win_rate | 0.4811 |
| gross_profit_factor | 0.9564 |
| gross_win_rate | 0.4984 |
| sharpe_ratio | -4.5990 |
| sortino_ratio | -1.6168 |
| max_drawdown | 0.8794 |
| cagr | -0.5512 |
| net_avg_win | 33.9623 |
| net_avg_loss | -57.8160 |
| avg_hold_time_bars | 9.8864 |
| exposure | 0.2849 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
