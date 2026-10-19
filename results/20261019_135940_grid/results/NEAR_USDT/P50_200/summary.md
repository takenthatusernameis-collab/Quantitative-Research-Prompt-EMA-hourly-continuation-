# EMA Hourly Continuation — NEAR/USDT P50_200

**Symbol:** NEAR/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 0.7435 |
| net_win_rate | 0.5081 |
| gross_profit_factor | 1.0187 |
| gross_win_rate | 0.5081 |
| sharpe_ratio | -1.7304 |
| sortino_ratio | -0.4726 |
| max_drawdown | 0.4734 |
| cagr | -0.1997 |
| net_avg_win | 66.0592 |
| net_avg_loss | -91.7834 |
| avg_hold_time_bars | 22.5081 |
| exposure | 0.3785 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
