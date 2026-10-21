# EMA Hourly Continuation — TAO/USDT P50_55

**Symbol:** TAO/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 82 |
| net_profit_factor | 0.8833 |
| net_win_rate | 0.5366 |
| gross_profit_factor | 1.1557 |
| gross_win_rate | 0.5366 |
| sharpe_ratio | -0.3473 |
| sortino_ratio | -0.0455 |
| max_drawdown | 0.1434 |
| cagr | -0.0213 |
| net_avg_win | 90.4226 |
| net_avg_loss | -118.5384 |
| avg_hold_time_bars | 5.8171 |
| exposure | 0.0217 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
