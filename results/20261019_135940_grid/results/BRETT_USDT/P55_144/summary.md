# EMA Hourly Continuation — BRETT/USDT P55_144

**Symbol:** BRETT/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 456 |
| net_profit_factor | 0.6800 |
| net_win_rate | 0.4715 |
| gross_profit_factor | 0.9079 |
| gross_win_rate | 0.4737 |
| sharpe_ratio | -2.8024 |
| sortino_ratio | -0.8722 |
| max_drawdown | 0.6432 |
| cagr | -0.3343 |
| net_avg_win | 61.2024 |
| net_avg_loss | -80.2891 |
| avg_hold_time_bars | 12.1360 |
| exposure | 0.2663 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
