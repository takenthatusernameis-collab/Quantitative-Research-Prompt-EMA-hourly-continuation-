# EMA Hourly Continuation — COTI/USDT P20_100

**Symbol:** COTI/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 733 |
| net_profit_factor | 0.6899 |
| net_win_rate | 0.4980 |
| gross_profit_factor | 0.9889 |
| gross_win_rate | 0.5007 |
| sharpe_ratio | -3.1183 |
| sortino_ratio | -1.1933 |
| max_drawdown | 0.7687 |
| cagr | -0.4319 |
| net_avg_win | 46.2257 |
| net_avg_loss | -66.4551 |
| avg_hold_time_bars | 12.2879 |
| exposure | 0.4094 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
