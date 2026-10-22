# EMA Hourly Continuation — BONK/USDT P26_34

**Symbol:** BONK/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1036 |
| net_profit_factor | 0.3675 |
| net_win_rate | 0.3967 |
| gross_profit_factor | 0.7655 |
| gross_win_rate | 0.4189 |
| sharpe_ratio | -11.3001 |
| sortino_ratio | -5.1743 |
| max_drawdown | 0.9990 |
| cagr | -0.9355 |
| net_avg_win | 14.1213 |
| net_avg_loss | -25.2698 |
| avg_hold_time_bars | 1.9160 |
| exposure | 0.0902 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
