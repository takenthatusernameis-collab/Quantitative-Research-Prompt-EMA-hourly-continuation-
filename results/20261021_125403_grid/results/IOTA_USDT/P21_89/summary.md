# EMA Hourly Continuation — IOTA/USDT P21_89

**Symbol:** IOTA/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 505 |
| net_profit_factor | 0.7209 |
| net_win_rate | 0.4653 |
| gross_profit_factor | 0.9147 |
| gross_win_rate | 0.4653 |
| sharpe_ratio | -2.6737 |
| sortino_ratio | -0.8549 |
| max_drawdown | 0.6589 |
| cagr | -0.3252 |
| net_avg_win | 68.9745 |
| net_avg_loss | -83.2791 |
| avg_hold_time_bars | 14.6752 |
| exposure | 0.3369 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
