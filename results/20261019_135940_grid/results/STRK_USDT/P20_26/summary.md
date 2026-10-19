# EMA Hourly Continuation — STRK/USDT P20_26

**Symbol:** STRK/USDT  |  **P_fast:** 20  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1177 |
| net_profit_factor | 0.2486 |
| net_win_rate | 0.3713 |
| gross_profit_factor | 0.6553 |
| gross_win_rate | 0.3951 |
| sharpe_ratio | -13.5013 |
| sortino_ratio | -6.6946 |
| max_drawdown | 0.9998 |
| cagr | -0.9694 |
| net_avg_win | 7.5714 |
| net_avg_loss | -17.9826 |
| avg_hold_time_bars | 1.9533 |
| exposure | 0.1045 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
