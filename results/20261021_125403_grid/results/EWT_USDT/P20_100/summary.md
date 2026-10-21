# EMA Hourly Continuation — EWT/USDT P20_100

**Symbol:** EWT/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 468 |
| net_profit_factor | 0.6773 |
| net_win_rate | 0.4573 |
| gross_profit_factor | 0.8264 |
| gross_win_rate | 0.4573 |
| sharpe_ratio | -2.5674 |
| sortino_ratio | -0.7873 |
| max_drawdown | 0.6264 |
| cagr | -0.3049 |
| net_avg_win | 58.7378 |
| net_avg_loss | -73.0649 |
| avg_hold_time_bars | 15.4915 |
| exposure | 0.3295 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
