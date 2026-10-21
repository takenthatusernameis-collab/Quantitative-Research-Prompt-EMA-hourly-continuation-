# EMA Hourly Continuation — CRV/USDT P8_100

**Symbol:** CRV/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.8431 |
| net_win_rate | 0.5011 |
| gross_profit_factor | 1.0064 |
| gross_win_rate | 0.5011 |
| sharpe_ratio | -1.1582 |
| sortino_ratio | -0.3474 |
| max_drawdown | 0.3688 |
| cagr | -0.1498 |
| net_avg_win | 81.7577 |
| net_avg_loss | -97.4107 |
| avg_hold_time_bars | 33.5877 |
| exposure | 0.6702 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
