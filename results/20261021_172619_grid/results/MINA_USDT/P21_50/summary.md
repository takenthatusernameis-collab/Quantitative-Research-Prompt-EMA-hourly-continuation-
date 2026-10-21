# EMA Hourly Continuation — MINA/USDT P21_50

**Symbol:** MINA/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 539 |
| net_profit_factor | 0.7424 |
| net_win_rate | 0.5046 |
| gross_profit_factor | 1.0210 |
| gross_win_rate | 0.5046 |
| sharpe_ratio | -2.2202 |
| sortino_ratio | -0.7405 |
| max_drawdown | 0.5973 |
| cagr | -0.2874 |
| net_avg_win | 60.7204 |
| net_avg_loss | -83.3161 |
| avg_hold_time_bars | 8.1967 |
| exposure | 0.2008 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
