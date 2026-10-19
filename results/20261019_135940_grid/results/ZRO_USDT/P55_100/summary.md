# EMA Hourly Continuation — ZRO/USDT P55_100

**Symbol:** ZRO/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 592 |
| net_profit_factor | 0.6178 |
| net_win_rate | 0.4882 |
| gross_profit_factor | 0.9313 |
| gross_win_rate | 0.4899 |
| sharpe_ratio | -3.5396 |
| sortino_ratio | -1.2657 |
| max_drawdown | 0.7762 |
| cagr | -0.4512 |
| net_avg_win | 42.1349 |
| net_avg_loss | -65.0491 |
| avg_hold_time_bars | 4.7534 |
| exposure | 0.1377 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
