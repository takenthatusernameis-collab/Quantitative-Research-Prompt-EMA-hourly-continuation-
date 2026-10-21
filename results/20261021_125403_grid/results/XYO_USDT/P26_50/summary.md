# EMA Hourly Continuation — XYO/USDT P26_50

**Symbol:** XYO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 428 |
| net_profit_factor | 0.6032 |
| net_win_rate | 0.4533 |
| gross_profit_factor | 0.8783 |
| gross_win_rate | 0.4556 |
| sharpe_ratio | -3.6486 |
| sortino_ratio | -1.0766 |
| max_drawdown | 0.7145 |
| cagr | -0.3916 |
| net_avg_win | 55.9806 |
| net_avg_loss | -76.9438 |
| avg_hold_time_bars | 7.2664 |
| exposure | 0.1407 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
