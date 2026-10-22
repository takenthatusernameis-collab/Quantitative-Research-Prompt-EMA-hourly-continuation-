# EMA Hourly Continuation — JASMY/USDT P26_50

**Symbol:** JASMY/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 964 |
| net_profit_factor | 0.4872 |
| net_win_rate | 0.4481 |
| gross_profit_factor | 0.8694 |
| gross_win_rate | 0.4658 |
| sharpe_ratio | -7.4562 |
| sortino_ratio | -3.2856 |
| max_drawdown | 0.9820 |
| cagr | -0.7966 |
| net_avg_win | 21.5860 |
| net_avg_loss | -35.9810 |
| avg_hold_time_bars | 3.2199 |
| exposure | 0.1411 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
