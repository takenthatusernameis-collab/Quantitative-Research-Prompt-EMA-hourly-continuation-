# EMA Hourly Continuation — RENDER/USDT P26_34

**Symbol:** RENDER/USDT  |  **P_fast:** 26  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 136 |
| net_profit_factor | 0.6127 |
| net_win_rate | 0.4485 |
| gross_profit_factor | 0.8189 |
| gross_win_rate | 0.4485 |
| sharpe_ratio | -1.9332 |
| sortino_ratio | -0.3459 |
| max_drawdown | 0.3020 |
| cagr | -0.1463 |
| net_avg_win | 75.1277 |
| net_avg_loss | -99.7340 |
| avg_hold_time_bars | 5.2868 |
| exposure | 0.0379 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
