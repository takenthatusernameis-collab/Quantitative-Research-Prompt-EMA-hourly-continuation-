# EMA Hourly Continuation — ASTR/USDT P89_144

**Symbol:** ASTR/USDT  |  **P_fast:** 89  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.4430 |
| net_win_rate | 0.4313 |
| gross_profit_factor | 0.8604 |
| gross_win_rate | 0.4651 |
| sharpe_ratio | -5.4039 |
| sortino_ratio | -1.6605 |
| max_drawdown | 0.8758 |
| cagr | -0.5578 |
| net_avg_win | 34.0089 |
| net_avg_loss | -58.2199 |
| avg_hold_time_bars | 6.3975 |
| exposure | 0.1369 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
