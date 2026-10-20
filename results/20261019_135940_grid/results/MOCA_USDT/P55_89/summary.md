# EMA Hourly Continuation — MOCA/USDT P55_89

**Symbol:** MOCA/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 590 |
| net_profit_factor | 0.4205 |
| net_win_rate | 0.4169 |
| gross_profit_factor | 0.7270 |
| gross_win_rate | 0.4339 |
| sharpe_ratio | -7.1095 |
| sortino_ratio | -2.5442 |
| max_drawdown | 0.9484 |
| cagr | -0.7243 |
| net_avg_win | 27.9292 |
| net_avg_loss | -47.4963 |
| avg_hold_time_bars | 4.2763 |
| exposure | 0.1265 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
