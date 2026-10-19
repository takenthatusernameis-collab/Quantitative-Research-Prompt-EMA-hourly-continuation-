# EMA Hourly Continuation — OP/USDT P55_200

**Symbol:** OP/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.6381 |
| net_win_rate | 0.4726 |
| gross_profit_factor | 0.9251 |
| gross_win_rate | 0.4804 |
| sharpe_ratio | -2.7179 |
| sortino_ratio | -0.7446 |
| max_drawdown | 0.5988 |
| cagr | -0.3004 |
| net_avg_win | 57.6883 |
| net_avg_loss | -81.0095 |
| avg_hold_time_bars | 21.7885 |
| exposure | 0.3793 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
