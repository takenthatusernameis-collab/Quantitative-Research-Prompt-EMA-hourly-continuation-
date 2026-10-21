# EMA Hourly Continuation — CRV/USDT P26_100

**Symbol:** CRV/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 412 |
| net_profit_factor | 0.8905 |
| net_win_rate | 0.5218 |
| gross_profit_factor | 1.0921 |
| gross_win_rate | 0.5218 |
| sharpe_ratio | -0.7619 |
| sortino_ratio | -0.2227 |
| max_drawdown | 0.3261 |
| cagr | -0.1007 |
| net_avg_win | 88.4869 |
| net_avg_loss | -108.4450 |
| avg_hold_time_bars | 16.5728 |
| exposure | 0.3104 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
