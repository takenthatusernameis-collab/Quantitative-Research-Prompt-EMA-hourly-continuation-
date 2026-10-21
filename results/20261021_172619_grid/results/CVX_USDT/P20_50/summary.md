# EMA Hourly Continuation — CVX/USDT P20_50

**Symbol:** CVX/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 567 |
| net_profit_factor | 0.7799 |
| net_win_rate | 0.5044 |
| gross_profit_factor | 1.0240 |
| gross_win_rate | 0.5044 |
| sharpe_ratio | -1.9489 |
| sortino_ratio | -0.6661 |
| max_drawdown | 0.5464 |
| cagr | -0.2640 |
| net_avg_win | 66.4980 |
| net_avg_loss | -86.7854 |
| avg_hold_time_bars | 6.8818 |
| exposure | 0.1774 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
