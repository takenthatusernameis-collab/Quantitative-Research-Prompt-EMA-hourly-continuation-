# EMA Hourly Continuation — GLM/USDT P12_20

**Symbol:** GLM/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 536 |
| net_profit_factor | 0.5850 |
| net_win_rate | 0.4888 |
| gross_profit_factor | 0.9651 |
| gross_win_rate | 0.4907 |
| sharpe_ratio | -4.0932 |
| sortino_ratio | -1.3660 |
| max_drawdown | 0.7924 |
| cagr | -0.4644 |
| net_avg_win | 42.5809 |
| net_avg_loss | -69.6045 |
| avg_hold_time_bars | 4.7668 |
| exposure | 0.1161 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
