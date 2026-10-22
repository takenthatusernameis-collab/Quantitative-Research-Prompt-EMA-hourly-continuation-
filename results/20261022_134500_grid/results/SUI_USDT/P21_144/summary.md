# EMA Hourly Continuation — SUI/USDT P21_144

**Symbol:** SUI/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 518 |
| net_profit_factor | 0.6908 |
| net_win_rate | 0.4903 |
| gross_profit_factor | 0.9970 |
| gross_win_rate | 0.4961 |
| sharpe_ratio | -2.8139 |
| sortino_ratio | -0.9011 |
| max_drawdown | 0.6854 |
| cagr | -0.3512 |
| net_avg_win | 58.2728 |
| net_avg_loss | -81.1616 |
| avg_hold_time_bars | 21.0965 |
| exposure | 0.4967 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
