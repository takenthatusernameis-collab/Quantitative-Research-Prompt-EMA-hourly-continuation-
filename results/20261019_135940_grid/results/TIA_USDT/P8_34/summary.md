# EMA Hourly Continuation — TIA/USDT P8_34

**Symbol:** TIA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1362 |
| net_profit_factor | 0.6122 |
| net_win_rate | 0.4574 |
| gross_profit_factor | 0.9516 |
| gross_win_rate | 0.4662 |
| sharpe_ratio | -7.3062 |
| sortino_ratio | -3.7877 |
| max_drawdown | 0.9905 |
| cagr | -0.8410 |
| net_avg_win | 25.0879 |
| net_avg_loss | -34.5481 |
| avg_hold_time_bars | 5.7188 |
| exposure | 0.3540 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
