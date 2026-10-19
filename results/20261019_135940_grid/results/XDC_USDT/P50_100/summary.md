# EMA Hourly Continuation — XDC/USDT P50_100

**Symbol:** XDC/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 712 |
| net_profit_factor | 0.2565 |
| net_win_rate | 0.4115 |
| gross_profit_factor | 0.7062 |
| gross_win_rate | 0.4508 |
| sharpe_ratio | -8.7499 |
| sortino_ratio | -3.2942 |
| max_drawdown | 0.9884 |
| cagr | -0.8279 |
| net_avg_win | 11.6349 |
| net_avg_loss | -31.7151 |
| avg_hold_time_bars | 5.0295 |
| exposure | 0.1628 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
