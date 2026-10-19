# EMA Hourly Continuation — CHZ/USDT P20_21

**Symbol:** CHZ/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1252 |
| net_profit_factor | 0.1813 |
| net_win_rate | 0.2883 |
| gross_profit_factor | 0.7768 |
| gross_win_rate | 0.3698 |
| sharpe_ratio | -18.6884 |
| sortino_ratio | -10.1695 |
| max_drawdown | 1.0000 |
| cagr | -0.9967 |
| net_avg_win | 6.1347 |
| net_avg_loss | -13.7089 |
| avg_hold_time_bars | 1.7181 |
| exposure | 0.0978 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
