# EMA Hourly Continuation — PUNDIX/USDT P50_144

**Symbol:** PUNDIX/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.7185 |
| net_win_rate | 0.4974 |
| gross_profit_factor | 0.9883 |
| gross_win_rate | 0.4974 |
| sharpe_ratio | -2.0637 |
| sortino_ratio | -0.5812 |
| max_drawdown | 0.4980 |
| cagr | -0.2348 |
| net_avg_win | 64.7303 |
| net_avg_loss | -89.1619 |
| avg_hold_time_bars | 16.5438 |
| exposure | 0.2918 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
