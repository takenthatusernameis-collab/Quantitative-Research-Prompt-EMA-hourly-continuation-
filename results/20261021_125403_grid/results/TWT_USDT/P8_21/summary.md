# EMA Hourly Continuation — TWT/USDT P8_21

**Symbol:** TWT/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 647 |
| net_profit_factor | 0.6893 |
| net_win_rate | 0.5209 |
| gross_profit_factor | 1.0853 |
| gross_win_rate | 0.5209 |
| sharpe_ratio | -2.9659 |
| sortino_ratio | -1.0894 |
| max_drawdown | 0.7170 |
| cagr | -0.3908 |
| net_avg_win | 46.8809 |
| net_avg_loss | -73.9312 |
| avg_hold_time_bars | 5.2117 |
| exposure | 0.1533 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
