# EMA Hourly Continuation — POLYX/USDT P21_34

**Symbol:** POLYX/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1048 |
| net_profit_factor | 0.3931 |
| net_win_rate | 0.4246 |
| gross_profit_factor | 0.8379 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -9.8344 |
| sortino_ratio | -4.5386 |
| max_drawdown | 0.9967 |
| cagr | -0.8964 |
| net_avg_win | 14.5062 |
| net_avg_loss | -27.2332 |
| avg_hold_time_bars | 3.2319 |
| exposure | 0.1540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
