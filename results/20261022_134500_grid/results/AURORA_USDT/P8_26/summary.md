# EMA Hourly Continuation — AURORA/USDT P8_26

**Symbol:** AURORA/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1344 |
| net_profit_factor | 0.4286 |
| net_win_rate | 0.3876 |
| gross_profit_factor | 0.8953 |
| gross_win_rate | 0.4152 |
| sharpe_ratio | -12.5302 |
| sortino_ratio | -6.4847 |
| max_drawdown | 0.9998 |
| cagr | -0.9663 |
| net_avg_win | 14.3936 |
| net_avg_loss | -21.2601 |
| avg_hold_time_bars | 4.6049 |
| exposure | 0.2813 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
