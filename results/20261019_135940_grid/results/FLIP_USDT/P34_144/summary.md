# EMA Hourly Continuation — FLIP/USDT P34_144

**Symbol:** FLIP/USDT  |  **P_fast:** 34  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 369 |
| net_profit_factor | 0.5468 |
| net_win_rate | 0.4390 |
| gross_profit_factor | 0.8536 |
| gross_win_rate | 0.4499 |
| sharpe_ratio | -4.0651 |
| sortino_ratio | -1.0882 |
| max_drawdown | 0.7547 |
| cagr | -0.4138 |
| net_avg_win | 55.0061 |
| net_avg_loss | -78.7242 |
| avg_hold_time_bars | 21.5772 |
| exposure | 0.3619 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
