# EMA Hourly Continuation — RLC/USDT P8_12

**Symbol:** RLC/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 437 |
| net_profit_factor | 0.6075 |
| net_win_rate | 0.4920 |
| gross_profit_factor | 0.9462 |
| gross_win_rate | 0.4943 |
| sharpe_ratio | -3.1377 |
| sortino_ratio | -0.9438 |
| max_drawdown | 0.6773 |
| cagr | -0.3493 |
| net_avg_win | 47.5137 |
| net_avg_loss | -75.7507 |
| avg_hold_time_bars | 4.4233 |
| exposure | 0.0879 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
