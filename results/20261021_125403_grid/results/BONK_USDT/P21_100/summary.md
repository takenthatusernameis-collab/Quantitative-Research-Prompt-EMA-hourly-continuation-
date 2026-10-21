# EMA Hourly Continuation — BONK/USDT P21_100

**Symbol:** BONK/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 414 |
| net_profit_factor | 0.8440 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 0.9890 |
| gross_win_rate | 0.5024 |
| sharpe_ratio | -1.0250 |
| sortino_ratio | -0.2984 |
| max_drawdown | 0.4426 |
| cagr | -0.1310 |
| net_avg_win | 77.6401 |
| net_avg_loss | -91.9915 |
| avg_hold_time_bars | 21.8575 |
| exposure | 0.4113 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
