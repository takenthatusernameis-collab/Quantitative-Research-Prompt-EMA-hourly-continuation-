# EMA Hourly Continuation — ETHFI/USDT P21_200

**Symbol:** ETHFI/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 365 |
| net_profit_factor | 0.7967 |
| net_win_rate | 0.4904 |
| gross_profit_factor | 0.9970 |
| gross_win_rate | 0.4932 |
| sharpe_ratio | -1.5391 |
| sortino_ratio | -0.4180 |
| max_drawdown | 0.4294 |
| cagr | -0.1778 |
| net_avg_win | 85.0317 |
| net_avg_loss | -102.7148 |
| avg_hold_time_bars | 38.8027 |
| exposure | 0.6438 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
