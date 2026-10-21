# EMA Hourly Continuation — ZRX/USDT P20_55

**Symbol:** ZRX/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 617 |
| net_profit_factor | 0.6869 |
| net_win_rate | 0.4830 |
| gross_profit_factor | 0.9523 |
| gross_win_rate | 0.4830 |
| sharpe_ratio | -3.2739 |
| sortino_ratio | -1.1642 |
| max_drawdown | 0.7502 |
| cagr | -0.4139 |
| net_avg_win | 54.3818 |
| net_avg_loss | -73.9571 |
| avg_hold_time_bars | 8.7261 |
| exposure | 0.2447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
