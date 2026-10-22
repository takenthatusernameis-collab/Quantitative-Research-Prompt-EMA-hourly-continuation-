# EMA Hourly Continuation — SKL/USDT P55_89

**Symbol:** SKL/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 334 |
| net_profit_factor | 0.7231 |
| net_win_rate | 0.4970 |
| gross_profit_factor | 0.9700 |
| gross_win_rate | 0.4970 |
| sharpe_ratio | -1.8011 |
| sortino_ratio | -0.4715 |
| max_drawdown | 0.4337 |
| cagr | -0.1940 |
| net_avg_win | 65.7675 |
| net_avg_loss | -89.8752 |
| avg_hold_time_bars | 6.5210 |
| exposure | 0.0990 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
