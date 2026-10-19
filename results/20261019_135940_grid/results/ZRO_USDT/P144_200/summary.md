# EMA Hourly Continuation — ZRO/USDT P144_200

**Symbol:** ZRO/USDT  |  **P_fast:** 144  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 383 |
| net_profit_factor | 0.6373 |
| net_win_rate | 0.5039 |
| gross_profit_factor | 1.0488 |
| gross_win_rate | 0.5144 |
| sharpe_ratio | -2.7791 |
| sortino_ratio | -0.7948 |
| max_drawdown | 0.6135 |
| cagr | -0.3178 |
| net_avg_win | 53.7274 |
| net_avg_loss | -85.6368 |
| avg_hold_time_bars | 3.5039 |
| exposure | 0.0657 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
