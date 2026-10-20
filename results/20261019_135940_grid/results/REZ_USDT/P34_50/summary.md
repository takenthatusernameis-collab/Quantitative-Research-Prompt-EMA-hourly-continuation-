# EMA Hourly Continuation — REZ/USDT P34_50

**Symbol:** REZ/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 914 |
| net_profit_factor | 0.5109 |
| net_win_rate | 0.4530 |
| gross_profit_factor | 0.9443 |
| gross_win_rate | 0.4726 |
| sharpe_ratio | -7.0292 |
| sortino_ratio | -3.0298 |
| max_drawdown | 0.9759 |
| cagr | -0.7719 |
| net_avg_win | 24.5790 |
| net_avg_loss | -39.8354 |
| avg_hold_time_bars | 3.2133 |
| exposure | 0.1355 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
