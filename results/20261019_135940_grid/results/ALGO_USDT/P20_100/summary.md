# EMA Hourly Continuation — ALGO/USDT P20_100

**Symbol:** ALGO/USDT  |  **P_fast:** 20  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 661 |
| net_profit_factor | 0.6653 |
| net_win_rate | 0.4947 |
| gross_profit_factor | 1.0380 |
| gross_win_rate | 0.5053 |
| sharpe_ratio | -3.4177 |
| sortino_ratio | -1.2298 |
| max_drawdown | 0.7881 |
| cagr | -0.4497 |
| net_avg_win | 47.2201 |
| net_avg_loss | -69.4894 |
| avg_hold_time_bars | 13.2905 |
| exposure | 0.3993 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
