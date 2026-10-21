# EMA Hourly Continuation — GRT/USDT P26_100

**Symbol:** GRT/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.8088 |
| net_win_rate | 0.5077 |
| gross_profit_factor | 1.0194 |
| gross_win_rate | 0.5077 |
| sharpe_ratio | -1.4084 |
| sortino_ratio | -0.4289 |
| max_drawdown | 0.4462 |
| cagr | -0.1799 |
| net_avg_win | 72.3708 |
| net_avg_loss | -92.2927 |
| avg_hold_time_bars | 15.5938 |
| exposure | 0.3197 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
