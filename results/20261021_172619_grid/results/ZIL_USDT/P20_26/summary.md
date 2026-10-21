# EMA Hourly Continuation — ZIL/USDT P20_26

**Symbol:** ZIL/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 200 |
| net_profit_factor | 0.6957 |
| net_win_rate | 0.5050 |
| gross_profit_factor | 1.0470 |
| gross_win_rate | 0.5050 |
| sharpe_ratio | -1.7144 |
| sortino_ratio | -0.3493 |
| max_drawdown | 0.3744 |
| cagr | -0.1478 |
| net_avg_win | 74.8703 |
| net_avg_loss | -109.7911 |
| avg_hold_time_bars | 4.7400 |
| exposure | 0.0431 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
