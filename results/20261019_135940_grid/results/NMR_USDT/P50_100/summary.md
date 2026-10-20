# EMA Hourly Continuation — NMR/USDT P50_100

**Symbol:** NMR/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 660 |
| net_profit_factor | 0.5435 |
| net_win_rate | 0.4682 |
| gross_profit_factor | 0.9425 |
| gross_win_rate | 0.4864 |
| sharpe_ratio | -5.3516 |
| sortino_ratio | -1.9320 |
| max_drawdown | 0.9113 |
| cagr | -0.6133 |
| net_avg_win | 34.9845 |
| net_avg_loss | -56.6675 |
| avg_hold_time_bars | 5.9970 |
| exposure | 0.1799 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
