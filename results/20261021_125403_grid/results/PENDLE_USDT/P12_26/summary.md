# EMA Hourly Continuation — PENDLE/USDT P12_26

**Symbol:** PENDLE/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.7091 |
| net_win_rate | 0.4793 |
| gross_profit_factor | 0.9327 |
| gross_win_rate | 0.4793 |
| sharpe_ratio | -2.4952 |
| sortino_ratio | -0.7829 |
| max_drawdown | 0.6239 |
| cagr | -0.3011 |
| net_avg_win | 62.6155 |
| net_avg_loss | -81.2634 |
| avg_hold_time_bars | 5.7427 |
| exposure | 0.1258 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
