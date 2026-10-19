# EMA Hourly Continuation — ZBCN/USDT P21_100

**Symbol:** ZBCN/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 838 |
| net_profit_factor | 0.6805 |
| net_win_rate | 0.4940 |
| gross_profit_factor | 0.9834 |
| gross_win_rate | 0.4940 |
| sharpe_ratio | -3.5201 |
| sortino_ratio | -1.4443 |
| max_drawdown | 0.8346 |
| cagr | -0.5012 |
| net_avg_win | 42.2029 |
| net_avg_loss | -60.5528 |
| avg_hold_time_bars | 9.0179 |
| exposure | 0.3496 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
