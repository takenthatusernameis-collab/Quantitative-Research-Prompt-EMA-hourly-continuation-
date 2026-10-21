# EMA Hourly Continuation — ZEN/USDT P50_89

**Symbol:** ZEN/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.7462 |
| net_win_rate | 0.5013 |
| gross_profit_factor | 1.0048 |
| gross_win_rate | 0.5013 |
| sharpe_ratio | -1.7853 |
| sortino_ratio | -0.4985 |
| max_drawdown | 0.4382 |
| cagr | -0.2052 |
| net_avg_win | 67.7994 |
| net_avg_loss | -91.3442 |
| avg_hold_time_bars | 7.5567 |
| exposure | 0.1302 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
