# EMA Hourly Continuation — ORBS/USDT P50_200

**Symbol:** ORBS/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 324 |
| net_profit_factor | 0.7669 |
| net_win_rate | 0.4907 |
| gross_profit_factor | 1.0060 |
| gross_win_rate | 0.4907 |
| sharpe_ratio | -1.7613 |
| sortino_ratio | -0.4530 |
| max_drawdown | 0.4997 |
| cagr | -0.1888 |
| net_avg_win | 84.5552 |
| net_avg_loss | -106.2506 |
| avg_hold_time_bars | 29.0247 |
| exposure | 0.4275 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
