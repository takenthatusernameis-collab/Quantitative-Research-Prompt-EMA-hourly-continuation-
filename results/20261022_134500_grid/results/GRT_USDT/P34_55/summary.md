# EMA Hourly Continuation — GRT/USDT P34_55

**Symbol:** GRT/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 861 |
| net_profit_factor | 0.4158 |
| net_win_rate | 0.4390 |
| gross_profit_factor | 0.8048 |
| gross_win_rate | 0.4634 |
| sharpe_ratio | -7.8650 |
| sortino_ratio | -3.2643 |
| max_drawdown | 0.9838 |
| cagr | -0.8018 |
| net_avg_win | 18.5094 |
| net_avg_loss | -34.8404 |
| avg_hold_time_bars | 3.1905 |
| exposure | 0.1243 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
