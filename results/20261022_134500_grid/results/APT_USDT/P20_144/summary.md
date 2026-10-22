# EMA Hourly Continuation — APT/USDT P20_144

**Symbol:** APT/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.7104 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0016 |
| gross_win_rate | 0.5052 |
| sharpe_ratio | -1.9669 |
| sortino_ratio | -0.5399 |
| max_drawdown | 0.4957 |
| cagr | -0.2296 |
| net_avg_win | 61.7342 |
| net_avg_loss | -86.8971 |
| avg_hold_time_bars | 35.5916 |
| exposure | 0.6180 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
