# EMA Hourly Continuation — MTL/USDT P20_144

**Symbol:** MTL/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 376 |
| net_profit_factor | 0.7423 |
| net_win_rate | 0.4894 |
| gross_profit_factor | 0.9564 |
| gross_win_rate | 0.4894 |
| sharpe_ratio | -1.8422 |
| sortino_ratio | -0.5086 |
| max_drawdown | 0.4740 |
| cagr | -0.2094 |
| net_avg_win | 70.0110 |
| net_avg_loss | -90.3813 |
| avg_hold_time_bars | 33.0319 |
| exposure | 0.5620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
