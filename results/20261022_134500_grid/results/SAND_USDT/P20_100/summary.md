# EMA Hourly Continuation — SAND/USDT P20_100

**Symbol:** SAND/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 627 |
| net_profit_factor | 0.5553 |
| net_win_rate | 0.4466 |
| gross_profit_factor | 0.8931 |
| gross_win_rate | 0.4545 |
| sharpe_ratio | -4.9835 |
| sortino_ratio | -1.7458 |
| max_drawdown | 0.8881 |
| cagr | -0.5715 |
| net_avg_win | 39.2922 |
| net_avg_loss | -57.0925 |
| avg_hold_time_bars | 14.5439 |
| exposure | 0.4145 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
