# EMA Hourly Continuation — LUNC/USDT P8_12

**Symbol:** LUNC/USDT  |  **P_fast:** 8  |  **P_slow:** 12

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 194 |
| net_profit_factor | 0.6676 |
| net_win_rate | 0.4948 |
| gross_profit_factor | 0.9738 |
| gross_win_rate | 0.4948 |
| sharpe_ratio | -1.7331 |
| sortino_ratio | -0.3473 |
| max_drawdown | 0.3820 |
| cagr | -0.1466 |
| net_avg_win | 68.6798 |
| net_avg_loss | -100.7833 |
| avg_hold_time_bars | 4.5361 |
| exposure | 0.0400 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
