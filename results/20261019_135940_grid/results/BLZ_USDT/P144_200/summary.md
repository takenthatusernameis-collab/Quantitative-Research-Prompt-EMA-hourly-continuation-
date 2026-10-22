# EMA Hourly Continuation — BLZ/USDT P144_200

**Symbol:** BLZ/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 462 |
| net_profit_factor | 0.5458 |
| net_win_rate | 0.4481 |
| gross_profit_factor | 0.9063 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -4.5983 |
| sortino_ratio | -1.3998 |
| max_drawdown | 0.8277 |
| cagr | -0.4873 |
| net_avg_win | 47.2970 |
| net_avg_loss | -70.3397 |
| avg_hold_time_bars | 6.5693 |
| exposure | 0.1373 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
