# EMA Hourly Continuation — ALGO/USDT P8_34

**Symbol:** ALGO/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 698 |
| net_profit_factor | 0.8879 |
| net_win_rate | 0.5430 |
| gross_profit_factor | 1.1694 |
| gross_win_rate | 0.5430 |
| sharpe_ratio | -0.8679 |
| sortino_ratio | -0.3323 |
| max_drawdown | 0.3681 |
| cagr | -0.1467 |
| net_avg_win | 68.6887 |
| net_avg_loss | -91.9110 |
| avg_hold_time_bars | 8.5917 |
| exposure | 0.2726 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
