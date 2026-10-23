# EMA Hourly Continuation — CPOOL/USDT P55_200

**Symbol:** CPOOL/USDT  |  **P_fast:** 55  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 488 |
| net_profit_factor | 0.5526 |
| net_win_rate | 0.4160 |
| gross_profit_factor | 0.7559 |
| gross_win_rate | 0.4180 |
| sharpe_ratio | -4.6258 |
| sortino_ratio | -1.4254 |
| max_drawdown | 0.8321 |
| cagr | -0.4990 |
| net_avg_win | 50.1130 |
| net_avg_loss | -64.5982 |
| avg_hold_time_bars | 13.1516 |
| exposure | 0.2917 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
