# EMA Hourly Continuation — ALGO/USDT P20_50

**Symbol:** ALGO/USDT  |  **P_fast:** 20  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 973 |
| net_profit_factor | 0.5180 |
| net_win_rate | 0.4872 |
| gross_profit_factor | 0.9773 |
| gross_win_rate | 0.5015 |
| sharpe_ratio | -6.0037 |
| sortino_ratio | -2.6350 |
| max_drawdown | 0.9616 |
| cagr | -0.7214 |
| net_avg_win | 21.7606 |
| net_avg_loss | -39.9013 |
| avg_hold_time_bars | 4.4440 |
| exposure | 0.1965 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
