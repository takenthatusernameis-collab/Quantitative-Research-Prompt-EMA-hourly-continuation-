# EMA Hourly Continuation — ALGO/USDT P50_100

**Symbol:** ALGO/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.5866 |
| net_win_rate | 0.5068 |
| gross_profit_factor | 1.0700 |
| gross_win_rate | 0.5169 |
| sharpe_ratio | -3.9055 |
| sortino_ratio | -1.3382 |
| max_drawdown | 0.8118 |
| cagr | -0.4769 |
| net_avg_win | 38.1407 |
| net_avg_loss | -66.8029 |
| avg_hold_time_bars | 5.7661 |
| exposure | 0.1546 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
