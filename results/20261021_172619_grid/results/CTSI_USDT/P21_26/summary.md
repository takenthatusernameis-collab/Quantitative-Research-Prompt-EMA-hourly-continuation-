# EMA Hourly Continuation — CTSI/USDT P21_26

**Symbol:** CTSI/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.4824 |
| net_win_rate | 0.4130 |
| gross_profit_factor | 0.7412 |
| gross_win_rate | 0.4130 |
| sharpe_ratio | -4.3030 |
| sortino_ratio | -1.1053 |
| max_drawdown | 0.7215 |
| cagr | -0.3990 |
| net_avg_win | 50.5566 |
| net_avg_loss | -73.7533 |
| avg_hold_time_bars | 5.8416 |
| exposure | 0.0855 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
