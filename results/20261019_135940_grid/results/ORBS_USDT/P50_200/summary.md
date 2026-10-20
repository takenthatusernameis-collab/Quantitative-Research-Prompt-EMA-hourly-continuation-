# EMA Hourly Continuation — ORBS/USDT P50_200

**Symbol:** ORBS/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 408 |
| net_profit_factor | 0.6150 |
| net_win_rate | 0.4412 |
| gross_profit_factor | 0.9231 |
| gross_win_rate | 0.4510 |
| sharpe_ratio | -3.8285 |
| sortino_ratio | -1.0904 |
| max_drawdown | 0.7364 |
| cagr | -0.4068 |
| net_avg_win | 64.8206 |
| net_avg_loss | -83.2161 |
| avg_hold_time_bars | 23.4755 |
| exposure | 0.4354 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
