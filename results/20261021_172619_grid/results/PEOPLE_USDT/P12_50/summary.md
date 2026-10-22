# EMA Hourly Continuation — PEOPLE/USDT P12_50

**Symbol:** PEOPLE/USDT  |  **P_fast:** 12  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 662 |
| net_profit_factor | 0.6561 |
| net_win_rate | 0.4441 |
| gross_profit_factor | 0.8085 |
| gross_win_rate | 0.4441 |
| sharpe_ratio | -3.6800 |
| sortino_ratio | -1.3392 |
| max_drawdown | 0.7967 |
| cagr | -0.4604 |
| net_avg_win | 51.2085 |
| net_avg_loss | -62.3534 |
| avg_hold_time_bars | 11.6178 |
| exposure | 0.3480 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
