# EMA Hourly Continuation — CETUS/USDT P8_50

**Symbol:** CETUS/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1088 |
| net_profit_factor | 0.6879 |
| net_win_rate | 0.4752 |
| gross_profit_factor | 1.0260 |
| gross_win_rate | 0.4871 |
| sharpe_ratio | -5.1305 |
| sortino_ratio | -2.3719 |
| max_drawdown | 0.9479 |
| cagr | -0.6803 |
| net_avg_win | 40.2398 |
| net_avg_loss | -52.9610 |
| avg_hold_time_bars | 9.4210 |
| exposure | 0.4638 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
