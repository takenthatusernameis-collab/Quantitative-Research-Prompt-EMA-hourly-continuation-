# EMA Hourly Continuation — ANYONE/USDT P89_200

**Symbol:** ANYONE/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 338 |
| net_profit_factor | 0.5957 |
| net_win_rate | 0.4408 |
| gross_profit_factor | 0.7790 |
| gross_win_rate | 0.4497 |
| sharpe_ratio | -2.9528 |
| sortino_ratio | -0.8096 |
| max_drawdown | 0.6099 |
| cagr | -0.3129 |
| net_avg_win | 56.5301 |
| net_avg_loss | -74.8125 |
| avg_hold_time_bars | 13.0917 |
| exposure | 0.2236 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
