# EMA Hourly Continuation — MLK/USDT P21_50

**Symbol:** MLK/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 432 |
| net_profit_factor | 0.4006 |
| net_win_rate | 0.3634 |
| gross_profit_factor | 0.6268 |
| gross_win_rate | 0.3681 |
| sharpe_ratio | -5.8787 |
| sortino_ratio | -1.7279 |
| max_drawdown | 0.8745 |
| cagr | -0.5561 |
| net_avg_win | 37.0851 |
| net_avg_loss | -52.8466 |
| avg_hold_time_bars | 8.0162 |
| exposure | 0.1567 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
