# EMA Hourly Continuation — BRETT/USDT P12_21

**Symbol:** BRETT/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1376 |
| net_profit_factor | 0.4763 |
| net_win_rate | 0.4339 |
| gross_profit_factor | 0.8518 |
| gross_win_rate | 0.4520 |
| sharpe_ratio | -9.9832 |
| sortino_ratio | -5.3610 |
| max_drawdown | 0.9983 |
| cagr | -0.9314 |
| net_avg_win | 15.2091 |
| net_avg_loss | -24.4705 |
| avg_hold_time_bars | 2.4978 |
| exposure | 0.1654 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
