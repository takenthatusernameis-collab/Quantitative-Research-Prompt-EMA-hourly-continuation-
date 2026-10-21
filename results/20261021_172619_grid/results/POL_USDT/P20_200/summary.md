# EMA Hourly Continuation — POL/USDT P20_200

**Symbol:** POL/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 266 |
| net_profit_factor | 1.0429 |
| net_win_rate | 0.5564 |
| gross_profit_factor | 1.2530 |
| gross_win_rate | 0.5564 |
| sharpe_ratio | 0.2534 |
| sortino_ratio | 0.0601 |
| max_drawdown | 0.1630 |
| cagr | 0.0209 |
| net_avg_win | 87.7854 |
| net_avg_loss | -105.5758 |
| avg_hold_time_bars | 55.8759 |
| exposure | 0.6756 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
