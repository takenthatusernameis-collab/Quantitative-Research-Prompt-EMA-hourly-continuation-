# EMA Hourly Continuation — CAKE/USDT P21_50

**Symbol:** CAKE/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 914 |
| net_profit_factor | 0.3595 |
| net_win_rate | 0.4365 |
| gross_profit_factor | 0.7912 |
| gross_win_rate | 0.4650 |
| sharpe_ratio | -8.1242 |
| sortino_ratio | -3.4883 |
| max_drawdown | 0.9861 |
| cagr | -0.8177 |
| net_avg_win | 13.8743 |
| net_avg_loss | -29.8966 |
| avg_hold_time_bars | 5.4223 |
| exposure | 0.2253 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
