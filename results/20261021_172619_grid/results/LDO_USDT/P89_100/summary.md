# EMA Hourly Continuation — LDO/USDT P89_100

**Symbol:** LDO/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 102 |
| net_profit_factor | 0.5218 |
| net_win_rate | 0.4216 |
| gross_profit_factor | 0.7350 |
| gross_win_rate | 0.4216 |
| sharpe_ratio | -2.0385 |
| sortino_ratio | -0.2932 |
| max_drawdown | 0.2931 |
| cagr | -0.1258 |
| net_avg_win | 72.7092 |
| net_avg_loss | -101.5614 |
| avg_hold_time_bars | 4.0098 |
| exposure | 0.0186 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
