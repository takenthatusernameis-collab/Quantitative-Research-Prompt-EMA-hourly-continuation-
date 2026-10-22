# EMA Hourly Continuation — AXS/USDT P21_144

**Symbol:** AXS/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 431 |
| net_profit_factor | 0.7211 |
| net_win_rate | 0.4988 |
| gross_profit_factor | 1.0335 |
| gross_win_rate | 0.5081 |
| sharpe_ratio | -2.2363 |
| sortino_ratio | -0.6496 |
| max_drawdown | 0.5826 |
| cagr | -0.2694 |
| net_avg_win | 65.7776 |
| net_avg_loss | -90.7973 |
| avg_hold_time_bars | 28.2993 |
| exposure | 0.5519 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
