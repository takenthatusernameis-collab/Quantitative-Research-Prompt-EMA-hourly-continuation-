# EMA Hourly Continuation — BDX/USDT P20_50

**Symbol:** BDX/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1395 |
| net_profit_factor | 0.2396 |
| net_win_rate | 0.2545 |
| gross_profit_factor | 0.6285 |
| gross_win_rate | 0.3176 |
| sharpe_ratio | -20.6912 |
| sortino_ratio | -11.8731 |
| max_drawdown | 1.0000 |
| cagr | -0.9987 |
| net_avg_win | 8.8777 |
| net_avg_loss | -12.6458 |
| avg_hold_time_bars | 3.5756 |
| exposure | 0.2267 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
