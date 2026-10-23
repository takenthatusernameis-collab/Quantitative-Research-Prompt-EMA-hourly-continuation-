# EMA Hourly Continuation — ALEX/USDT P50_55

**Symbol:** ALEX/USDT  |  **P_fast:** 50  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 712 |
| net_profit_factor | 0.2219 |
| net_win_rate | 0.2781 |
| gross_profit_factor | 0.7298 |
| gross_win_rate | 0.3329 |
| sharpe_ratio | -12.6978 |
| sortino_ratio | -4.9654 |
| max_drawdown | 0.9989 |
| cagr | -0.9331 |
| net_avg_win | 14.3834 |
| net_avg_loss | -24.9741 |
| avg_hold_time_bars | 3.6713 |
| exposure | 0.1188 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
