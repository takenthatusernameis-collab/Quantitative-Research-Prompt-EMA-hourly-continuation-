# EMA Hourly Continuation — MOVR/USDT P50_200

**Symbol:** MOVR/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 322 |
| net_profit_factor | 0.7090 |
| net_win_rate | 0.4627 |
| gross_profit_factor | 0.8626 |
| gross_win_rate | 0.4627 |
| sharpe_ratio | -1.8918 |
| sortino_ratio | -0.4817 |
| max_drawdown | 0.4694 |
| cagr | -0.1996 |
| net_avg_win | 70.0201 |
| net_avg_loss | -85.0604 |
| avg_hold_time_bars | 25.7484 |
| exposure | 0.3769 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
