# EMA Hourly Continuation — ID/USDT P21_26

**Symbol:** ID/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 329 |
| net_profit_factor | 0.5860 |
| net_win_rate | 0.4833 |
| gross_profit_factor | 0.9391 |
| gross_win_rate | 0.4833 |
| sharpe_ratio | -3.0058 |
| sortino_ratio | -0.7801 |
| max_drawdown | 0.5993 |
| cagr | -0.3019 |
| net_avg_win | 53.0607 |
| net_avg_loss | -84.6914 |
| avg_hold_time_bars | 4.6140 |
| exposure | 0.0687 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
