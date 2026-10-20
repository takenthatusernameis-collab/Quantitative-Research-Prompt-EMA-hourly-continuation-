# EMA Hourly Continuation — EGLD/USDT P34_100

**Symbol:** EGLD/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 595 |
| net_profit_factor | 0.5413 |
| net_win_rate | 0.4773 |
| gross_profit_factor | 0.9425 |
| gross_win_rate | 0.4924 |
| sharpe_ratio | -4.2603 |
| sortino_ratio | -1.4616 |
| max_drawdown | 0.8422 |
| cagr | -0.5077 |
| net_avg_win | 34.5365 |
| net_avg_loss | -58.2676 |
| avg_hold_time_bars | 10.8504 |
| exposure | 0.2935 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
