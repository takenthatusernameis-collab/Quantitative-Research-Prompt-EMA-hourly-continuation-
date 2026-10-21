# EMA Hourly Continuation — W/USDT P20_21

**Symbol:** W/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 148 |
| net_profit_factor | 0.8728 |
| net_win_rate | 0.5405 |
| gross_profit_factor | 1.1768 |
| gross_win_rate | 0.5405 |
| sharpe_ratio | -0.5325 |
| sortino_ratio | -0.0937 |
| max_drawdown | 0.2389 |
| cagr | -0.0434 |
| net_avg_win | 90.4438 |
| net_avg_loss | -121.9154 |
| avg_hold_time_bars | 4.6689 |
| exposure | 0.0314 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
