# EMA Hourly Continuation — JST/USDT P21_100

**Symbol:** JST/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.3789 |
| net_win_rate | 0.4627 |
| gross_profit_factor | 0.9966 |
| gross_win_rate | 0.4983 |
| sharpe_ratio | -5.8727 |
| sortino_ratio | -1.9721 |
| max_drawdown | 0.9301 |
| cagr | -0.6427 |
| net_avg_win | 20.6817 |
| net_avg_loss | -47.0051 |
| avg_hold_time_bars | 15.8508 |
| exposure | 0.4232 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
