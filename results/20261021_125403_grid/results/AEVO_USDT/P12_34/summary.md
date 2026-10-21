# EMA Hourly Continuation — AEVO/USDT P12_34

**Symbol:** AEVO/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 693 |
| net_profit_factor | 0.7158 |
| net_win_rate | 0.4791 |
| gross_profit_factor | 0.9351 |
| gross_win_rate | 0.4791 |
| sharpe_ratio | -3.0827 |
| sortino_ratio | -1.1566 |
| max_drawdown | 0.7626 |
| cagr | -0.4111 |
| net_avg_win | 55.9144 |
| net_avg_loss | -71.8406 |
| avg_hold_time_bars | 6.8499 |
| exposure | 0.2148 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
