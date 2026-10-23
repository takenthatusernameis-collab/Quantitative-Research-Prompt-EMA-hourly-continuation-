# EMA Hourly Continuation — DEEP/USDT P21_144

**Symbol:** DEEP/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.7215 |
| net_win_rate | 0.4820 |
| gross_profit_factor | 0.9317 |
| gross_win_rate | 0.4880 |
| sharpe_ratio | -2.0044 |
| sortino_ratio | -0.5764 |
| max_drawdown | 0.4249 |
| cagr | -0.2387 |
| net_avg_win | 68.0475 |
| net_avg_loss | -87.7768 |
| avg_hold_time_bars | 30.7784 |
| exposure | 0.5820 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
