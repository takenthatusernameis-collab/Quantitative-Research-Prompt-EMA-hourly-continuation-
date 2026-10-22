# EMA Hourly Continuation — CYBER/USDT P21_144

**Symbol:** CYBER/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 373 |
| net_profit_factor | 0.7980 |
| net_win_rate | 0.4879 |
| gross_profit_factor | 0.9563 |
| gross_win_rate | 0.4879 |
| sharpe_ratio | -1.4140 |
| sortino_ratio | -0.3897 |
| max_drawdown | 0.3981 |
| cagr | -0.1655 |
| net_avg_win | 79.2775 |
| net_avg_loss | -94.6585 |
| avg_hold_time_bars | 33.7373 |
| exposure | 0.5720 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
