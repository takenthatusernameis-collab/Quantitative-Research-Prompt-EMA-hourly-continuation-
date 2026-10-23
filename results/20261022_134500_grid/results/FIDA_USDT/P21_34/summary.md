# EMA Hourly Continuation — FIDA/USDT P21_34

**Symbol:** FIDA/USDT  |  **P_fast:** 21  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1106 |
| net_profit_factor | 0.4215 |
| net_win_rate | 0.4250 |
| gross_profit_factor | 0.9223 |
| gross_win_rate | 0.4575 |
| sharpe_ratio | -9.3888 |
| sortino_ratio | -4.4217 |
| max_drawdown | 0.9960 |
| cagr | -0.8878 |
| net_avg_win | 15.4399 |
| net_avg_loss | -27.0702 |
| avg_hold_time_bars | 3.3174 |
| exposure | 0.1660 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
