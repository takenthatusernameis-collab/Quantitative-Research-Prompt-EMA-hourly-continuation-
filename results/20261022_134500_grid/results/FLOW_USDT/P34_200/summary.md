# EMA Hourly Continuation — FLOW/USDT P34_200

**Symbol:** FLOW/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 387 |
| net_profit_factor | 0.6258 |
| net_win_rate | 0.4625 |
| gross_profit_factor | 0.8754 |
| gross_win_rate | 0.4677 |
| sharpe_ratio | -2.9143 |
| sortino_ratio | -0.8004 |
| max_drawdown | 0.6257 |
| cagr | -0.3215 |
| net_avg_win | 58.1597 |
| net_avg_loss | -79.9750 |
| avg_hold_time_bars | 29.3488 |
| exposure | 0.5163 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
