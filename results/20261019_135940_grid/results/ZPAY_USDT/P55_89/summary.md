# EMA Hourly Continuation — ZPAY/USDT P55_89

**Symbol:** ZPAY/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 647 |
| net_profit_factor | 0.3856 |
| net_win_rate | 0.3478 |
| gross_profit_factor | 0.5938 |
| gross_win_rate | 0.3509 |
| sharpe_ratio | -7.3332 |
| sortino_ratio | -2.6148 |
| max_drawdown | 0.9578 |
| cagr | -0.7107 |
| net_avg_win | 26.6682 |
| net_avg_loss | -36.8778 |
| avg_hold_time_bars | 8.9923 |
| exposure | 0.2633 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
