# EMA Hourly Continuation — NOT/USDT P21_100

**Symbol:** NOT/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 674 |
| net_profit_factor | 0.6243 |
| net_win_rate | 0.4777 |
| gross_profit_factor | 0.9209 |
| gross_win_rate | 0.4807 |
| sharpe_ratio | -4.0537 |
| sortino_ratio | -1.5009 |
| max_drawdown | 0.8335 |
| cagr | -0.5150 |
| net_avg_win | 42.7118 |
| net_avg_loss | -62.5847 |
| avg_hold_time_bars | 12.9585 |
| exposure | 0.4103 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
