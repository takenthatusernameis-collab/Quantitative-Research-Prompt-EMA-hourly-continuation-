# EMA Hourly Continuation — SWFTC/USDT P21_55

**Symbol:** SWFTC/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 435 |
| net_profit_factor | 0.7248 |
| net_win_rate | 0.4874 |
| gross_profit_factor | 0.9455 |
| gross_win_rate | 0.4874 |
| sharpe_ratio | -2.0650 |
| sortino_ratio | -0.6160 |
| max_drawdown | 0.5272 |
| cagr | -0.2459 |
| net_avg_win | 63.0773 |
| net_avg_loss | -82.7320 |
| avg_hold_time_bars | 8.9379 |
| exposure | 0.1767 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
