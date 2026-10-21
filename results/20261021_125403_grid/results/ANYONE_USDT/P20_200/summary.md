# EMA Hourly Continuation — ANYONE/USDT P20_200

**Symbol:** ANYONE/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 241 |
| net_profit_factor | 0.9304 |
| net_win_rate | 0.5145 |
| gross_profit_factor | 1.0412 |
| gross_win_rate | 0.5145 |
| sharpe_ratio | -0.3121 |
| sortino_ratio | -0.0732 |
| max_drawdown | 0.1960 |
| cagr | -0.0370 |
| net_avg_win | 88.0590 |
| net_avg_loss | -100.3057 |
| avg_hold_time_bars | 54.7925 |
| exposure | 0.6673 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
