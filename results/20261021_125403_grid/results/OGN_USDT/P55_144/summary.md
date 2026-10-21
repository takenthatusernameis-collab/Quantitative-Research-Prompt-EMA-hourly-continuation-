# EMA Hourly Continuation — OGN/USDT P55_144

**Symbol:** OGN/USDT  |  **P_fast:** 55  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 404 |
| net_profit_factor | 0.5077 |
| net_win_rate | 0.4183 |
| gross_profit_factor | 0.6822 |
| gross_win_rate | 0.4183 |
| sharpe_ratio | -3.9973 |
| sortino_ratio | -1.1341 |
| max_drawdown | 0.7464 |
| cagr | -0.4098 |
| net_avg_win | 44.8886 |
| net_avg_loss | -63.5830 |
| avg_hold_time_bars | 15.0025 |
| exposure | 0.2743 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
