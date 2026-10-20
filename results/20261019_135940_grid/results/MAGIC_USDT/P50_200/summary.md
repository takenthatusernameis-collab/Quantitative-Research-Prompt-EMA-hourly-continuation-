# EMA Hourly Continuation — MAGIC/USDT P50_200

**Symbol:** MAGIC/USDT  |  **P_fast:** 50  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 337 |
| net_profit_factor | 0.6208 |
| net_win_rate | 0.4481 |
| gross_profit_factor | 0.8150 |
| gross_win_rate | 0.4510 |
| sharpe_ratio | -2.7763 |
| sortino_ratio | -0.7215 |
| max_drawdown | 0.5981 |
| cagr | -0.2858 |
| net_avg_win | 61.8595 |
| net_avg_loss | -80.8927 |
| avg_hold_time_bars | 28.3798 |
| exposure | 0.4347 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
