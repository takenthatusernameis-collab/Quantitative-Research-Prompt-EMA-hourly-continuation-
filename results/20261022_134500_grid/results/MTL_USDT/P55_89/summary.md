# EMA Hourly Continuation — MTL/USDT P55_89

**Symbol:** MTL/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 633 |
| net_profit_factor | 0.3779 |
| net_win_rate | 0.3934 |
| gross_profit_factor | 0.7395 |
| gross_win_rate | 0.4313 |
| sharpe_ratio | -7.7130 |
| sortino_ratio | -2.7394 |
| max_drawdown | 0.9685 |
| cagr | -0.7462 |
| net_avg_win | 23.6242 |
| net_avg_loss | -40.5408 |
| avg_hold_time_bars | 6.1343 |
| exposure | 0.1757 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
