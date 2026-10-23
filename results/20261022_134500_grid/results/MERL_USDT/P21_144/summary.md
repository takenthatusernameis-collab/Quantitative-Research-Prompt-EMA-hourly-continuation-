# EMA Hourly Continuation — MERL/USDT P21_144

**Symbol:** MERL/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 482 |
| net_profit_factor | 0.6934 |
| net_win_rate | 0.4544 |
| gross_profit_factor | 0.8985 |
| gross_win_rate | 0.4564 |
| sharpe_ratio | -3.0445 |
| sortino_ratio | -0.9420 |
| max_drawdown | 0.7233 |
| cagr | -0.3584 |
| net_avg_win | 69.2744 |
| net_avg_loss | -83.1951 |
| avg_hold_time_bars | 24.7614 |
| exposure | 0.5440 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
