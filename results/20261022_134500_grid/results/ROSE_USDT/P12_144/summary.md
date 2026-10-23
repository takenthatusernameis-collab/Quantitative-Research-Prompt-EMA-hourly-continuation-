# EMA Hourly Continuation — ROSE/USDT P12_144

**Symbol:** ROSE/USDT  |  **P_fast:** 12  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 391 |
| net_profit_factor | 0.9544 |
| net_win_rate | 0.5499 |
| gross_profit_factor | 1.2324 |
| gross_win_rate | 0.5550 |
| sharpe_ratio | -0.2441 |
| sortino_ratio | -0.0697 |
| max_drawdown | 0.2626 |
| cagr | -0.0376 |
| net_avg_win | 89.3488 |
| net_avg_loss | -114.3600 |
| avg_hold_time_bars | 41.5831 |
| exposure | 0.7390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
