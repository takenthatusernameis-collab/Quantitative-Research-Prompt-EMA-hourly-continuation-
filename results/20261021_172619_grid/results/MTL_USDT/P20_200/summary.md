# EMA Hourly Continuation — MTL/USDT P20_200

**Symbol:** MTL/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 295 |
| net_profit_factor | 0.7108 |
| net_win_rate | 0.4678 |
| gross_profit_factor | 0.8824 |
| gross_win_rate | 0.4678 |
| sharpe_ratio | -1.8779 |
| sortino_ratio | -0.4563 |
| max_drawdown | 0.4283 |
| cagr | -0.1914 |
| net_avg_win | 73.9142 |
| net_avg_loss | -91.3978 |
| avg_hold_time_bars | 49.1017 |
| exposure | 0.6555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
