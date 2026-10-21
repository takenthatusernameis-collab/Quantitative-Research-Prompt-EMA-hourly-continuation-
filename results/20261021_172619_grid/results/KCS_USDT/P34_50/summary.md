# EMA Hourly Continuation — KCS/USDT P34_50

**Symbol:** KCS/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 265 |
| net_profit_factor | 0.3288 |
| net_win_rate | 0.3962 |
| gross_profit_factor | 0.7075 |
| gross_win_rate | 0.4000 |
| sharpe_ratio | -5.4056 |
| sortino_ratio | -1.2906 |
| max_drawdown | 0.7870 |
| cagr | -0.4524 |
| net_avg_win | 36.3755 |
| net_avg_loss | -72.5939 |
| avg_hold_time_bars | 6.0830 |
| exposure | 0.0733 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
