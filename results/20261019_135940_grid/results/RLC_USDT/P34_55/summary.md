# EMA Hourly Continuation — RLC/USDT P34_55

**Symbol:** RLC/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 860 |
| net_profit_factor | 0.4162 |
| net_win_rate | 0.4430 |
| gross_profit_factor | 0.8350 |
| gross_win_rate | 0.4663 |
| sharpe_ratio | -7.8423 |
| sortino_ratio | -3.2571 |
| max_drawdown | 0.9833 |
| cagr | -0.8018 |
| net_avg_win | 18.3871 |
| net_avg_loss | -35.1435 |
| avg_hold_time_bars | 3.5651 |
| exposure | 0.1394 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
