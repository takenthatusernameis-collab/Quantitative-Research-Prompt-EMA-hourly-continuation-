# EMA Hourly Continuation — POKT/USDT P34_200

**Symbol:** POKT/USDT  |  **P_fast:** 34  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.7690 |
| net_win_rate | 0.4750 |
| gross_profit_factor | 0.9284 |
| gross_win_rate | 0.4750 |
| sharpe_ratio | -1.7571 |
| sortino_ratio | -0.4726 |
| max_drawdown | 0.4849 |
| cagr | -0.1964 |
| net_avg_win | 82.5240 |
| net_avg_loss | -97.0986 |
| avg_hold_time_bars | 31.4722 |
| exposure | 0.5127 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
