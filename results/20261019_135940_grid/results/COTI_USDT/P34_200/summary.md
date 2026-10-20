# EMA Hourly Continuation — COTI/USDT P34_200

**Symbol:** COTI/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 379 |
| net_profit_factor | 0.9569 |
| net_win_rate | 0.5620 |
| gross_profit_factor | 1.2861 |
| gross_win_rate | 0.5646 |
| sharpe_ratio | -0.2160 |
| sortino_ratio | -0.0601 |
| max_drawdown | 0.2577 |
| cagr | -0.0341 |
| net_avg_win | 87.0012 |
| net_avg_loss | -116.6659 |
| avg_hold_time_bars | 30.4644 |
| exposure | 0.5248 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
