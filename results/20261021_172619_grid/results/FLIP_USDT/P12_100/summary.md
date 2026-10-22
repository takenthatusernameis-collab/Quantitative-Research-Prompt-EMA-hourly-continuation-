# EMA Hourly Continuation — FLIP/USDT P12_100

**Symbol:** FLIP/USDT  |  **P_fast:** 12  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 386 |
| net_profit_factor | 0.7480 |
| net_win_rate | 0.4948 |
| gross_profit_factor | 0.9904 |
| gross_win_rate | 0.4974 |
| sharpe_ratio | -1.8611 |
| sortino_ratio | -0.5188 |
| max_drawdown | 0.4979 |
| cagr | -0.2151 |
| net_avg_win | 70.8445 |
| net_avg_loss | -92.7630 |
| avg_hold_time_bars | 35.5078 |
| exposure | 0.6230 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
