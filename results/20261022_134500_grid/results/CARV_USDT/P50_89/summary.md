# EMA Hourly Continuation — CARV/USDT P50_89

**Symbol:** CARV/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 439 |
| net_profit_factor | 0.4475 |
| net_win_rate | 0.4305 |
| gross_profit_factor | 0.8568 |
| gross_win_rate | 0.4647 |
| sharpe_ratio | -5.5658 |
| sortino_ratio | -1.8411 |
| max_drawdown | 0.8379 |
| cagr | -0.5823 |
| net_avg_win | 35.5681 |
| net_avg_loss | -60.0833 |
| avg_hold_time_bars | 5.7107 |
| exposure | 0.1411 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
