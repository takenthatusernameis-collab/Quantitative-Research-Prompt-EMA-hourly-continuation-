# EMA Hourly Continuation — AIOZ/USDT P8_26

**Symbol:** AIOZ/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1612 |
| net_profit_factor | 0.5156 |
| net_win_rate | 0.4355 |
| gross_profit_factor | 0.8484 |
| gross_win_rate | 0.4485 |
| sharpe_ratio | -9.9970 |
| sortino_ratio | -5.5989 |
| max_drawdown | 0.9991 |
| cagr | -0.9391 |
| net_avg_win | 15.1489 |
| net_avg_loss | -22.6655 |
| avg_hold_time_bars | 3.7612 |
| exposure | 0.2756 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
