# EMA Hourly Continuation — CATI/USDT P34_144

**Symbol:** CATI/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 426 |
| net_profit_factor | 0.5772 |
| net_win_rate | 0.4413 |
| gross_profit_factor | 0.9271 |
| gross_win_rate | 0.4671 |
| sharpe_ratio | -4.5473 |
| sortino_ratio | -1.4493 |
| max_drawdown | 0.8054 |
| cagr | -0.5047 |
| net_avg_win | 55.7978 |
| net_avg_loss | -76.3652 |
| avg_hold_time_bars | 19.8920 |
| exposure | 0.4645 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
