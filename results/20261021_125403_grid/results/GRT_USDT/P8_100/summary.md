# EMA Hourly Continuation — GRT/USDT P8_100

**Symbol:** GRT/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 475 |
| net_profit_factor | 0.9097 |
| net_win_rate | 0.5284 |
| gross_profit_factor | 1.1100 |
| gross_win_rate | 0.5284 |
| sharpe_ratio | -0.6319 |
| sortino_ratio | -0.1980 |
| max_drawdown | 0.3298 |
| cagr | -0.0917 |
| net_avg_win | 86.5218 |
| net_avg_loss | -106.5725 |
| avg_hold_time_bars | 30.4253 |
| exposure | 0.6540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
