# EMA Hourly Continuation — SSV/USDT P50_200

**Symbol:** SSV/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 340 |
| net_profit_factor | 0.7318 |
| net_win_rate | 0.4765 |
| gross_profit_factor | 0.8973 |
| gross_win_rate | 0.4765 |
| sharpe_ratio | -1.7853 |
| sortino_ratio | -0.4672 |
| max_drawdown | 0.4352 |
| cagr | -0.1931 |
| net_avg_win | 70.3892 |
| net_avg_loss | -87.5463 |
| avg_hold_time_bars | 25.5471 |
| exposure | 0.3930 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
