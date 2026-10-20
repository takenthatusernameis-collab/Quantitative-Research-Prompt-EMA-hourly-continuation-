# EMA Hourly Continuation — WAVES/USDT P8_21

**Symbol:** WAVES/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1804 |
| net_profit_factor | 0.3466 |
| net_win_rate | 0.4030 |
| gross_profit_factor | 0.9004 |
| gross_win_rate | 0.4479 |
| sharpe_ratio | -14.9501 |
| sortino_ratio | -9.0534 |
| max_drawdown | 1.0000 |
| cagr | -0.9907 |
| net_avg_win | 7.2980 |
| net_avg_loss | -14.2113 |
| avg_hold_time_bars | 2.9712 |
| exposure | 0.2436 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
