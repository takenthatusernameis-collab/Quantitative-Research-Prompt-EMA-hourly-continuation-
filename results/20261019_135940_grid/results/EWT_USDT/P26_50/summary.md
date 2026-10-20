# EMA Hourly Continuation — EWT/USDT P26_50

**Symbol:** EWT/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 840 |
| net_profit_factor | 0.3906 |
| net_win_rate | 0.3940 |
| gross_profit_factor | 0.7251 |
| gross_win_rate | 0.3976 |
| sharpe_ratio | -9.3160 |
| sortino_ratio | -3.8192 |
| max_drawdown | 0.9926 |
| cagr | -0.8572 |
| net_avg_win | 19.2153 |
| net_avg_loss | -31.9937 |
| avg_hold_time_bars | 4.2917 |
| exposure | 0.1639 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
