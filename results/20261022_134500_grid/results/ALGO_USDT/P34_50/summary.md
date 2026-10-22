# EMA Hourly Continuation — ALGO/USDT P34_50

**Symbol:** ALGO/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 863 |
| net_profit_factor | 0.3921 |
| net_win_rate | 0.4751 |
| gross_profit_factor | 0.9869 |
| gross_win_rate | 0.5064 |
| sharpe_ratio | -7.5932 |
| sortino_ratio | -3.1614 |
| max_drawdown | 0.9814 |
| cagr | -0.7920 |
| net_avg_win | 15.4242 |
| net_avg_loss | -35.6073 |
| avg_hold_time_bars | 2.4508 |
| exposure | 0.0961 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
