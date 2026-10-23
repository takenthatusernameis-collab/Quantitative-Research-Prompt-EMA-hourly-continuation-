# EMA Hourly Continuation — METIS/USDT P20_200

**Symbol:** METIS/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 372 |
| net_profit_factor | 0.6078 |
| net_win_rate | 0.4462 |
| gross_profit_factor | 0.8343 |
| gross_win_rate | 0.4516 |
| sharpe_ratio | -3.1064 |
| sortino_ratio | -0.8366 |
| max_drawdown | 0.6416 |
| cagr | -0.3317 |
| net_avg_win | 59.4122 |
| net_avg_loss | -78.7746 |
| avg_hold_time_bars | 37.3199 |
| exposure | 0.6310 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
