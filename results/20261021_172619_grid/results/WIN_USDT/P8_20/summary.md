# EMA Hourly Continuation — WIN/USDT P8_20

**Symbol:** WIN/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 502 |
| net_profit_factor | 0.7302 |
| net_win_rate | 0.5339 |
| gross_profit_factor | 1.1969 |
| gross_win_rate | 0.5339 |
| sharpe_ratio | -2.4525 |
| sortino_ratio | -0.7972 |
| max_drawdown | 0.6199 |
| cagr | -0.3028 |
| net_avg_win | 60.1699 |
| net_avg_loss | -94.3703 |
| avg_hold_time_bars | 6.2550 |
| exposure | 0.1427 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
