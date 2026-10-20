# EMA Hourly Continuation — EUL/USDT P55_89

**Symbol:** EUL/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 583 |
| net_profit_factor | 0.2958 |
| net_win_rate | 0.3859 |
| gross_profit_factor | 0.5431 |
| gross_win_rate | 0.3979 |
| sharpe_ratio | -7.2188 |
| sortino_ratio | -2.4549 |
| max_drawdown | 0.9554 |
| cagr | -0.7070 |
| net_avg_win | 17.8159 |
| net_avg_loss | -37.8504 |
| avg_hold_time_bars | 4.8902 |
| exposure | 0.1296 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
