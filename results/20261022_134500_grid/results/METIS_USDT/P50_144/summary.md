# EMA Hourly Continuation — METIS/USDT P50_144

**Symbol:** METIS/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 500 |
| net_profit_factor | 0.4889 |
| net_win_rate | 0.4240 |
| gross_profit_factor | 0.7890 |
| gross_win_rate | 0.4380 |
| sharpe_ratio | -4.8991 |
| sortino_ratio | -1.5321 |
| max_drawdown | 0.8493 |
| cagr | -0.5276 |
| net_avg_win | 38.2513 |
| net_avg_loss | -57.5980 |
| avg_hold_time_bars | 12.0420 |
| exposure | 0.2737 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
