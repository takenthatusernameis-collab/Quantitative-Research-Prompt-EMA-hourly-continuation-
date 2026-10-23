# EMA Hourly Continuation — BAND/USDT P21_50

**Symbol:** BAND/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 914 |
| net_profit_factor | 0.5651 |
| net_win_rate | 0.4639 |
| gross_profit_factor | 1.0135 |
| gross_win_rate | 0.4803 |
| sharpe_ratio | -6.3264 |
| sortino_ratio | -2.6886 |
| max_drawdown | 0.9634 |
| cagr | -0.7298 |
| net_avg_win | 29.5143 |
| net_avg_loss | -45.1949 |
| avg_hold_time_bars | 5.7035 |
| exposure | 0.2359 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
