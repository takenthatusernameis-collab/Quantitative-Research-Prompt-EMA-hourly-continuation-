# EMA Hourly Continuation — DODO/USDT P34_144

**Symbol:** DODO/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 579 |
| net_profit_factor | 0.6167 |
| net_win_rate | 0.4560 |
| gross_profit_factor | 0.8912 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -3.8681 |
| sortino_ratio | -1.3088 |
| max_drawdown | 0.8025 |
| cagr | -0.4599 |
| net_avg_win | 48.0687 |
| net_avg_loss | -65.3217 |
| avg_hold_time_bars | 14.1952 |
| exposure | 0.3719 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
