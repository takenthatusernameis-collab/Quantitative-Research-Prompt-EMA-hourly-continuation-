# EMA Hourly Continuation — CFX/USDT P12_50

**Symbol:** CFX/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 588 |
| net_profit_factor | 0.6963 |
| net_win_rate | 0.4694 |
| gross_profit_factor | 0.8853 |
| gross_win_rate | 0.4694 |
| sharpe_ratio | -2.8432 |
| sortino_ratio | -0.9824 |
| max_drawdown | 0.7003 |
| cagr | -0.3630 |
| net_avg_win | 56.3014 |
| net_avg_loss | -71.5293 |
| avg_hold_time_bars | 11.9439 |
| exposure | 0.3192 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
