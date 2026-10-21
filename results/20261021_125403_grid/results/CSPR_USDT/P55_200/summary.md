# EMA Hourly Continuation — CSPR/USDT P55_200

**Symbol:** CSPR/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 389 |
| net_profit_factor | 0.6429 |
| net_win_rate | 0.4370 |
| gross_profit_factor | 0.7951 |
| gross_win_rate | 0.4370 |
| sharpe_ratio | -2.8779 |
| sortino_ratio | -0.8024 |
| max_drawdown | 0.6135 |
| cagr | -0.3096 |
| net_avg_win | 64.1284 |
| net_avg_loss | -77.4360 |
| avg_hold_time_bars | 18.9075 |
| exposure | 0.3343 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
