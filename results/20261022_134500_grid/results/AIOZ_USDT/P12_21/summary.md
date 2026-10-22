# EMA Hourly Continuation — AIOZ/USDT P12_21

**Symbol:** AIOZ/USDT  |  **P_fast:** 12  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1558 |
| net_profit_factor | 0.4114 |
| net_win_rate | 0.3941 |
| gross_profit_factor | 0.8520 |
| gross_win_rate | 0.4153 |
| sharpe_ratio | -13.3138 |
| sortino_ratio | -7.4190 |
| max_drawdown | 0.9999 |
| cagr | -0.9780 |
| net_avg_win | 11.3839 |
| net_avg_loss | -17.9968 |
| avg_hold_time_bars | 2.2875 |
| exposure | 0.1620 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
