# EMA Hourly Continuation — ZBCN/USDT P21_200

**Symbol:** ZBCN/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 552 |
| net_profit_factor | 0.7450 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0148 |
| gross_win_rate | 0.5036 |
| sharpe_ratio | -2.2874 |
| sortino_ratio | -0.7565 |
| max_drawdown | 0.6271 |
| cagr | -0.3088 |
| net_avg_win | 63.2874 |
| net_avg_loss | -84.9509 |
| avg_hold_time_bars | 20.9185 |
| exposure | 0.5342 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
