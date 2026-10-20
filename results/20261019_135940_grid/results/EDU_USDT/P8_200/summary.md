# EMA Hourly Continuation — EDU/USDT P8_200

**Symbol:** EDU/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.6308 |
| net_win_rate | 0.4436 |
| gross_profit_factor | 0.8359 |
| gross_win_rate | 0.4495 |
| sharpe_ratio | -3.4483 |
| sortino_ratio | -1.0864 |
| max_drawdown | 0.7406 |
| cagr | -0.4023 |
| net_avg_win | 55.4625 |
| net_avg_loss | -70.0860 |
| avg_hold_time_bars | 33.2079 |
| exposure | 0.7589 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
