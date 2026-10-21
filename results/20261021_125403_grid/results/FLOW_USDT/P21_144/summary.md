# EMA Hourly Continuation — FLOW/USDT P21_144

**Symbol:** FLOW/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 350 |
| net_profit_factor | 0.7512 |
| net_win_rate | 0.4800 |
| gross_profit_factor | 0.9230 |
| gross_win_rate | 0.4800 |
| sharpe_ratio | -1.7095 |
| sortino_ratio | -0.4552 |
| max_drawdown | 0.4169 |
| cagr | -0.1897 |
| net_avg_win | 73.7549 |
| net_avg_loss | -90.6305 |
| avg_hold_time_bars | 34.3114 |
| exposure | 0.5459 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
