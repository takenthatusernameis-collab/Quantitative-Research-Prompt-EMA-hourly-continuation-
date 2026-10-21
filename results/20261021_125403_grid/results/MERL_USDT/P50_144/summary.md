# EMA Hourly Continuation — MERL/USDT P50_144

**Symbol:** MERL/USDT  |  **P_fast:** 50  |  **P_slow:** 144

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 336 |
| net_profit_factor | 0.7529 |
| net_win_rate | 0.4732 |
| gross_profit_factor | 0.8947 |
| gross_win_rate | 0.4732 |
| sharpe_ratio | -1.6355 |
| sortino_ratio | -0.4270 |
| max_drawdown | 0.4394 |
| cagr | -0.1793 |
| net_avg_win | 74.8002 |
| net_avg_loss | -89.2506 |
| avg_hold_time_bars | 17.1845 |
| exposure | 0.2632 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
