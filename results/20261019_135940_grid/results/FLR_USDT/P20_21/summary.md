# EMA Hourly Continuation — FLR/USDT P20_21

**Symbol:** FLR/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1414 |
| net_profit_factor | 0.1470 |
| net_win_rate | 0.2468 |
| gross_profit_factor | 0.7050 |
| gross_win_rate | 0.3409 |
| sharpe_ratio | -21.2795 |
| sortino_ratio | -12.4951 |
| max_drawdown | 1.0000 |
| cagr | -0.9991 |
| net_avg_win | 4.9370 |
| net_avg_loss | -11.0075 |
| avg_hold_time_bars | 1.6994 |
| exposure | 0.1092 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
