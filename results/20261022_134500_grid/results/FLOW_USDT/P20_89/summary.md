# EMA Hourly Continuation — FLOW/USDT P20_89

**Symbol:** FLOW/USDT  |  **P_fast:** 20  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 686 |
| net_profit_factor | 0.5655 |
| net_win_rate | 0.4621 |
| gross_profit_factor | 0.8994 |
| gross_win_rate | 0.4665 |
| sharpe_ratio | -4.8645 |
| sortino_ratio | -1.7918 |
| max_drawdown | 0.8914 |
| cagr | -0.5782 |
| net_avg_win | 36.3568 |
| net_avg_loss | -55.2329 |
| avg_hold_time_bars | 13.3848 |
| exposure | 0.4174 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
