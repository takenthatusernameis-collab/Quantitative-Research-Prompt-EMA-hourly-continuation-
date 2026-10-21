# EMA Hourly Continuation — MEW/USDT P50_100

**Symbol:** MEW/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.6392 |
| net_win_rate | 0.4569 |
| gross_profit_factor | 0.8025 |
| gross_win_rate | 0.4569 |
| sharpe_ratio | -2.5161 |
| sortino_ratio | -0.7000 |
| max_drawdown | 0.5632 |
| cagr | -0.2742 |
| net_avg_win | 55.9627 |
| net_avg_loss | -73.6596 |
| avg_hold_time_bars | 9.0836 |
| exposure | 0.1581 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
