# EMA Hourly Continuation — PUNDIX/USDT P34_144

**Symbol:** PUNDIX/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.7768 |
| net_win_rate | 0.5038 |
| gross_profit_factor | 1.0236 |
| gross_win_rate | 0.5038 |
| sharpe_ratio | -1.6297 |
| sortino_ratio | -0.4608 |
| max_drawdown | 0.4305 |
| cagr | -0.1927 |
| net_avg_win | 73.4930 |
| net_avg_loss | -96.0675 |
| avg_hold_time_bars | 23.5754 |
| exposure | 0.4190 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
