# EMA Hourly Continuation — FLOW/USDT P20_200

**Symbol:** FLOW/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 343 |
| net_profit_factor | 0.6382 |
| net_win_rate | 0.4694 |
| gross_profit_factor | 0.9111 |
| gross_win_rate | 0.4723 |
| sharpe_ratio | -2.7203 |
| sortino_ratio | -0.7004 |
| max_drawdown | 0.5871 |
| cagr | -0.2893 |
| net_avg_win | 63.0893 |
| net_avg_loss | -87.4477 |
| avg_hold_time_bars | 42.4752 |
| exposure | 0.6622 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
