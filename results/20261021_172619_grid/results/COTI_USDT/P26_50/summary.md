# EMA Hourly Continuation — COTI/USDT P26_50

**Symbol:** COTI/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 388 |
| net_profit_factor | 0.7370 |
| net_win_rate | 0.4897 |
| gross_profit_factor | 0.9594 |
| gross_win_rate | 0.4897 |
| sharpe_ratio | -1.9129 |
| sortino_ratio | -0.5395 |
| max_drawdown | 0.5127 |
| cagr | -0.2192 |
| net_avg_win | 68.2552 |
| net_avg_loss | -88.8687 |
| avg_hold_time_bars | 5.8892 |
| exposure | 0.1039 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
