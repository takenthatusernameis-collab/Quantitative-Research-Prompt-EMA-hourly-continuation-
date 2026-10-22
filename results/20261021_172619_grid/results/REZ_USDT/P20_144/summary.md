# EMA Hourly Continuation — REZ/USDT P20_144

**Symbol:** REZ/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 370 |
| net_profit_factor | 1.0196 |
| net_win_rate | 0.5459 |
| gross_profit_factor | 1.1902 |
| gross_win_rate | 0.5459 |
| sharpe_ratio | 0.1879 |
| sortino_ratio | 0.0528 |
| max_drawdown | 0.1784 |
| cagr | 0.0156 |
| net_avg_win | 100.7731 |
| net_avg_loss | -118.8381 |
| avg_hold_time_bars | 32.0973 |
| exposure | 0.5479 |

Decision label: exploratory signal


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
