# EMA Hourly Continuation — KMNO/USDT P8_21

**Symbol:** KMNO/USDT  |  **P_fast:** 8  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1353 |
| net_profit_factor | 0.4537 |
| net_win_rate | 0.4383 |
| gross_profit_factor | 0.8814 |
| gross_win_rate | 0.4619 |
| sharpe_ratio | -9.6954 |
| sortino_ratio | -5.0318 |
| max_drawdown | 0.9982 |
| cagr | -0.9224 |
| net_avg_win | 13.9793 |
| net_avg_loss | -24.0417 |
| avg_hold_time_bars | 3.5455 |
| exposure | 0.2215 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
