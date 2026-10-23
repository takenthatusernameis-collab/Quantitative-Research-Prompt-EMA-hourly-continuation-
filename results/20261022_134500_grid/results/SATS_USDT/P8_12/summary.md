# EMA Hourly Continuation — SATS/USDT P8_12

**Symbol:** SATS/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1395 |
| net_profit_factor | 0.3074 |
| net_win_rate | 0.4237 |
| gross_profit_factor | 0.7884 |
| gross_win_rate | 0.4480 |
| sharpe_ratio | -11.1865 |
| sortino_ratio | -5.8865 |
| max_drawdown | 0.9995 |
| cagr | -0.9490 |
| net_avg_win | 7.5041 |
| net_avg_loss | -17.9470 |
| avg_hold_time_bars | 2.2452 |
| exposure | 0.1417 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
