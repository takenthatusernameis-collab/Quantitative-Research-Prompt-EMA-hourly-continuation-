# EMA Hourly Continuation — ANKR/USDT P20_144

**Symbol:** ANKR/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.7747 |
| net_win_rate | 0.4859 |
| gross_profit_factor | 0.9734 |
| gross_win_rate | 0.4859 |
| sharpe_ratio | -1.7989 |
| sortino_ratio | -0.5078 |
| max_drawdown | 0.4960 |
| cagr | -0.2097 |
| net_avg_win | 80.7372 |
| net_avg_loss | -98.5196 |
| avg_hold_time_bars | 32.8977 |
| exposure | 0.5847 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
