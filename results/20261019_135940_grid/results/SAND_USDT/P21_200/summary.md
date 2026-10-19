# EMA Hourly Continuation — SAND/USDT P21_200

**Symbol:** SAND/USDT  |  **P_fast:** 21  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 282 |
| net_profit_factor | 0.6194 |
| net_win_rate | 0.4574 |
| gross_profit_factor | 0.8999 |
| gross_win_rate | 0.4681 |
| sharpe_ratio | -2.5810 |
| sortino_ratio | -0.6062 |
| max_drawdown | 0.5345 |
| cagr | -0.2528 |
| net_avg_win | 65.4606 |
| net_avg_loss | -89.1087 |
| avg_hold_time_bars | 54.6241 |
| exposure | 0.7002 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
