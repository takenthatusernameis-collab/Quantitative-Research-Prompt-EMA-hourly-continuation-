# EMA Hourly Continuation — BAND/USDT P20_200

**Symbol:** BAND/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 312 |
| net_profit_factor | 0.8081 |
| net_win_rate | 0.4968 |
| gross_profit_factor | 0.9758 |
| gross_win_rate | 0.4968 |
| sharpe_ratio | -1.1603 |
| sortino_ratio | -0.2918 |
| max_drawdown | 0.3376 |
| cagr | -0.1271 |
| net_avg_win | 78.8338 |
| net_avg_loss | -96.3139 |
| avg_hold_time_bars | 45.7468 |
| exposure | 0.6459 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
