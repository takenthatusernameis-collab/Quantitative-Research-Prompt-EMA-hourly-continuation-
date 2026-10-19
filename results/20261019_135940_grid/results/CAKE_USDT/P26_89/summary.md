# EMA Hourly Continuation — CAKE/USDT P26_89

**Symbol:** CAKE/USDT  |  **P_fast:** 26  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 636 |
| net_profit_factor | 0.5894 |
| net_win_rate | 0.4984 |
| gross_profit_factor | 1.0370 |
| gross_win_rate | 0.5126 |
| sharpe_ratio | -4.0161 |
| sortino_ratio | -1.4179 |
| max_drawdown | 0.8391 |
| cagr | -0.5025 |
| net_avg_win | 37.4463 |
| net_avg_loss | -63.1304 |
| avg_hold_time_bars | 11.5487 |
| exposure | 0.3339 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
