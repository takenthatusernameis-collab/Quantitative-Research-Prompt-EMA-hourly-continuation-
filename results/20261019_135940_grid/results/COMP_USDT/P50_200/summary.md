# EMA Hourly Continuation — COMP/USDT P50_200

**Symbol:** COMP/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 427 |
| net_profit_factor | 0.5183 |
| net_win_rate | 0.4614 |
| gross_profit_factor | 0.8653 |
| gross_win_rate | 0.4754 |
| sharpe_ratio | -3.7366 |
| sortino_ratio | -1.0757 |
| max_drawdown | 0.7496 |
| cagr | -0.4123 |
| net_avg_win | 40.2393 |
| net_avg_loss | -66.4989 |
| avg_hold_time_bars | 20.2459 |
| exposure | 0.3930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
