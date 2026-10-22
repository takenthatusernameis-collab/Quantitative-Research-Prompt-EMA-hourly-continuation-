# EMA Hourly Continuation — COMP/USDT P89_100

**Symbol:** COMP/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 621 |
| net_profit_factor | 0.2032 |
| net_win_rate | 0.3881 |
| gross_profit_factor | 0.6991 |
| gross_win_rate | 0.4461 |
| sharpe_ratio | -9.6971 |
| sortino_ratio | -3.5255 |
| max_drawdown | 0.9907 |
| cagr | -0.8444 |
| net_avg_win | 10.4833 |
| net_avg_loss | -32.7183 |
| avg_hold_time_bars | 2.1836 |
| exposure | 0.0616 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
