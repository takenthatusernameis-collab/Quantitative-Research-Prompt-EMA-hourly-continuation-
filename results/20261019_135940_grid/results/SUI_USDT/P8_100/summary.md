# EMA Hourly Continuation — SUI/USDT P8_100

**Symbol:** SUI/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 678 |
| net_profit_factor | 0.6430 |
| net_win_rate | 0.4749 |
| gross_profit_factor | 0.9479 |
| gross_win_rate | 0.4838 |
| sharpe_ratio | -4.0753 |
| sortino_ratio | -1.4764 |
| max_drawdown | 0.8504 |
| cagr | -0.5176 |
| net_avg_win | 46.9656 |
| net_avg_loss | -66.0680 |
| avg_hold_time_bars | 20.6239 |
| exposure | 0.6356 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
