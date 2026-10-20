# EMA Hourly Continuation — ELON/USDT P8_50

**Symbol:** ELON/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1211 |
| net_profit_factor | 0.4897 |
| net_win_rate | 0.4385 |
| gross_profit_factor | 0.8026 |
| gross_win_rate | 0.4443 |
| sharpe_ratio | -7.8329 |
| sortino_ratio | -3.8584 |
| max_drawdown | 0.9902 |
| cagr | -0.8416 |
| net_avg_win | 17.8980 |
| net_avg_loss | -28.5383 |
| avg_hold_time_bars | 7.4889 |
| exposure | 0.4122 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
