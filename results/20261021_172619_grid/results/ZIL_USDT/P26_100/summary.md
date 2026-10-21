# EMA Hourly Continuation — ZIL/USDT P26_100

**Symbol:** ZIL/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.8191 |
| net_win_rate | 0.5190 |
| gross_profit_factor | 1.0765 |
| gross_win_rate | 0.5190 |
| sharpe_ratio | -1.3474 |
| sortino_ratio | -0.4097 |
| max_drawdown | 0.4853 |
| cagr | -0.1730 |
| net_avg_win | 74.0126 |
| net_avg_loss | -97.5070 |
| avg_hold_time_bars | 15.7517 |
| exposure | 0.3200 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
