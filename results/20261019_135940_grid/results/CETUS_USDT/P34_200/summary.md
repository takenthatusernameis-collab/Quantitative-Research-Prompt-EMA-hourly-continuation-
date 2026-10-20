# EMA Hourly Continuation — CETUS/USDT P34_200

**Symbol:** CETUS/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 311 |
| net_profit_factor | 0.7911 |
| net_win_rate | 0.5113 |
| gross_profit_factor | 1.0690 |
| gross_win_rate | 0.5145 |
| sharpe_ratio | -1.3437 |
| sortino_ratio | -0.3348 |
| max_drawdown | 0.3646 |
| cagr | -0.1481 |
| net_avg_win | 79.2039 |
| net_avg_loss | -104.7313 |
| avg_hold_time_bars | 41.3537 |
| exposure | 0.5820 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
