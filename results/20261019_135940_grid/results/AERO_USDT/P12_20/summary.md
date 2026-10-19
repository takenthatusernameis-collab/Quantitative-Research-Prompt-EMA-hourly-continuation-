# EMA Hourly Continuation — AERO/USDT P12_20

**Symbol:** AERO/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1420 |
| net_profit_factor | 0.2516 |
| net_win_rate | 0.4035 |
| gross_profit_factor | 0.5840 |
| gross_win_rate | 0.4359 |
| sharpe_ratio | -12.5819 |
| sortino_ratio | -6.7079 |
| max_drawdown | 0.9998 |
| cagr | -0.9694 |
| net_avg_win | 5.8655 |
| net_avg_loss | -15.7726 |
| avg_hold_time_bars | 2.1563 |
| exposure | 0.1392 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
