# EMA Hourly Continuation — IOST/USDT P12_89

**Symbol:** IOST/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 469 |
| net_profit_factor | 0.8977 |
| net_win_rate | 0.5394 |
| gross_profit_factor | 1.1599 |
| gross_win_rate | 0.5394 |
| sharpe_ratio | -0.6881 |
| sortino_ratio | -0.2154 |
| max_drawdown | 0.2784 |
| cagr | -0.0982 |
| net_avg_win | 79.2661 |
| net_avg_loss | -103.4299 |
| avg_hold_time_bars | 27.5736 |
| exposure | 0.5878 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
