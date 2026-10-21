# EMA Hourly Continuation — SEI/USDT P20_50

**Symbol:** SEI/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.7442 |
| net_win_rate | 0.4881 |
| gross_profit_factor | 0.9619 |
| gross_win_rate | 0.4881 |
| sharpe_ratio | -2.0859 |
| sortino_ratio | -0.6409 |
| max_drawdown | 0.5307 |
| cagr | -0.2546 |
| net_avg_win | 67.4604 |
| net_avg_loss | -86.4283 |
| avg_hold_time_bars | 9.0629 |
| exposure | 0.1899 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
