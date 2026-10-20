# EMA Hourly Continuation — PROM/USDT P50_144

**Symbol:** PROM/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 595 |
| net_profit_factor | 0.4249 |
| net_win_rate | 0.4050 |
| gross_profit_factor | 0.7664 |
| gross_win_rate | 0.4387 |
| sharpe_ratio | -6.3608 |
| sortino_ratio | -2.1786 |
| max_drawdown | 0.9350 |
| cagr | -0.6573 |
| net_avg_win | 28.5766 |
| net_avg_loss | -45.7845 |
| avg_hold_time_bars | 10.7496 |
| exposure | 0.2907 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
