# EMA Hourly Continuation — CYBER/USDT P21_100

**Symbol:** CYBER/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 493 |
| net_profit_factor | 0.7035 |
| net_win_rate | 0.4726 |
| gross_profit_factor | 0.8782 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -2.3692 |
| sortino_ratio | -0.7487 |
| max_drawdown | 0.5988 |
| cagr | -0.2915 |
| net_avg_win | 58.9756 |
| net_avg_loss | -75.1262 |
| avg_hold_time_bars | 19.7728 |
| exposure | 0.4431 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
