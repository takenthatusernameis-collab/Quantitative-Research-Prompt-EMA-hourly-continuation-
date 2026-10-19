# EMA Hourly Continuation — NEAR/USDT P50_100

**Symbol:** NEAR/USDT  |  **P_fast:** 50  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 597 |
| net_profit_factor | 0.5413 |
| net_win_rate | 0.4690 |
| gross_profit_factor | 0.9072 |
| gross_win_rate | 0.4740 |
| sharpe_ratio | -4.5601 |
| sortino_ratio | -1.5652 |
| max_drawdown | 0.8571 |
| cagr | -0.5352 |
| net_avg_win | 35.9858 |
| net_avg_loss | -58.7246 |
| avg_hold_time_bars | 5.4171 |
| exposure | 0.1470 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
