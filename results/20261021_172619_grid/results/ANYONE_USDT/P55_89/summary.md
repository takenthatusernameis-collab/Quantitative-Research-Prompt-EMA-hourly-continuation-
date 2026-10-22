# EMA Hourly Continuation — ANYONE/USDT P55_89

**Symbol:** ANYONE/USDT  |  **P_fast:** 55  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 280 |
| net_profit_factor | 0.6704 |
| net_win_rate | 0.4536 |
| gross_profit_factor | 0.8198 |
| gross_win_rate | 0.4536 |
| sharpe_ratio | -2.1661 |
| sortino_ratio | -0.5424 |
| max_drawdown | 0.4416 |
| cagr | -0.2210 |
| net_avg_win | 69.0497 |
| net_avg_loss | -85.4934 |
| avg_hold_time_bars | 6.8321 |
| exposure | 0.0967 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
