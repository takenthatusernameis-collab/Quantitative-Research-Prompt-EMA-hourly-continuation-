# EMA Hourly Continuation — UNI/USDT P21_100

**Symbol:** UNI/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 634 |
| net_profit_factor | 0.6324 |
| net_win_rate | 0.4842 |
| gross_profit_factor | 0.9502 |
| gross_win_rate | 0.4858 |
| sharpe_ratio | -3.7821 |
| sortino_ratio | -1.3358 |
| max_drawdown | 0.8089 |
| cagr | -0.4765 |
| net_avg_win | 45.0050 |
| net_avg_loss | -66.8146 |
| avg_hold_time_bars | 14.0789 |
| exposure | 0.4057 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
