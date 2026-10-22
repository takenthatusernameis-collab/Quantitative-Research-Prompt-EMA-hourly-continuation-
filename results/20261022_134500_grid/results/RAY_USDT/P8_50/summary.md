# EMA Hourly Continuation — RAY/USDT P8_50

**Symbol:** RAY/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1117 |
| net_profit_factor | 0.6712 |
| net_win_rate | 0.4718 |
| gross_profit_factor | 1.0004 |
| gross_win_rate | 0.4790 |
| sharpe_ratio | -5.4665 |
| sortino_ratio | -2.5695 |
| max_drawdown | 0.9565 |
| cagr | -0.7089 |
| net_avg_win | 36.9928 |
| net_avg_loss | -49.2280 |
| avg_hold_time_bars | 8.7726 |
| exposure | 0.4454 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
