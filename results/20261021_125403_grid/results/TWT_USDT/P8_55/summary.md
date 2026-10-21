# EMA Hourly Continuation — TWT/USDT P8_55

**Symbol:** TWT/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 751 |
| net_profit_factor | 0.7302 |
| net_win_rate | 0.5126 |
| gross_profit_factor | 0.9997 |
| gross_win_rate | 0.5140 |
| sharpe_ratio | -2.1951 |
| sortino_ratio | -0.8648 |
| max_drawdown | 0.6497 |
| cagr | -0.3270 |
| net_avg_win | 44.3028 |
| net_avg_loss | -63.8202 |
| avg_hold_time_bars | 13.9321 |
| exposure | 0.4756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
