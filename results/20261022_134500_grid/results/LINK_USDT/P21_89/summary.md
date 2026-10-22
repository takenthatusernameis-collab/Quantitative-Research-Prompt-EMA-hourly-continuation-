# EMA Hourly Continuation — LINK/USDT P21_89

**Symbol:** LINK/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 677 |
| net_profit_factor | 0.5839 |
| net_win_rate | 0.4520 |
| gross_profit_factor | 0.9297 |
| gross_win_rate | 0.4638 |
| sharpe_ratio | -5.2940 |
| sortino_ratio | -1.9309 |
| max_drawdown | 0.9094 |
| cagr | -0.6100 |
| net_avg_win | 41.5480 |
| net_avg_loss | -58.6894 |
| avg_hold_time_bars | 11.2024 |
| exposure | 0.3447 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
