# EMA Hourly Continuation — METIS/USDT P8_26

**Symbol:** METIS/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 736 |
| net_profit_factor | 0.7474 |
| net_win_rate | 0.4932 |
| gross_profit_factor | 0.9972 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -2.7881 |
| sortino_ratio | -1.0824 |
| max_drawdown | 0.7151 |
| cagr | -0.3920 |
| net_avg_win | 58.1401 |
| net_avg_loss | -75.7068 |
| avg_hold_time_bars | 6.7351 |
| exposure | 0.2253 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
