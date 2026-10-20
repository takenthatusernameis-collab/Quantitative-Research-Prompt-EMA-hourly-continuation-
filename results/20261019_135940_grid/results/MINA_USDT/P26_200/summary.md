# EMA Hourly Continuation — MINA/USDT P26_200

**Symbol:** MINA/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 366 |
| net_profit_factor | 0.7784 |
| net_win_rate | 0.5164 |
| gross_profit_factor | 1.0721 |
| gross_win_rate | 0.5219 |
| sharpe_ratio | -1.3831 |
| sortino_ratio | -0.3759 |
| max_drawdown | 0.4607 |
| cagr | -0.1633 |
| net_avg_win | 67.0953 |
| net_avg_loss | -92.0383 |
| avg_hold_time_bars | 36.2514 |
| exposure | 0.6031 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
