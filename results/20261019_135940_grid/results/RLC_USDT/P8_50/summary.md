# EMA Hourly Continuation — RLC/USDT P8_50

**Symbol:** RLC/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1091 |
| net_profit_factor | 0.6334 |
| net_win_rate | 0.4675 |
| gross_profit_factor | 1.0058 |
| gross_win_rate | 0.4794 |
| sharpe_ratio | -5.9789 |
| sortino_ratio | -2.7692 |
| max_drawdown | 0.9682 |
| cagr | -0.7393 |
| net_avg_win | 32.7162 |
| net_avg_loss | -45.3419 |
| avg_hold_time_bars | 9.2612 |
| exposure | 0.4593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
