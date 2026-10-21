# EMA Hourly Continuation — W/USDT P8_144

**Symbol:** W/USDT  |  **P_fast:** 8  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 363 |
| net_profit_factor | 0.9863 |
| net_win_rate | 0.5344 |
| gross_profit_factor | 1.1338 |
| gross_win_rate | 0.5344 |
| sharpe_ratio | -0.0203 |
| sortino_ratio | -0.0056 |
| max_drawdown | 0.1505 |
| cagr | -0.0096 |
| net_avg_win | 89.3106 |
| net_avg_loss | -103.9430 |
| avg_hold_time_bars | 44.6474 |
| exposure | 0.7367 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
