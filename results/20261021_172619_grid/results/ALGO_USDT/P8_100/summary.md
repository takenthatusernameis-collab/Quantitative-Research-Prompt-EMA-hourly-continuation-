# EMA Hourly Continuation — ALGO/USDT P8_100

**Symbol:** ALGO/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 398 |
| net_profit_factor | 0.9479 |
| net_win_rate | 0.5352 |
| gross_profit_factor | 1.1330 |
| gross_win_rate | 0.5352 |
| sharpe_ratio | -0.2543 |
| sortino_ratio | -0.0732 |
| max_drawdown | 0.1860 |
| cagr | -0.0390 |
| net_avg_win | 81.2822 |
| net_avg_loss | -98.7272 |
| avg_hold_time_bars | 39.0955 |
| exposure | 0.7073 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
