# EMA Hourly Continuation — METIS/USDT P20_200

**Symbol:** METIS/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 297 |
| net_profit_factor | 0.7421 |
| net_win_rate | 0.4646 |
| gross_profit_factor | 0.8743 |
| gross_win_rate | 0.4646 |
| sharpe_ratio | -1.6729 |
| sortino_ratio | -0.4090 |
| max_drawdown | 0.4157 |
| cagr | -0.1723 |
| net_avg_win | 78.8236 |
| net_avg_loss | -92.1913 |
| avg_hold_time_bars | 46.2626 |
| exposure | 0.6245 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
