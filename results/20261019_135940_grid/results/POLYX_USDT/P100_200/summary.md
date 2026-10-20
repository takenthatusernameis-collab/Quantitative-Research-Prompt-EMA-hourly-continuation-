# EMA Hourly Continuation — POLYX/USDT P100_200

**Symbol:** POLYX/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 411 |
| net_profit_factor | 0.5907 |
| net_win_rate | 0.4818 |
| gross_profit_factor | 0.9759 |
| gross_win_rate | 0.4964 |
| sharpe_ratio | -3.2751 |
| sortino_ratio | -0.9373 |
| max_drawdown | 0.6768 |
| cagr | -0.3599 |
| net_avg_win | 49.1180 |
| net_avg_loss | -77.2969 |
| avg_hold_time_bars | 9.2628 |
| exposure | 0.1730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
