# EMA Hourly Continuation — ONDO/USDT P26_50

**Symbol:** ONDO/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 941 |
| net_profit_factor | 0.5075 |
| net_win_rate | 0.4570 |
| gross_profit_factor | 0.8964 |
| gross_win_rate | 0.4697 |
| sharpe_ratio | -6.9674 |
| sortino_ratio | -3.0207 |
| max_drawdown | 0.9763 |
| cagr | -0.7714 |
| net_avg_win | 23.3788 |
| net_avg_loss | -38.7614 |
| avg_hold_time_bars | 3.6174 |
| exposure | 0.1547 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
