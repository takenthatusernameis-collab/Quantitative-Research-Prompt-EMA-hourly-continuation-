# EMA Hourly Continuation — TURBO/USDT P26_50

**Symbol:** TURBO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 814 |
| net_profit_factor | 0.5885 |
| net_win_rate | 0.4730 |
| gross_profit_factor | 0.9818 |
| gross_win_rate | 0.4902 |
| sharpe_ratio | -6.1664 |
| sortino_ratio | -2.7149 |
| max_drawdown | 0.9409 |
| cagr | -0.7329 |
| net_avg_win | 34.7949 |
| net_avg_loss | -53.0639 |
| avg_hold_time_bars | 3.6130 |
| exposure | 0.1604 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
