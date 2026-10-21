# EMA Hourly Continuation — OP/USDT P8_50

**Symbol:** OP/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 641 |
| net_profit_factor | 0.7173 |
| net_win_rate | 0.4805 |
| gross_profit_factor | 0.8957 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -2.4310 |
| sortino_ratio | -0.8776 |
| max_drawdown | 0.6629 |
| cagr | -0.3319 |
| net_avg_win | 52.4583 |
| net_avg_loss | -67.6422 |
| avg_hold_time_bars | 15.4103 |
| exposure | 0.4490 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
