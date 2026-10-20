# EMA Hourly Continuation — SKL/USDT P8_12

**Symbol:** SKL/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1900 |
| net_profit_factor | 0.2428 |
| net_win_rate | 0.3874 |
| gross_profit_factor | 0.7667 |
| gross_win_rate | 0.4395 |
| sharpe_ratio | -16.8858 |
| sortino_ratio | -10.5707 |
| max_drawdown | 1.0000 |
| cagr | -0.9961 |
| net_avg_win | 4.3577 |
| net_avg_loss | -11.3465 |
| avg_hold_time_bars | 1.8011 |
| exposure | 0.1555 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
