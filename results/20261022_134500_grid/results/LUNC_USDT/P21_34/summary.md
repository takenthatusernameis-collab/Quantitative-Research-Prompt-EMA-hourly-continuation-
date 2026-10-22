# EMA Hourly Continuation — LUNC/USDT P21_34

**Symbol:** LUNC/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1214 |
| net_profit_factor | 0.2375 |
| net_win_rate | 0.3550 |
| gross_profit_factor | 0.6777 |
| gross_win_rate | 0.3954 |
| sharpe_ratio | -14.0419 |
| sortino_ratio | -7.0699 |
| max_drawdown | 0.9999 |
| cagr | -0.9743 |
| net_avg_win | 7.2264 |
| net_avg_loss | -16.7479 |
| avg_hold_time_bars | 2.3188 |
| exposure | 0.1280 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
