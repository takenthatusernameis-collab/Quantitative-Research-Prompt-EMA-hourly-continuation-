# EMA Hourly Continuation — MOCA/USDT P8_21

**Symbol:** MOCA/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1437 |
| net_profit_factor | 0.3914 |
| net_win_rate | 0.3967 |
| gross_profit_factor | 0.6940 |
| gross_win_rate | 0.4280 |
| sharpe_ratio | -12.7553 |
| sortino_ratio | -7.2016 |
| max_drawdown | 0.9997 |
| cagr | -0.9730 |
| net_avg_win | 11.2806 |
| net_avg_loss | -18.9472 |
| avg_hold_time_bars | 3.2380 |
| exposure | 0.2333 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
