# EMA Hourly Continuation — HBAR/USDT P55_100

**Symbol:** HBAR/USDT  |  **P_fast:** 55  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 290 |
| net_profit_factor | 0.7544 |
| net_win_rate | 0.5138 |
| gross_profit_factor | 1.0350 |
| gross_win_rate | 0.5138 |
| sharpe_ratio | -1.3962 |
| sortino_ratio | -0.3423 |
| max_drawdown | 0.3375 |
| cagr | -0.1448 |
| net_avg_win | 66.9652 |
| net_avg_loss | -93.8022 |
| avg_hold_time_bars | 7.9207 |
| exposure | 0.1044 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
