# EMA Hourly Continuation — ORDI/USDT P26_200

**Symbol:** ORDI/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 354 |
| net_profit_factor | 0.8282 |
| net_win_rate | 0.4915 |
| gross_profit_factor | 0.9714 |
| gross_win_rate | 0.4915 |
| sharpe_ratio | -1.1381 |
| sortino_ratio | -0.3058 |
| max_drawdown | 0.3457 |
| cagr | -0.1328 |
| net_avg_win | 83.2884 |
| net_avg_loss | -97.2183 |
| avg_hold_time_bars | 31.5960 |
| exposure | 0.5084 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
