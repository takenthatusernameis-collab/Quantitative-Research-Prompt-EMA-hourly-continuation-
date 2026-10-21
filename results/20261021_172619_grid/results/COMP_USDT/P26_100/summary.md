# EMA Hourly Continuation — COMP/USDT P26_100

**Symbol:** COMP/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 511 |
| net_profit_factor | 0.7148 |
| net_win_rate | 0.5010 |
| gross_profit_factor | 0.9557 |
| gross_win_rate | 0.5010 |
| sharpe_ratio | -2.0484 |
| sortino_ratio | -0.6637 |
| max_drawdown | 0.5691 |
| cagr | -0.2625 |
| net_avg_win | 52.3401 |
| net_avg_loss | -73.5068 |
| avg_hold_time_bars | 16.0783 |
| exposure | 0.3735 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
