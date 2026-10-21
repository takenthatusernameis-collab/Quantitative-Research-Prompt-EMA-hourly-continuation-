# EMA Hourly Continuation — AGLD/USDT P21_200

**Symbol:** AGLD/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.7349 |
| net_win_rate | 0.4611 |
| gross_profit_factor | 0.8791 |
| gross_win_rate | 0.4611 |
| sharpe_ratio | -2.0623 |
| sortino_ratio | -0.5637 |
| max_drawdown | 0.5550 |
| cagr | -0.2287 |
| net_avg_win | 77.4574 |
| net_avg_loss | -90.1907 |
| avg_hold_time_bars | 34.8713 |
| exposure | 0.5886 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
