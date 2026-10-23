# EMA Hourly Continuation — AGLD/USDT P8_20

**Symbol:** AGLD/USDT  |  **P_fast:** 8  |  **P_slow:** 20

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1486 |
| net_profit_factor | 0.3824 |
| net_win_rate | 0.4280 |
| gross_profit_factor | 0.7933 |
| gross_win_rate | 0.4536 |
| sharpe_ratio | -10.0210 |
| sortino_ratio | -5.4513 |
| max_drawdown | 0.9987 |
| cagr | -0.9292 |
| net_avg_win | 9.7224 |
| net_avg_loss | -19.0246 |
| avg_hold_time_bars | 3.7584 |
| exposure | 0.2527 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
