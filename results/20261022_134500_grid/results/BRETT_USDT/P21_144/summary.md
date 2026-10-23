# EMA Hourly Continuation — BRETT/USDT P21_144

**Symbol:** BRETT/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.6810 |
| net_win_rate | 0.4530 |
| gross_profit_factor | 0.8433 |
| gross_win_rate | 0.4530 |
| sharpe_ratio | -2.6460 |
| sortino_ratio | -0.7717 |
| max_drawdown | 0.5834 |
| cagr | -0.3033 |
| net_avg_win | 67.1663 |
| net_avg_loss | -81.6674 |
| avg_hold_time_bars | 29.2723 |
| exposure | 0.5690 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
