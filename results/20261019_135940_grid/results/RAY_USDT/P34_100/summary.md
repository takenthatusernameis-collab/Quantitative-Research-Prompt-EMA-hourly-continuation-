# EMA Hourly Continuation — RAY/USDT P34_100

**Symbol:** RAY/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.5948 |
| net_win_rate | 0.4766 |
| gross_profit_factor | 0.9125 |
| gross_win_rate | 0.4887 |
| sharpe_ratio | -3.9719 |
| sortino_ratio | -1.4318 |
| max_drawdown | 0.8477 |
| cagr | -0.5006 |
| net_avg_win | 38.3285 |
| net_avg_loss | -58.6833 |
| avg_hold_time_bars | 7.8612 |
| exposure | 0.2369 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
