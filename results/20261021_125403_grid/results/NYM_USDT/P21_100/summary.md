# EMA Hourly Continuation — NYM/USDT P21_100

**Symbol:** NYM/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 380 |
| net_profit_factor | 0.5217 |
| net_win_rate | 0.4342 |
| gross_profit_factor | 0.7810 |
| gross_win_rate | 0.4395 |
| sharpe_ratio | -3.7073 |
| sortino_ratio | -1.0255 |
| max_drawdown | 0.7082 |
| cagr | -0.3784 |
| net_avg_win | 46.0816 |
| net_avg_loss | -67.7863 |
| avg_hold_time_bars | 21.9184 |
| exposure | 0.3786 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
