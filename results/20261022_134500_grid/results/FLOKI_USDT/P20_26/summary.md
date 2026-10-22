# EMA Hourly Continuation — FLOKI/USDT P20_26

**Symbol:** FLOKI/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1306 |
| net_profit_factor | 0.2640 |
| net_win_rate | 0.3530 |
| gross_profit_factor | 0.6156 |
| gross_win_rate | 0.3890 |
| sharpe_ratio | -15.0056 |
| sortino_ratio | -7.8248 |
| max_drawdown | 1.0000 |
| cagr | -0.9850 |
| net_avg_win | 7.7817 |
| net_avg_loss | -16.0794 |
| avg_hold_time_bars | 1.9288 |
| exposure | 0.1145 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
