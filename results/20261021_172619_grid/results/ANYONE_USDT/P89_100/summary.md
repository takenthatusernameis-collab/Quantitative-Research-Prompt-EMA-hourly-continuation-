# EMA Hourly Continuation — ANYONE/USDT P89_100

**Symbol:** ANYONE/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 112 |
| net_profit_factor | 0.6520 |
| net_win_rate | 0.4643 |
| gross_profit_factor | 0.8435 |
| gross_win_rate | 0.4643 |
| sharpe_ratio | -1.3964 |
| sortino_ratio | -0.2219 |
| max_drawdown | 0.2432 |
| cagr | -0.0965 |
| net_avg_win | 73.8287 |
| net_avg_loss | -98.1361 |
| avg_hold_time_bars | 5.7768 |
| exposure | 0.0327 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
