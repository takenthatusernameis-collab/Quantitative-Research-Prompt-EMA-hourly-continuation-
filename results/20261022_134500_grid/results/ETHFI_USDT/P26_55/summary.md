# EMA Hourly Continuation — ETHFI/USDT P26_55

**Symbol:** ETHFI/USDT  |  **P_fast:** 26  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 983 |
| net_profit_factor | 0.5688 |
| net_win_rate | 0.4578 |
| gross_profit_factor | 0.9398 |
| gross_win_rate | 0.4649 |
| sharpe_ratio | -6.3151 |
| sortino_ratio | -2.7959 |
| max_drawdown | 0.9678 |
| cagr | -0.7395 |
| net_avg_win | 28.3139 |
| net_avg_loss | -42.0265 |
| avg_hold_time_bars | 4.3052 |
| exposure | 0.1924 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
