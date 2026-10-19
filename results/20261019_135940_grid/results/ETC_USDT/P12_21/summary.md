# EMA Hourly Continuation — ETC/USDT P12_21

**Symbol:** ETC/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1489 |
| net_profit_factor | 0.2498 |
| net_win_rate | 0.3754 |
| gross_profit_factor | 0.9261 |
| gross_win_rate | 0.4399 |
| sharpe_ratio | -16.0081 |
| sortino_ratio | -8.9868 |
| max_drawdown | 1.0000 |
| cagr | -0.9918 |
| net_avg_win | 5.9559 |
| net_avg_loss | -14.3326 |
| avg_hold_time_bars | 2.1968 |
| exposure | 0.1487 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
