# EMA Hourly Continuation — ROSE/USDT P12_89

**Symbol:** ROSE/USDT  |  **P_fast:** 12  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.8732 |
| net_win_rate | 0.5101 |
| gross_profit_factor | 1.0492 |
| gross_win_rate | 0.5101 |
| sharpe_ratio | -1.0620 |
| sortino_ratio | -0.3383 |
| max_drawdown | 0.4732 |
| cagr | -0.1473 |
| net_avg_win | 90.1528 |
| net_avg_loss | -107.5064 |
| avg_hold_time_bars | 24.9069 |
| exposure | 0.5593 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
