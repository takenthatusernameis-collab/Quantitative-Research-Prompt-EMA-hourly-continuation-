# EMA Hourly Continuation — UMA/USDT P12_55

**Symbol:** UMA/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 987 |
| net_profit_factor | 0.5056 |
| net_win_rate | 0.4590 |
| gross_profit_factor | 0.8500 |
| gross_win_rate | 0.4701 |
| sharpe_ratio | -6.0844 |
| sortino_ratio | -2.6965 |
| max_drawdown | 0.9619 |
| cagr | -0.7218 |
| net_avg_win | 21.6686 |
| net_avg_loss | -36.3550 |
| avg_hold_time_bars | 8.1003 |
| exposure | 0.3634 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
