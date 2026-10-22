# EMA Hourly Continuation — ZPAY/USDT P100_144

**Symbol:** ZPAY/USDT  |  **P_fast:** 100  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 515 |
| net_profit_factor | 0.3945 |
| net_win_rate | 0.3612 |
| gross_profit_factor | 0.5731 |
| gross_win_rate | 0.3650 |
| sharpe_ratio | -5.9777 |
| sortino_ratio | -1.9030 |
| max_drawdown | 0.8948 |
| cagr | -0.5904 |
| net_avg_win | 31.3436 |
| net_avg_loss | -44.9168 |
| avg_hold_time_bars | 10.4563 |
| exposure | 0.2437 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
