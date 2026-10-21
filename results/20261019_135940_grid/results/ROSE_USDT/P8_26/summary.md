# EMA Hourly Continuation — ROSE/USDT P8_26

**Symbol:** ROSE/USDT  |  **P_fast:** 8  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1641 |
| net_profit_factor | 0.4440 |
| net_win_rate | 0.4497 |
| gross_profit_factor | 0.8334 |
| gross_win_rate | 0.4680 |
| sharpe_ratio | -9.3318 |
| sortino_ratio | -5.3442 |
| max_drawdown | 0.9985 |
| cagr | -0.9247 |
| net_avg_win | 10.8034 |
| net_avg_loss | -19.8868 |
| avg_hold_time_bars | 3.6338 |
| exposure | 0.2710 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
