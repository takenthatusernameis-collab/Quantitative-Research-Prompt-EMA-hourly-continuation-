# EMA Hourly Continuation — AERO/USDT P50_89

**Symbol:** AERO/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 579 |
| net_profit_factor | 0.5030 |
| net_win_rate | 0.4594 |
| gross_profit_factor | 0.8527 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -4.8694 |
| sortino_ratio | -1.6287 |
| max_drawdown | 0.8721 |
| cagr | -0.5576 |
| net_avg_win | 33.1440 |
| net_avg_loss | -55.9953 |
| avg_hold_time_bars | 5.1451 |
| exposure | 0.1354 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
