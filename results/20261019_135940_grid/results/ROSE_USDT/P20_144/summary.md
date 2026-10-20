# EMA Hourly Continuation — ROSE/USDT P20_144

**Symbol:** ROSE/USDT  |  **P_fast:** 20  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 461 |
| net_profit_factor | 0.7641 |
| net_win_rate | 0.4989 |
| gross_profit_factor | 1.0285 |
| gross_win_rate | 0.5054 |
| sharpe_ratio | -1.9390 |
| sortino_ratio | -0.5868 |
| max_drawdown | 0.5385 |
| cagr | -0.2443 |
| net_avg_win | 71.1412 |
| net_avg_loss | -92.6984 |
| avg_hold_time_bars | 28.1757 |
| exposure | 0.5904 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
