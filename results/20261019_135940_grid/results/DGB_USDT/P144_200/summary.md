# EMA Hourly Continuation — DGB/USDT P144_200

**Symbol:** DGB/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 465 |
| net_profit_factor | 0.4692 |
| net_win_rate | 0.4430 |
| gross_profit_factor | 0.8893 |
| gross_win_rate | 0.4602 |
| sharpe_ratio | -5.1413 |
| sortino_ratio | -1.5673 |
| max_drawdown | 0.8564 |
| cagr | -0.5349 |
| net_avg_win | 36.6347 |
| net_avg_loss | -62.1016 |
| avg_hold_time_bars | 4.4301 |
| exposure | 0.0936 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
