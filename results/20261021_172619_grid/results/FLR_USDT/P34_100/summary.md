# EMA Hourly Continuation — FLR/USDT P34_100

**Symbol:** FLR/USDT  |  **P_fast:** 34  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 473 |
| net_profit_factor | 0.6384 |
| net_win_rate | 0.4651 |
| gross_profit_factor | 0.8617 |
| gross_win_rate | 0.4672 |
| sharpe_ratio | -3.0310 |
| sortino_ratio | -0.9397 |
| max_drawdown | 0.6647 |
| cagr | -0.3506 |
| net_avg_win | 53.0992 |
| net_avg_loss | -72.3312 |
| avg_hold_time_bars | 10.4989 |
| exposure | 0.2257 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
