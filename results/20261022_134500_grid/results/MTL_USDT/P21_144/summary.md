# EMA Hourly Continuation — MTL/USDT P21_144

**Symbol:** MTL/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 452 |
| net_profit_factor | 0.5975 |
| net_win_rate | 0.4624 |
| gross_profit_factor | 0.9097 |
| gross_win_rate | 0.4757 |
| sharpe_ratio | -3.5113 |
| sortino_ratio | -1.0479 |
| max_drawdown | 0.7308 |
| cagr | -0.3953 |
| net_avg_win | 51.0528 |
| net_avg_loss | -73.4929 |
| avg_hold_time_bars | 27.6770 |
| exposure | 0.5661 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
