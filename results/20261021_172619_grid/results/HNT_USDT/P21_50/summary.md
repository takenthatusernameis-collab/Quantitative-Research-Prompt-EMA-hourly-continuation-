# EMA Hourly Continuation — HNT/USDT P21_50

**Symbol:** HNT/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 466 |
| net_profit_factor | 0.6988 |
| net_win_rate | 0.4828 |
| gross_profit_factor | 0.8985 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -2.2314 |
| sortino_ratio | -0.6875 |
| max_drawdown | 0.5595 |
| cagr | -0.2705 |
| net_avg_win | 56.4063 |
| net_avg_loss | -75.3617 |
| avg_hold_time_bars | 7.7790 |
| exposure | 0.1648 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
