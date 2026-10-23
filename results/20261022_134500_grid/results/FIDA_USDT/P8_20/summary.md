# EMA Hourly Continuation — FIDA/USDT P8_20

**Symbol:** FIDA/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1493 |
| net_profit_factor | 0.3875 |
| net_win_rate | 0.4300 |
| gross_profit_factor | 0.7357 |
| gross_win_rate | 0.4454 |
| sharpe_ratio | -10.3975 |
| sortino_ratio | -5.6661 |
| max_drawdown | 0.9991 |
| cagr | -0.9383 |
| net_avg_win | 9.8453 |
| net_avg_loss | -19.1678 |
| avg_hold_time_bars | 3.7636 |
| exposure | 0.2543 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
