# EMA Hourly Continuation — CFG/USDT P34_100

**Symbol:** CFG/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 442 |
| net_profit_factor | 0.8331 |
| net_win_rate | 0.5045 |
| gross_profit_factor | 1.0195 |
| gross_win_rate | 0.5045 |
| sharpe_ratio | -1.1754 |
| sortino_ratio | -0.3542 |
| max_drawdown | 0.4318 |
| cagr | -0.1519 |
| net_avg_win | 75.8132 |
| net_avg_loss | -92.6659 |
| avg_hold_time_bars | 11.9321 |
| exposure | 0.2397 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
