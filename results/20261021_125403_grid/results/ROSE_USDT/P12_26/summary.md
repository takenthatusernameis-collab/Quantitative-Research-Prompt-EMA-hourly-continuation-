# EMA Hourly Continuation — ROSE/USDT P12_26

**Symbol:** ROSE/USDT  |  **P_fast:** 12  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 494 |
| net_profit_factor | 0.7761 |
| net_win_rate | 0.5142 |
| gross_profit_factor | 1.0471 |
| gross_win_rate | 0.5142 |
| sharpe_ratio | -1.7117 |
| sortino_ratio | -0.5478 |
| max_drawdown | 0.4741 |
| cagr | -0.2223 |
| net_avg_win | 63.8777 |
| net_avg_loss | -87.1108 |
| avg_hold_time_bars | 4.9636 |
| exposure | 0.1115 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
