# EMA Hourly Continuation — MINA/USDT P21_144

**Symbol:** MINA/USDT  |  **P_fast:** 21  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 375 |
| net_profit_factor | 0.9048 |
| net_win_rate | 0.5307 |
| gross_profit_factor | 1.1112 |
| gross_win_rate | 0.5307 |
| sharpe_ratio | -0.5385 |
| sortino_ratio | -0.1502 |
| max_drawdown | 0.3090 |
| cagr | -0.0708 |
| net_avg_win | 80.4380 |
| net_avg_loss | -100.5208 |
| avg_hold_time_bars | 33.6080 |
| exposure | 0.5729 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
