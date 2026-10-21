# EMA Hourly Continuation — NYM/USDT P8_20

**Symbol:** NYM/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 504 |
| net_profit_factor | 0.3689 |
| net_win_rate | 0.4385 |
| gross_profit_factor | 0.7582 |
| gross_win_rate | 0.4484 |
| sharpe_ratio | -5.5448 |
| sortino_ratio | -1.7799 |
| max_drawdown | 0.8800 |
| cagr | -0.5678 |
| net_avg_win | 23.2352 |
| net_avg_loss | -49.1813 |
| avg_hold_time_bars | 10.2381 |
| exposure | 0.2345 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
