# EMA Hourly Continuation — THETA/USDT P8_34

**Symbol:** THETA/USDT  |  **P_fast:** 8  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1387 |
| net_profit_factor | 0.5395 |
| net_win_rate | 0.4492 |
| gross_profit_factor | 0.9097 |
| gross_win_rate | 0.4607 |
| sharpe_ratio | -8.2515 |
| sortino_ratio | -4.3286 |
| max_drawdown | 0.9950 |
| cagr | -0.8786 |
| net_avg_win | 18.7074 |
| net_avg_loss | -28.2782 |
| avg_hold_time_bars | 5.1593 |
| exposure | 0.3253 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
