# EMA Hourly Continuation — SYN/USDT P26_200

**Symbol:** SYN/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 293 |
| net_profit_factor | 0.9780 |
| net_win_rate | 0.5324 |
| gross_profit_factor | 1.1289 |
| gross_win_rate | 0.5324 |
| sharpe_ratio | -0.0631 |
| sortino_ratio | -0.0156 |
| max_drawdown | 0.1712 |
| cagr | -0.0126 |
| net_avg_win | 89.2364 |
| net_avg_loss | -103.9007 |
| avg_hold_time_bars | 46.4573 |
| exposure | 0.6187 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
