# EMA Hourly Continuation — SLP/USDT P21_100

**Symbol:** SLP/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 739 |
| net_profit_factor | 0.6085 |
| net_win_rate | 0.4601 |
| gross_profit_factor | 0.9477 |
| gross_win_rate | 0.4682 |
| sharpe_ratio | -4.9337 |
| sortino_ratio | -1.8748 |
| max_drawdown | 0.9034 |
| cagr | -0.6001 |
| net_avg_win | 41.1343 |
| net_avg_loss | -57.6061 |
| avg_hold_time_bars | 13.2287 |
| exposure | 0.4444 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
