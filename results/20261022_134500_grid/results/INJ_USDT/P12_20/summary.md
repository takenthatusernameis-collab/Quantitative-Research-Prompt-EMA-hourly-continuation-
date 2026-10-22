# EMA Hourly Continuation — INJ/USDT P12_20

**Symbol:** INJ/USDT  |  **P_fast:** 12  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1530 |
| net_profit_factor | 0.3801 |
| net_win_rate | 0.4190 |
| gross_profit_factor | 0.8246 |
| gross_win_rate | 0.4392 |
| sharpe_ratio | -12.4537 |
| sortino_ratio | -6.9029 |
| max_drawdown | 0.9999 |
| cagr | -0.9714 |
| net_avg_win | 9.5642 |
| net_avg_loss | -18.1432 |
| avg_hold_time_bars | 2.2902 |
| exposure | 0.1593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
