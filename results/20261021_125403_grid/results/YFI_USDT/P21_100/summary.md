# EMA Hourly Continuation — YFI/USDT P21_100

**Symbol:** YFI/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 556 |
| net_profit_factor | 0.6670 |
| net_win_rate | 0.4730 |
| gross_profit_factor | 0.9334 |
| gross_win_rate | 0.4730 |
| sharpe_ratio | -3.2813 |
| sortino_ratio | -1.1017 |
| max_drawdown | 0.7308 |
| cagr | -0.3987 |
| net_avg_win | 55.0461 |
| net_avg_loss | -74.0792 |
| avg_hold_time_bars | 15.5522 |
| exposure | 0.3913 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
