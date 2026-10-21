# EMA Hourly Continuation — MASK/USDT P8_55

**Symbol:** MASK/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 752 |
| net_profit_factor | 0.6176 |
| net_win_rate | 0.4681 |
| gross_profit_factor | 0.8568 |
| gross_win_rate | 0.4694 |
| sharpe_ratio | -3.9437 |
| sortino_ratio | -1.5391 |
| max_drawdown | 0.8349 |
| cagr | -0.5074 |
| net_avg_win | 38.1245 |
| net_avg_loss | -54.3269 |
| avg_hold_time_bars | 13.8231 |
| exposure | 0.4725 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
