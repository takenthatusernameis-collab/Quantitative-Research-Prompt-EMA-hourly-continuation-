# EMA Hourly Continuation — RENDER/USDT P21_26

**Symbol:** RENDER/USDT  |  **P_fast:** 21  |  **P_slow:** 26

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 133 |
| net_profit_factor | 0.5711 |
| net_win_rate | 0.4286 |
| gross_profit_factor | 0.7589 |
| gross_win_rate | 0.4286 |
| sharpe_ratio | -2.2060 |
| sortino_ratio | -0.3893 |
| max_drawdown | 0.3276 |
| cagr | -0.1641 |
| net_avg_win | 75.0381 |
| net_avg_loss | -98.5519 |
| avg_hold_time_bars | 5.5489 |
| exposure | 0.0390 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
