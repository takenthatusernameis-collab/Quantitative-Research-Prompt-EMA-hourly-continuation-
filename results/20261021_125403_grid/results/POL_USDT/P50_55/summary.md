# EMA Hourly Continuation — POL/USDT P50_55

**Symbol:** POL/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 121 |
| net_profit_factor | 0.5405 |
| net_win_rate | 0.4545 |
| gross_profit_factor | 0.7981 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -1.9293 |
| sortino_ratio | -0.3040 |
| max_drawdown | 0.3139 |
| cagr | -0.1304 |
| net_avg_win | 63.2636 |
| net_avg_loss | -97.5446 |
| avg_hold_time_bars | 5.9174 |
| exposure | 0.0325 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
