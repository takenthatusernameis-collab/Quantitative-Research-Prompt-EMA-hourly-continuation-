# EMA Hourly Continuation — NYM/USDT P50_89

**Symbol:** NYM/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 263 |
| net_profit_factor | 0.4068 |
| net_win_rate | 0.4106 |
| gross_profit_factor | 0.6939 |
| gross_win_rate | 0.4183 |
| sharpe_ratio | -4.0569 |
| sortino_ratio | -0.9422 |
| max_drawdown | 0.6817 |
| cagr | -0.3556 |
| net_avg_win | 42.4359 |
| net_avg_loss | -72.6883 |
| avg_hold_time_bars | 10.4449 |
| exposure | 0.1249 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
