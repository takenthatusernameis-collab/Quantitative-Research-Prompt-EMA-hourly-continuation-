# EMA Hourly Continuation — AXS/USDT P21_50

**Symbol:** AXS/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 465 |
| net_profit_factor | 0.8262 |
| net_win_rate | 0.5290 |
| gross_profit_factor | 1.1319 |
| gross_win_rate | 0.5290 |
| sharpe_ratio | -1.3439 |
| sortino_ratio | -0.4177 |
| max_drawdown | 0.4277 |
| cagr | -0.1748 |
| net_avg_win | 74.2603 |
| net_avg_loss | -100.9570 |
| avg_hold_time_bars | 7.6000 |
| exposure | 0.1599 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
