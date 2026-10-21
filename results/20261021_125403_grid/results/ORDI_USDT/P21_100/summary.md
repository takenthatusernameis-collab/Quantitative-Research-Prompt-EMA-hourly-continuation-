# EMA Hourly Continuation — ORDI/USDT P21_100

**Symbol:** ORDI/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 479 |
| net_profit_factor | 0.7096 |
| net_win_rate | 0.4614 |
| gross_profit_factor | 0.8629 |
| gross_win_rate | 0.4614 |
| sharpe_ratio | -2.4441 |
| sortino_ratio | -0.7600 |
| max_drawdown | 0.6000 |
| cagr | -0.2946 |
| net_avg_win | 64.5430 |
| net_avg_loss | -77.9133 |
| avg_hold_time_bars | 16.0480 |
| exposure | 0.3494 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
