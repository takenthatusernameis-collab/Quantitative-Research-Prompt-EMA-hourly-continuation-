# EMA Hourly Continuation — T/USDT P8_50

**Symbol:** T/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 882 |
| net_profit_factor | 0.6220 |
| net_win_rate | 0.4637 |
| gross_profit_factor | 0.9978 |
| gross_win_rate | 0.4785 |
| sharpe_ratio | -5.5335 |
| sortino_ratio | -2.3002 |
| max_drawdown | 0.9406 |
| cagr | -0.6719 |
| net_avg_win | 37.8061 |
| net_avg_loss | -52.5614 |
| avg_hold_time_bars | 11.4535 |
| exposure | 0.4571 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
