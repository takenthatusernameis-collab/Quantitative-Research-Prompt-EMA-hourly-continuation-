# EMA Hourly Continuation — MTL/USDT P50_144

**Symbol:** MTL/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 453 |
| net_profit_factor | 0.4918 |
| net_win_rate | 0.4459 |
| gross_profit_factor | 0.8131 |
| gross_win_rate | 0.4592 |
| sharpe_ratio | -4.5243 |
| sortino_ratio | -1.3509 |
| max_drawdown | 0.8098 |
| cagr | -0.4807 |
| net_avg_win | 38.7389 |
| net_avg_loss | -63.3880 |
| avg_hold_time_bars | 15.6777 |
| exposure | 0.3214 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
