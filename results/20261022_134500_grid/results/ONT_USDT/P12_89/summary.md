# EMA Hourly Continuation — ONT/USDT P12_89

**Symbol:** ONT/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 729 |
| net_profit_factor | 0.6296 |
| net_win_rate | 0.4650 |
| gross_profit_factor | 0.9147 |
| gross_win_rate | 0.4691 |
| sharpe_ratio | -4.2294 |
| sortino_ratio | -1.5984 |
| max_drawdown | 0.8614 |
| cagr | -0.5345 |
| net_avg_win | 42.8482 |
| net_avg_loss | -59.1591 |
| avg_hold_time_bars | 15.8587 |
| exposure | 0.5231 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
