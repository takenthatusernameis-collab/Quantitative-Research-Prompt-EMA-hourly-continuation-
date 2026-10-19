# EMA Hourly Continuation — LINK/USDT P8_50

**Symbol:** LINK/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1077 |
| net_profit_factor | 0.6098 |
| net_win_rate | 0.4698 |
| gross_profit_factor | 1.0547 |
| gross_win_rate | 0.4838 |
| sharpe_ratio | -6.6943 |
| sortino_ratio | -3.0500 |
| max_drawdown | 0.9799 |
| cagr | -0.7842 |
| net_avg_win | 30.2303 |
| net_avg_loss | -43.9297 |
| avg_hold_time_bars | 9.0743 |
| exposure | 0.4442 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
