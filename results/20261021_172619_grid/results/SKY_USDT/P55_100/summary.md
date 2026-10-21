# EMA Hourly Continuation — SKY/USDT P55_100

**Symbol:** SKY/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 321 |
| net_profit_factor | 0.9182 |
| net_win_rate | 0.5701 |
| gross_profit_factor | 1.3118 |
| gross_win_rate | 0.5701 |
| sharpe_ratio | -0.4845 |
| sortino_ratio | -0.1400 |
| max_drawdown | 0.2272 |
| cagr | -0.0662 |
| net_avg_win | 80.2608 |
| net_avg_loss | -115.9084 |
| avg_hold_time_bars | 7.2461 |
| exposure | 0.1297 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
