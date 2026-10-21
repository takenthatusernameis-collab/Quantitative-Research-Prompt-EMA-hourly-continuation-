# EMA Hourly Continuation — JTO/USDT P21_55

**Symbol:** JTO/USDT  |  **P_fast:** 21  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 560 |
| net_profit_factor | 0.7581 |
| net_win_rate | 0.4839 |
| gross_profit_factor | 0.9506 |
| gross_win_rate | 0.4839 |
| sharpe_ratio | -2.1698 |
| sortino_ratio | -0.7333 |
| max_drawdown | 0.5898 |
| cagr | -0.2869 |
| net_avg_win | 66.1706 |
| net_avg_loss | -81.8484 |
| avg_hold_time_bars | 8.5268 |
| exposure | 0.2170 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
