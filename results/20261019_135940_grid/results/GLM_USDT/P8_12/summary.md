# EMA Hourly Continuation — GLM/USDT P8_12

**Symbol:** GLM/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1679 |
| net_profit_factor | 0.2594 |
| net_win_rate | 0.3806 |
| gross_profit_factor | 0.8528 |
| gross_win_rate | 0.4532 |
| sharpe_ratio | -15.9271 |
| sortino_ratio | -9.4256 |
| max_drawdown | 1.0000 |
| cagr | -0.9925 |
| net_avg_win | 5.4817 |
| net_avg_loss | -12.9834 |
| avg_hold_time_bars | 2.3609 |
| exposure | 0.1802 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
