# EMA Hourly Continuation — ZIL/USDT P12_100

**Symbol:** ZIL/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 465 |
| net_profit_factor | 0.7908 |
| net_win_rate | 0.5032 |
| gross_profit_factor | 0.9978 |
| gross_win_rate | 0.5032 |
| sharpe_ratio | -1.5140 |
| sortino_ratio | -0.4676 |
| max_drawdown | 0.4696 |
| cagr | -0.1947 |
| net_avg_win | 67.7627 |
| net_avg_loss | -86.8039 |
| avg_hold_time_bars | 26.1978 |
| exposure | 0.5537 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
