# EMA Hourly Continuation — BDX/USDT P21_144

**Symbol:** BDX/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1045 |
| net_profit_factor | 0.3230 |
| net_win_rate | 0.3158 |
| gross_profit_factor | 0.7037 |
| gross_win_rate | 0.3608 |
| sharpe_ratio | -14.3240 |
| sortino_ratio | -6.7415 |
| max_drawdown | 0.9999 |
| cagr | -0.9736 |
| net_avg_win | 14.4536 |
| net_avg_loss | -20.6554 |
| avg_hold_time_bars | 8.2986 |
| exposure | 0.3942 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
