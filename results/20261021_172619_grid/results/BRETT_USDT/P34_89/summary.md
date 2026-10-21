# EMA Hourly Continuation — BRETT/USDT P34_89

**Symbol:** BRETT/USDT  |  **P_fast:** 34  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.7111 |
| net_win_rate | 0.4611 |
| gross_profit_factor | 0.8516 |
| gross_win_rate | 0.4611 |
| sharpe_ratio | -2.0819 |
| sortino_ratio | -0.5772 |
| max_drawdown | 0.4689 |
| cagr | -0.2341 |
| net_avg_win | 69.5444 |
| net_avg_loss | -83.6783 |
| avg_hold_time_bars | 12.2000 |
| exposure | 0.2113 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
