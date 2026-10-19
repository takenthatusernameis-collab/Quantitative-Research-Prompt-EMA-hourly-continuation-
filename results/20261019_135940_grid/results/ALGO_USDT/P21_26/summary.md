# EMA Hourly Continuation — ALGO/USDT P21_26

**Symbol:** ALGO/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1152 |
| net_profit_factor | 0.1921 |
| net_win_rate | 0.3689 |
| gross_profit_factor | 0.6802 |
| gross_win_rate | 0.4193 |
| sharpe_ratio | -14.2863 |
| sortino_ratio | -7.0490 |
| max_drawdown | 0.9999 |
| cagr | -0.9787 |
| net_avg_win | 5.5950 |
| net_avg_loss | -17.0251 |
| avg_hold_time_bars | 1.7674 |
| exposure | 0.0925 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
