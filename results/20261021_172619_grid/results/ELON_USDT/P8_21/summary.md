# EMA Hourly Continuation — ELON/USDT P8_21

**Symbol:** ELON/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 487 |
| net_profit_factor | 0.6523 |
| net_win_rate | 0.4764 |
| gross_profit_factor | 0.9017 |
| gross_win_rate | 0.4764 |
| sharpe_ratio | -3.0172 |
| sortino_ratio | -0.9531 |
| max_drawdown | 0.6801 |
| cagr | -0.3541 |
| net_avg_win | 53.8906 |
| net_avg_loss | -75.1644 |
| avg_hold_time_bars | 5.9343 |
| exposure | 0.1314 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
