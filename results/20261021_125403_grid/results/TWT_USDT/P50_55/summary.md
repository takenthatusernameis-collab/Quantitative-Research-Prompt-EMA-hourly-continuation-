# EMA Hourly Continuation — TWT/USDT P50_55

**Symbol:** TWT/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 138 |
| net_profit_factor | 0.6919 |
| net_win_rate | 0.5362 |
| gross_profit_factor | 1.1255 |
| gross_win_rate | 0.5362 |
| sharpe_ratio | -1.2264 |
| sortino_ratio | -0.2088 |
| max_drawdown | 0.2504 |
| cagr | -0.0907 |
| net_avg_win | 64.4609 |
| net_avg_loss | -107.7143 |
| avg_hold_time_bars | 4.7536 |
| exposure | 0.0298 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
