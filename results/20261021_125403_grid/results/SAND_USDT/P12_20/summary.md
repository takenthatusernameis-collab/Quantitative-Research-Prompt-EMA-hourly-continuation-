# EMA Hourly Continuation — SAND/USDT P12_20

**Symbol:** SAND/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 289 |
| net_profit_factor | 0.6327 |
| net_win_rate | 0.4810 |
| gross_profit_factor | 0.9292 |
| gross_win_rate | 0.4810 |
| sharpe_ratio | -2.4340 |
| sortino_ratio | -0.5939 |
| max_drawdown | 0.5033 |
| cagr | -0.2379 |
| net_avg_win | 61.2920 |
| net_avg_loss | -89.7676 |
| avg_hold_time_bars | 4.4256 |
| exposure | 0.0581 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
