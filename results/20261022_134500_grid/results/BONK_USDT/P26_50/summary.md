# EMA Hourly Continuation — BONK/USDT P26_50

**Symbol:** BONK/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 921 |
| net_profit_factor | 0.4945 |
| net_win_rate | 0.4658 |
| gross_profit_factor | 0.8514 |
| gross_win_rate | 0.4788 |
| sharpe_ratio | -6.4076 |
| sortino_ratio | -2.7321 |
| max_drawdown | 0.9672 |
| cagr | -0.7406 |
| net_avg_win | 22.0372 |
| net_avg_loss | -38.8548 |
| avg_hold_time_bars | 3.7047 |
| exposure | 0.1551 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
