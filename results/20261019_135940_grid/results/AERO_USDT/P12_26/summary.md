# EMA Hourly Continuation — AERO/USDT P12_26

**Symbol:** AERO/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1332 |
| net_profit_factor | 0.3727 |
| net_win_rate | 0.4459 |
| gross_profit_factor | 0.7216 |
| gross_win_rate | 0.4580 |
| sharpe_ratio | -9.4729 |
| sortino_ratio | -4.8643 |
| max_drawdown | 0.9979 |
| cagr | -0.9131 |
| net_avg_win | 9.9792 |
| net_avg_loss | -21.5528 |
| avg_hold_time_bars | 2.8761 |
| exposure | 0.1741 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
