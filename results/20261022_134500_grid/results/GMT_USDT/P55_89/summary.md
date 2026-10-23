# EMA Hourly Continuation — GMT/USDT P55_89

**Symbol:** GMT/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 687 |
| net_profit_factor | 0.4728 |
| net_win_rate | 0.4279 |
| gross_profit_factor | 0.9174 |
| gross_win_rate | 0.4469 |
| sharpe_ratio | -6.8805 |
| sortino_ratio | -2.5619 |
| max_drawdown | 0.9594 |
| cagr | -0.7143 |
| net_avg_win | 29.1865 |
| net_avg_loss | -46.1848 |
| avg_hold_time_bars | 3.8370 |
| exposure | 0.1198 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
