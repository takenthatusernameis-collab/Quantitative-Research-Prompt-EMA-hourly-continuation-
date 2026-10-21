# EMA Hourly Continuation — DOGE/USDT P55_200

**Symbol:** DOGE/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 279 |
| net_profit_factor | 0.9221 |
| net_win_rate | 0.5412 |
| gross_profit_factor | 1.1733 |
| gross_win_rate | 0.5412 |
| sharpe_ratio | -0.3766 |
| sortino_ratio | -0.0911 |
| max_drawdown | 0.2082 |
| cagr | -0.0441 |
| net_avg_win | 83.9103 |
| net_avg_loss | -107.3531 |
| avg_hold_time_bars | 26.1685 |
| exposure | 0.3319 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
