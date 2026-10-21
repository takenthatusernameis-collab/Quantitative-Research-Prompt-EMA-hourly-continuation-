# EMA Hourly Continuation — FLOKI/USDT P34_55

**Symbol:** FLOKI/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 314 |
| net_profit_factor | 0.6994 |
| net_win_rate | 0.4841 |
| gross_profit_factor | 0.9376 |
| gross_win_rate | 0.4841 |
| sharpe_ratio | -2.0418 |
| sortino_ratio | -0.5179 |
| max_drawdown | 0.4566 |
| cagr | -0.2113 |
| net_avg_win | 68.7489 |
| net_avg_loss | -92.2248 |
| avg_hold_time_bars | 5.5637 |
| exposure | 0.0794 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
