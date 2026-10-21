# EMA Hourly Continuation — LUNC/USDT P21_200

**Symbol:** LUNC/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.8002 |
| net_win_rate | 0.5039 |
| gross_profit_factor | 0.9990 |
| gross_win_rate | 0.5039 |
| sharpe_ratio | -1.3107 |
| sortino_ratio | -0.3669 |
| max_drawdown | 0.3878 |
| cagr | -0.1568 |
| net_avg_win | 72.2865 |
| net_avg_loss | -91.7672 |
| avg_hold_time_bars | 31.0836 |
| exposure | 0.5411 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
