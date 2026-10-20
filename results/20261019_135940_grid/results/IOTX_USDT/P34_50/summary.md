# EMA Hourly Continuation — IOTX/USDT P34_50

**Symbol:** IOTX/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 925 |
| net_profit_factor | 0.3921 |
| net_win_rate | 0.4227 |
| gross_profit_factor | 0.8830 |
| gross_win_rate | 0.4573 |
| sharpe_ratio | -9.3395 |
| sortino_ratio | -4.0438 |
| max_drawdown | 0.9943 |
| cagr | -0.8703 |
| net_avg_win | 16.3973 |
| net_avg_loss | -30.6219 |
| avg_hold_time_bars | 2.9924 |
| exposure | 0.1258 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
