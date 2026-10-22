# EMA Hourly Continuation — ADA/USDT P55_100

**Symbol:** ADA/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.4279 |
| net_win_rate | 0.4576 |
| gross_profit_factor | 0.7971 |
| gross_win_rate | 0.4746 |
| sharpe_ratio | -5.4436 |
| sortino_ratio | -1.8646 |
| max_drawdown | 0.9018 |
| cagr | -0.6004 |
| net_avg_win | 24.9316 |
| net_avg_loss | -49.1633 |
| avg_hold_time_bars | 5.3068 |
| exposure | 0.1423 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
