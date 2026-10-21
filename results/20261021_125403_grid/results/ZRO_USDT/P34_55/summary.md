# EMA Hourly Continuation — ZRO/USDT P34_55

**Symbol:** ZRO/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 305 |
| net_profit_factor | 0.8194 |
| net_win_rate | 0.5148 |
| gross_profit_factor | 1.0521 |
| gross_win_rate | 0.5148 |
| sharpe_ratio | -1.0855 |
| sortino_ratio | -0.2831 |
| max_drawdown | 0.2707 |
| cagr | -0.1228 |
| net_avg_win | 76.0811 |
| net_avg_loss | -98.4915 |
| avg_hold_time_bars | 5.4984 |
| exposure | 0.0821 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
