# EMA Hourly Continuation — PUNDIX/USDT P21_55

**Symbol:** PUNDIX/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 596 |
| net_profit_factor | 0.6671 |
| net_win_rate | 0.4815 |
| gross_profit_factor | 0.9581 |
| gross_win_rate | 0.4832 |
| sharpe_ratio | -3.4101 |
| sortino_ratio | -1.1921 |
| max_drawdown | 0.7609 |
| cagr | -0.4200 |
| net_avg_win | 52.0423 |
| net_avg_loss | -72.4595 |
| avg_hold_time_bars | 8.5940 |
| exposure | 0.2328 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
