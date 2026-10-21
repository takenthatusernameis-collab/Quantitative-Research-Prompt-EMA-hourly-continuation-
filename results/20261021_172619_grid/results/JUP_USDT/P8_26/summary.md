# EMA Hourly Continuation — JUP/USDT P8_26

**Symbol:** JUP/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 638 |
| net_profit_factor | 0.8851 |
| net_win_rate | 0.5329 |
| gross_profit_factor | 1.1332 |
| gross_win_rate | 0.5329 |
| sharpe_ratio | -0.9255 |
| sortino_ratio | -0.3378 |
| max_drawdown | 0.3751 |
| cagr | -0.1483 |
| net_avg_win | 75.1617 |
| net_avg_loss | -96.8877 |
| avg_hold_time_bars | 6.7445 |
| exposure | 0.1956 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
