# EMA Hourly Continuation — ZK/USDT P12_34

**Symbol:** ZK/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 608 |
| net_profit_factor | 0.7495 |
| net_win_rate | 0.4934 |
| gross_profit_factor | 0.9697 |
| gross_win_rate | 0.4934 |
| sharpe_ratio | -2.3528 |
| sortino_ratio | -0.8604 |
| max_drawdown | 0.6387 |
| cagr | -0.3260 |
| net_avg_win | 60.1320 |
| net_avg_loss | -78.1478 |
| avg_hold_time_bars | 6.5329 |
| exposure | 0.1937 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
