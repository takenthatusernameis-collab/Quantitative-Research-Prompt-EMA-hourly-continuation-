# EMA Hourly Continuation — IOST/USDT P55_89

**Symbol:** IOST/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 384 |
| net_profit_factor | 0.7005 |
| net_win_rate | 0.5078 |
| gross_profit_factor | 1.0713 |
| gross_win_rate | 0.5078 |
| sharpe_ratio | -2.4463 |
| sortino_ratio | -0.6899 |
| max_drawdown | 0.5554 |
| cagr | -0.2717 |
| net_avg_win | 65.8639 |
| net_avg_loss | -97.0030 |
| avg_hold_time_bars | 6.4453 |
| exposure | 0.1125 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
