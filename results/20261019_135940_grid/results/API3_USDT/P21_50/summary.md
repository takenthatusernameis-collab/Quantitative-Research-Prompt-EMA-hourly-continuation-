# EMA Hourly Continuation — API3/USDT P21_50

**Symbol:** API3/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1023 |
| net_profit_factor | 0.5719 |
| net_win_rate | 0.4477 |
| gross_profit_factor | 0.9698 |
| gross_win_rate | 0.4682 |
| sharpe_ratio | -7.0499 |
| sortino_ratio | -3.1865 |
| max_drawdown | 0.9796 |
| cagr | -0.7849 |
| net_avg_win | 28.5507 |
| net_avg_loss | -40.4697 |
| avg_hold_time_bars | 4.5914 |
| exposure | 0.2135 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
