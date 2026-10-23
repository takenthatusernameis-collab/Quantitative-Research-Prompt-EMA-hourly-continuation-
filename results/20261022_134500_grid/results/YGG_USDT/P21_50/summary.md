# EMA Hourly Continuation — YGG/USDT P21_50

**Symbol:** YGG/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1007 |
| net_profit_factor | 0.5768 |
| net_win_rate | 0.4588 |
| gross_profit_factor | 0.9301 |
| gross_win_rate | 0.4717 |
| sharpe_ratio | -6.4451 |
| sortino_ratio | -2.8716 |
| max_drawdown | 0.9712 |
| cagr | -0.7507 |
| net_avg_win | 28.6148 |
| net_avg_loss | -42.0538 |
| avg_hold_time_bars | 4.4171 |
| exposure | 0.2013 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
