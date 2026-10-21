# EMA Hourly Continuation — TWT/USDT P8_50

**Symbol:** TWT/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 757 |
| net_profit_factor | 0.7028 |
| net_win_rate | 0.5073 |
| gross_profit_factor | 0.9643 |
| gross_win_rate | 0.5073 |
| sharpe_ratio | -2.4810 |
| sortino_ratio | -0.9804 |
| max_drawdown | 0.6945 |
| cagr | -0.3608 |
| net_avg_win | 41.5610 |
| net_avg_loss | -60.8829 |
| avg_hold_time_bars | 12.7583 |
| exposure | 0.4390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
