# EMA Hourly Continuation — TWT/USDT P34_144

**Symbol:** TWT/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 400 |
| net_profit_factor | 0.7313 |
| net_win_rate | 0.4950 |
| gross_profit_factor | 0.9684 |
| gross_win_rate | 0.4950 |
| sharpe_ratio | -1.8729 |
| sortino_ratio | -0.5360 |
| max_drawdown | 0.5068 |
| cagr | -0.2184 |
| net_avg_win | 63.4500 |
| net_avg_loss | -85.0400 |
| avg_hold_time_bars | 20.5875 |
| exposure | 0.3743 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
