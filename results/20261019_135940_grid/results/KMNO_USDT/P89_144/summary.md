# EMA Hourly Continuation — KMNO/USDT P89_144

**Symbol:** KMNO/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.5352 |
| net_win_rate | 0.4601 |
| gross_profit_factor | 0.8790 |
| gross_win_rate | 0.4695 |
| sharpe_ratio | -4.0914 |
| sortino_ratio | -1.2021 |
| max_drawdown | 0.7614 |
| cagr | -0.4398 |
| net_avg_win | 44.7335 |
| net_avg_loss | -71.2236 |
| avg_hold_time_bars | 7.2113 |
| exposure | 0.1418 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
