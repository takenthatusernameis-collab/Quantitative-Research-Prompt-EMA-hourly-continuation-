# EMA Hourly Continuation — NEO/USDT P26_200

**Symbol:** NEO/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.5722 |
| net_win_rate | 0.4536 |
| gross_profit_factor | 0.8297 |
| gross_win_rate | 0.4590 |
| sharpe_ratio | -3.1765 |
| sortino_ratio | -0.8452 |
| max_drawdown | 0.6538 |
| cagr | -0.3377 |
| net_avg_win | 51.9382 |
| net_avg_loss | -75.3407 |
| avg_hold_time_bars | 36.1421 |
| exposure | 0.6013 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
