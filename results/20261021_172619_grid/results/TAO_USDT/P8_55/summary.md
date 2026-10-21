# EMA Hourly Continuation — TAO/USDT P8_55

**Symbol:** TAO/USDT  |  **P_fast:** 8  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 637 |
| net_profit_factor | 0.9348 |
| net_win_rate | 0.5275 |
| gross_profit_factor | 1.1184 |
| gross_win_rate | 0.5275 |
| sharpe_ratio | -0.5780 |
| sortino_ratio | -0.2104 |
| max_drawdown | 0.4280 |
| cagr | -0.0997 |
| net_avg_win | 98.9298 |
| net_avg_loss | -118.1365 |
| avg_hold_time_bars | 15.4867 |
| exposure | 0.4484 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
