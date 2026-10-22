# EMA Hourly Continuation — ETN/USDT P20_100

**Symbol:** ETN/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 395 |
| net_profit_factor | 0.5801 |
| net_win_rate | 0.4127 |
| gross_profit_factor | 0.7136 |
| gross_win_rate | 0.4127 |
| sharpe_ratio | -3.8445 |
| sortino_ratio | -1.1773 |
| max_drawdown | 0.6898 |
| cagr | -0.4201 |
| net_avg_win | 57.7813 |
| net_avg_loss | -69.9865 |
| avg_hold_time_bars | 16.4127 |
| exposure | 0.3521 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
