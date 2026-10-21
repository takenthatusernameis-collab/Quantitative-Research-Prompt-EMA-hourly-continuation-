# EMA Hourly Continuation — ENA/USDT P20_55

**Symbol:** ENA/USDT  |  **P_fast:** 20  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 498 |
| net_profit_factor | 0.9530 |
| net_win_rate | 0.5382 |
| gross_profit_factor | 1.1501 |
| gross_win_rate | 0.5382 |
| sharpe_ratio | -0.2601 |
| sortino_ratio | -0.0840 |
| max_drawdown | 0.3422 |
| cagr | -0.0454 |
| net_avg_win | 83.4105 |
| net_avg_loss | -101.9799 |
| avg_hold_time_bars | 9.2771 |
| exposure | 0.2100 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
