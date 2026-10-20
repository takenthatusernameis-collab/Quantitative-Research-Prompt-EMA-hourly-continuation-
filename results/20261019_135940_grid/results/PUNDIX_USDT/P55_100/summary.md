# EMA Hourly Continuation — PUNDIX/USDT P55_100

**Symbol:** PUNDIX/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 592 |
| net_profit_factor | 0.3735 |
| net_win_rate | 0.4291 |
| gross_profit_factor | 0.7055 |
| gross_win_rate | 0.4561 |
| sharpe_ratio | -6.2577 |
| sortino_ratio | -2.1533 |
| max_drawdown | 0.9297 |
| cagr | -0.6512 |
| net_avg_win | 21.8082 |
| net_avg_loss | -43.8732 |
| avg_hold_time_bars | 6.9544 |
| exposure | 0.1871 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
