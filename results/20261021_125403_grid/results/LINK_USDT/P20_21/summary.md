# EMA Hourly Continuation — LINK/USDT P20_21

**Symbol:** LINK/USDT  |  **P_fast:** 20  |  **P_slow:** 21

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 126 |
| net_profit_factor | 0.5942 |
| net_win_rate | 0.4524 |
| gross_profit_factor | 0.8329 |
| gross_win_rate | 0.4524 |
| sharpe_ratio | -1.8610 |
| sortino_ratio | -0.2983 |
| max_drawdown | 0.3403 |
| cagr | -0.1284 |
| net_avg_win | 74.9644 |
| net_avg_loss | -104.2205 |
| avg_hold_time_bars | 4.9603 |
| exposure | 0.0284 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
