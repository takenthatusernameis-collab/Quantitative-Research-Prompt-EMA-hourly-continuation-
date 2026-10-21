# EMA Hourly Continuation — T/USDT P34_55

**Symbol:** T/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 460 |
| net_profit_factor | 0.6047 |
| net_win_rate | 0.4891 |
| gross_profit_factor | 0.9802 |
| gross_win_rate | 0.4913 |
| sharpe_ratio | -3.5145 |
| sortino_ratio | -1.0795 |
| max_drawdown | 0.7261 |
| cagr | -0.3909 |
| net_avg_win | 48.5219 |
| net_avg_loss | -76.8256 |
| avg_hold_time_bars | 6.7826 |
| exposure | 0.1412 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
