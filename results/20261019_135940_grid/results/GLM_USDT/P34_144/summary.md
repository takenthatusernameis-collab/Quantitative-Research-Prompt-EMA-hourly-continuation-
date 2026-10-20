# EMA Hourly Continuation — GLM/USDT P34_144

**Symbol:** GLM/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 526 |
| net_profit_factor | 0.5939 |
| net_win_rate | 0.4715 |
| gross_profit_factor | 0.9271 |
| gross_win_rate | 0.4867 |
| sharpe_ratio | -3.6665 |
| sortino_ratio | -1.1836 |
| max_drawdown | 0.7634 |
| cagr | -0.4320 |
| net_avg_win | 44.7184 |
| net_avg_loss | -67.1715 |
| avg_hold_time_bars | 15.2395 |
| exposure | 0.3644 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
