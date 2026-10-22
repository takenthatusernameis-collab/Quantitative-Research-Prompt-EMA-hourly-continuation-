# EMA Hourly Continuation — TAO/USDT P20_100

**Symbol:** TAO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 705 |
| net_profit_factor | 0.7179 |
| net_win_rate | 0.4950 |
| gross_profit_factor | 1.0044 |
| gross_win_rate | 0.4979 |
| sharpe_ratio | -3.3723 |
| sortino_ratio | -1.2505 |
| max_drawdown | 0.7947 |
| cagr | -0.4562 |
| net_avg_win | 57.1277 |
| net_avg_loss | -78.0121 |
| avg_hold_time_bars | 12.3149 |
| exposure | 0.3946 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
