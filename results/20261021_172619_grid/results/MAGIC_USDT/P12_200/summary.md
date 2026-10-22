# EMA Hourly Continuation — MAGIC/USDT P12_200

**Symbol:** MAGIC/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 320 |
| net_profit_factor | 0.7845 |
| net_win_rate | 0.4750 |
| gross_profit_factor | 0.9305 |
| gross_win_rate | 0.4750 |
| sharpe_ratio | -1.5662 |
| sortino_ratio | -0.3985 |
| max_drawdown | 0.4980 |
| cagr | -0.1689 |
| net_avg_win | 88.9921 |
| net_avg_loss | -102.6374 |
| avg_hold_time_bars | 50.6125 |
| exposure | 0.7362 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
