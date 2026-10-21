# EMA Hourly Continuation — EGLD/USDT P50_89

**Symbol:** EGLD/USDT  |  **P_fast:** 50  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 374 |
| net_profit_factor | 0.7088 |
| net_win_rate | 0.5000 |
| gross_profit_factor | 1.0007 |
| gross_win_rate | 0.5000 |
| sharpe_ratio | -2.0724 |
| sortino_ratio | -0.5759 |
| max_drawdown | 0.4968 |
| cagr | -0.2310 |
| net_avg_win | 62.8490 |
| net_avg_loss | -88.6744 |
| avg_hold_time_bars | 6.9278 |
| exposure | 0.1178 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
