# EMA Hourly Continuation — ZRO/USDT P12_50

**Symbol:** ZRO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 579 |
| net_profit_factor | 0.9699 |
| net_win_rate | 0.5458 |
| gross_profit_factor | 1.1864 |
| gross_win_rate | 0.5458 |
| sharpe_ratio | -0.1505 |
| sortino_ratio | -0.0545 |
| max_drawdown | 0.3070 |
| cagr | -0.0355 |
| net_avg_win | 82.4747 |
| net_avg_loss | -102.1686 |
| avg_hold_time_bars | 11.0397 |
| exposure | 0.3129 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
