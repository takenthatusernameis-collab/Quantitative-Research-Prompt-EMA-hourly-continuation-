# EMA Hourly Continuation — PROM/USDT P12_34

**Symbol:** PROM/USDT  |  **P_fast:** 12  |  **P_slow:** 34

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 663 |
| net_profit_factor | 0.6060 |
| net_win_rate | 0.4465 |
| gross_profit_factor | 0.8774 |
| gross_win_rate | 0.4480 |
| sharpe_ratio | -4.5572 |
| sortino_ratio | -1.6683 |
| max_drawdown | 0.8606 |
| cagr | -0.5396 |
| net_avg_win | 44.5506 |
| net_avg_loss | -59.2940 |
| avg_hold_time_bars | 8.2775 |
| exposure | 0.2495 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
