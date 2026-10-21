# EMA Hourly Continuation — SWFTC/USDT P100_200

**Symbol:** SWFTC/USDT  |  **P_fast:** 100  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 232 |
| net_profit_factor | 0.7992 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0072 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -1.1236 |
| sortino_ratio | -0.2452 |
| max_drawdown | 0.3019 |
| cagr | -0.1071 |
| net_avg_win | 84.9404 |
| net_avg_loss | -106.2796 |
| avg_hold_time_bars | 14.6940 |
| exposure | 0.1550 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
