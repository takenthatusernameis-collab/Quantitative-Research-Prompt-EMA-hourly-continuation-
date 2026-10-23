# EMA Hourly Continuation — GMX/USDT P21_100

**Symbol:** GMX/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 698 |
| net_profit_factor | 0.6236 |
| net_win_rate | 0.4685 |
| gross_profit_factor | 0.9611 |
| gross_win_rate | 0.4713 |
| sharpe_ratio | -4.4114 |
| sortino_ratio | -1.6418 |
| max_drawdown | 0.8647 |
| cagr | -0.5421 |
| net_avg_win | 43.5360 |
| net_avg_loss | -61.5366 |
| avg_hold_time_bars | 12.4785 |
| exposure | 0.3959 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
