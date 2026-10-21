# EMA Hourly Continuation — APE/USDT P8_21

**Symbol:** APE/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 525 |
| net_profit_factor | 0.6728 |
| net_win_rate | 0.4800 |
| gross_profit_factor | 0.9187 |
| gross_win_rate | 0.4800 |
| sharpe_ratio | -2.8405 |
| sortino_ratio | -0.9314 |
| max_drawdown | 0.6730 |
| cagr | -0.3473 |
| net_avg_win | 53.6564 |
| net_avg_loss | -73.6135 |
| avg_hold_time_bars | 5.5810 |
| exposure | 0.1332 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
