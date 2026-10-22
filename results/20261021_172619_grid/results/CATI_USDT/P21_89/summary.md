# EMA Hourly Continuation — CATI/USDT P21_89

**Symbol:** CATI/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 390 |
| net_profit_factor | 0.6769 |
| net_win_rate | 0.4667 |
| gross_profit_factor | 0.8369 |
| gross_win_rate | 0.4667 |
| sharpe_ratio | -2.4792 |
| sortino_ratio | -0.7639 |
| max_drawdown | 0.5715 |
| cagr | -0.2976 |
| net_avg_win | 59.9452 |
| net_avg_loss | -77.4918 |
| avg_hold_time_bars | 18.0051 |
| exposure | 0.3849 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
