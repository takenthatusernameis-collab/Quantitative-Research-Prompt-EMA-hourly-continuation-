# EMA Hourly Continuation — TIA/USDT P26_55

**Symbol:** TIA/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 430 |
| net_profit_factor | 0.8395 |
| net_win_rate | 0.5140 |
| gross_profit_factor | 1.0567 |
| gross_win_rate | 0.5140 |
| sharpe_ratio | -1.1581 |
| sortino_ratio | -0.3453 |
| max_drawdown | 0.3861 |
| cagr | -0.1482 |
| net_avg_win | 78.4637 |
| net_avg_loss | -98.8370 |
| avg_hold_time_bars | 7.0163 |
| exposure | 0.1371 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
