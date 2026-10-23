# EMA Hourly Continuation — W/USDT P21_50

**Symbol:** W/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 971 |
| net_profit_factor | 0.5795 |
| net_win_rate | 0.4511 |
| gross_profit_factor | 0.9424 |
| gross_win_rate | 0.4604 |
| sharpe_ratio | -6.5830 |
| sortino_ratio | -2.8807 |
| max_drawdown | 0.9717 |
| cagr | -0.7560 |
| net_avg_win | 30.5593 |
| net_avg_loss | -43.3312 |
| avg_hold_time_bars | 4.7600 |
| exposure | 0.2101 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
