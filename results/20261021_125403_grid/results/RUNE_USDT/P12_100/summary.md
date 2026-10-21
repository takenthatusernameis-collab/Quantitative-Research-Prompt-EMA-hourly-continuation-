# EMA Hourly Continuation — RUNE/USDT P12_100

**Symbol:** RUNE/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 362 |
| net_profit_factor | 0.7951 |
| net_win_rate | 0.4945 |
| gross_profit_factor | 0.9749 |
| gross_win_rate | 0.4945 |
| sharpe_ratio | -1.3891 |
| sortino_ratio | -0.3778 |
| max_drawdown | 0.4044 |
| cagr | -0.1607 |
| net_avg_win | 77.1683 |
| net_avg_loss | -94.9339 |
| avg_hold_time_bars | 39.6519 |
| exposure | 0.6525 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
