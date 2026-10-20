# EMA Hourly Continuation — CATI/USDT P20_200

**Symbol:** CATI/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 342 |
| net_profit_factor | 0.4544 |
| net_win_rate | 0.3918 |
| gross_profit_factor | 0.6996 |
| gross_win_rate | 0.4152 |
| sharpe_ratio | -5.0889 |
| sortino_ratio | -1.4402 |
| max_drawdown | 0.7927 |
| cagr | -0.5079 |
| net_avg_win | 47.9630 |
| net_avg_loss | -67.9944 |
| avg_hold_time_bars | 36.0702 |
| exposure | 0.6762 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
