# EMA Hourly Continuation — DGB/USDT P144_200

**Symbol:** DGB/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 207 |
| net_profit_factor | 0.7029 |
| net_win_rate | 0.4879 |
| gross_profit_factor | 0.9671 |
| gross_win_rate | 0.4879 |
| sharpe_ratio | -1.6379 |
| sortino_ratio | -0.3378 |
| max_drawdown | 0.3337 |
| cagr | -0.1431 |
| net_avg_win | 75.2998 |
| net_avg_loss | -102.0771 |
| avg_hold_time_bars | 7.3527 |
| exposure | 0.0692 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
