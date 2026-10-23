# EMA Hourly Continuation — EDU/USDT P12_55

**Symbol:** EDU/USDT  |  **P_fast:** 12  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1091 |
| net_profit_factor | 0.5594 |
| net_win_rate | 0.4546 |
| gross_profit_factor | 0.8275 |
| gross_win_rate | 0.4592 |
| sharpe_ratio | -5.8632 |
| sortino_ratio | -2.7270 |
| max_drawdown | 0.9636 |
| cagr | -0.7264 |
| net_avg_win | 24.6239 |
| net_avg_loss | -36.6942 |
| avg_hold_time_bars | 7.6453 |
| exposure | 0.3774 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
