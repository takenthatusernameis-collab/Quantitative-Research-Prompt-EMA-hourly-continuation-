# EMA Hourly Continuation — DEEP/USDT P20_144

**Symbol:** DEEP/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 0.8978 |
| net_win_rate | 0.5061 |
| gross_profit_factor | 1.0123 |
| gross_win_rate | 0.5061 |
| sharpe_ratio | -0.5532 |
| sortino_ratio | -0.1383 |
| max_drawdown | 0.1771 |
| cagr | -0.0649 |
| net_avg_win | 89.5859 |
| net_avg_loss | -102.2589 |
| avg_hold_time_bars | 43.9837 |
| exposure | 0.6101 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
