# EMA Hourly Continuation — BOME/USDT P12_200

**Symbol:** BOME/USDT  |  **P_fast:** 12  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.7651 |
| net_win_rate | 0.4752 |
| gross_profit_factor | 0.8832 |
| gross_win_rate | 0.4752 |
| sharpe_ratio | -1.4208 |
| sortino_ratio | -0.3620 |
| max_drawdown | 0.3763 |
| cagr | -0.1545 |
| net_avg_win | 73.2113 |
| net_avg_loss | -86.6293 |
| avg_hold_time_bars | 49.2640 |
| exposure | 0.7210 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
