# EMA Hourly Continuation — XYO/USDT P12_50

**Symbol:** XYO/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 664 |
| net_profit_factor | 0.6179 |
| net_win_rate | 0.4533 |
| gross_profit_factor | 0.8387 |
| gross_win_rate | 0.4548 |
| sharpe_ratio | -4.0578 |
| sortino_ratio | -1.4858 |
| max_drawdown | 0.8256 |
| cagr | -0.4950 |
| net_avg_win | 44.1428 |
| net_avg_loss | -59.2361 |
| avg_hold_time_bars | 10.2846 |
| exposure | 0.3090 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
