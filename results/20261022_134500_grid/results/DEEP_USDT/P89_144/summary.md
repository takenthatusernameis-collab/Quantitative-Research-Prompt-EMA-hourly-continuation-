# EMA Hourly Continuation — DEEP/USDT P89_144

**Symbol:** DEEP/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.6449 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 0.9769 |
| gross_win_rate | 0.5030 |
| sharpe_ratio | -2.6901 |
| sortino_ratio | -0.7765 |
| max_drawdown | 0.5400 |
| cagr | -0.3106 |
| net_avg_win | 57.0285 |
| net_avg_loss | -87.3900 |
| avg_hold_time_bars | 5.4822 |
| exposure | 0.1049 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
