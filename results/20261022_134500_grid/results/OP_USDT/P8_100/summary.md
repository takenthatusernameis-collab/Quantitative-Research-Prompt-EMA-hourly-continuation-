# EMA Hourly Continuation — OP/USDT P8_100

**Symbol:** OP/USDT  |  **P_fast:** 8  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 626 |
| net_profit_factor | 0.6502 |
| net_win_rate | 0.4728 |
| gross_profit_factor | 0.9447 |
| gross_win_rate | 0.4824 |
| sharpe_ratio | -3.4546 |
| sortino_ratio | -1.2233 |
| max_drawdown | 0.7830 |
| cagr | -0.4347 |
| net_avg_win | 47.8081 |
| net_avg_loss | -65.9525 |
| avg_hold_time_bars | 23.6518 |
| exposure | 0.6730 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
