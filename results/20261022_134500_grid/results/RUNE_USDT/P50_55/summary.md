# EMA Hourly Continuation — RUNE/USDT P50_55

**Symbol:** RUNE/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 781 |
| net_profit_factor | 0.2435 |
| net_win_rate | 0.3688 |
| gross_profit_factor | 0.7908 |
| gross_win_rate | 0.4469 |
| sharpe_ratio | -11.5488 |
| sortino_ratio | -4.7367 |
| max_drawdown | 0.9984 |
| cagr | -0.9234 |
| net_avg_win | 11.1557 |
| net_avg_loss | -26.7689 |
| avg_hold_time_bars | 1.9859 |
| exposure | 0.0705 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
