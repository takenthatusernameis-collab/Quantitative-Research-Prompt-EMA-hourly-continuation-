# EMA Hourly Continuation — RIO/USDT P20_21

**Symbol:** RIO/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 138 |
| net_profit_factor | 0.5958 |
| net_win_rate | 0.4130 |
| gross_profit_factor | 0.7186 |
| gross_win_rate | 0.4130 |
| sharpe_ratio | -1.9764 |
| sortino_ratio | -0.3291 |
| max_drawdown | 0.3212 |
| cagr | -0.1411 |
| net_avg_win | 81.4327 |
| net_avg_loss | -96.1795 |
| avg_hold_time_bars | 6.1449 |
| exposure | 0.0389 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
