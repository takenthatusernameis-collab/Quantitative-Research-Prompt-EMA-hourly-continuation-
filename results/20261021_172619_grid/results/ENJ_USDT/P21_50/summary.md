# EMA Hourly Continuation — ENJ/USDT P21_50

**Symbol:** ENJ/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 513 |
| net_profit_factor | 0.7533 |
| net_win_rate | 0.5049 |
| gross_profit_factor | 1.0344 |
| gross_win_rate | 0.5068 |
| sharpe_ratio | -2.1156 |
| sortino_ratio | -0.6858 |
| max_drawdown | 0.5827 |
| cagr | -0.2698 |
| net_avg_win | 64.5628 |
| net_avg_loss | -87.3918 |
| avg_hold_time_bars | 6.8441 |
| exposure | 0.1589 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
