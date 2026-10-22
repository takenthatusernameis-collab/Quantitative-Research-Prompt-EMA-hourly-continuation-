# EMA Hourly Continuation — FLIP/USDT P34_200

**Symbol:** FLIP/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 261 |
| net_profit_factor | 0.6645 |
| net_win_rate | 0.4598 |
| gross_profit_factor | 0.8471 |
| gross_win_rate | 0.4598 |
| sharpe_ratio | -2.0603 |
| sortino_ratio | -0.4713 |
| max_drawdown | 0.4766 |
| cagr | -0.1962 |
| net_avg_win | 69.6734 |
| net_avg_loss | -89.2387 |
| avg_hold_time_bars | 39.5556 |
| exposure | 0.4693 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
