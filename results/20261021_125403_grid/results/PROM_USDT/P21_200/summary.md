# EMA Hourly Continuation — PROM/USDT P21_200

**Symbol:** PROM/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 368 |
| net_profit_factor | 0.5095 |
| net_win_rate | 0.3967 |
| gross_profit_factor | 0.6626 |
| gross_win_rate | 0.4022 |
| sharpe_ratio | -3.9814 |
| sortino_ratio | -1.0745 |
| max_drawdown | 0.7392 |
| cagr | -0.3945 |
| net_avg_win | 50.9651 |
| net_avg_loss | -65.7848 |
| avg_hold_time_bars | 33.5326 |
| exposure | 0.5609 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
