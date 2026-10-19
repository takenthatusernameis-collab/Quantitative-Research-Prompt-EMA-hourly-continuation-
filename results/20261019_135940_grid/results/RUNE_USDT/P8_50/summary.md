# EMA Hourly Continuation — RUNE/USDT P8_50

**Symbol:** RUNE/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1066 |
| net_profit_factor | 0.6440 |
| net_win_rate | 0.4887 |
| gross_profit_factor | 1.0834 |
| gross_win_rate | 0.4972 |
| sharpe_ratio | -5.8741 |
| sortino_ratio | -2.6751 |
| max_drawdown | 0.9651 |
| cagr | -0.7332 |
| net_avg_win | 33.4617 |
| net_avg_loss | -49.6719 |
| avg_hold_time_bars | 9.5835 |
| exposure | 0.4644 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
