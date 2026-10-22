# EMA Hourly Continuation — OSMO/USDT P8_21

**Symbol:** OSMO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 712 |
| net_profit_factor | 0.7437 |
| net_win_rate | 0.4916 |
| gross_profit_factor | 1.1051 |
| gross_win_rate | 0.4916 |
| sharpe_ratio | -3.5744 |
| sortino_ratio | -1.3699 |
| max_drawdown | 0.8367 |
| cagr | -0.4655 |
| net_avg_win | 65.7094 |
| net_avg_loss | -85.4270 |
| avg_hold_time_bars | 5.8399 |
| exposure | 0.1890 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
