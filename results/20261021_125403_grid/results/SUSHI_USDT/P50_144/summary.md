# EMA Hourly Continuation — SUSHI/USDT P50_144

**Symbol:** SUSHI/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 382 |
| net_profit_factor | 0.7177 |
| net_win_rate | 0.4791 |
| gross_profit_factor | 0.9076 |
| gross_win_rate | 0.4791 |
| sharpe_ratio | -1.9617 |
| sortino_ratio | -0.5455 |
| max_drawdown | 0.5258 |
| cagr | -0.2225 |
| net_avg_win | 65.3006 |
| net_avg_loss | -83.6683 |
| avg_hold_time_bars | 15.5445 |
| exposure | 0.2687 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
