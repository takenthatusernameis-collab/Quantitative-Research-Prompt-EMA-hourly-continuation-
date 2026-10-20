# EMA Hourly Continuation — GMX/USDT P21_26

**Symbol:** GMX/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1137 |
| net_profit_factor | 0.2352 |
| net_win_rate | 0.3703 |
| gross_profit_factor | 0.7960 |
| gross_win_rate | 0.4195 |
| sharpe_ratio | -13.2668 |
| sortino_ratio | -6.4623 |
| max_drawdown | 0.9998 |
| cagr | -0.9654 |
| net_avg_win | 7.3026 |
| net_avg_loss | -18.2573 |
| avg_hold_time_bars | 2.7318 |
| exposure | 0.1412 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
