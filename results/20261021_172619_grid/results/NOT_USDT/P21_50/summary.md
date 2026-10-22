# EMA Hourly Continuation — NOT/USDT P21_50

**Symbol:** NOT/USDT  |  **P_fast:** 21  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 447 |
| net_profit_factor | 0.7934 |
| net_win_rate | 0.5056 |
| gross_profit_factor | 1.0110 |
| gross_win_rate | 0.5056 |
| sharpe_ratio | -1.5265 |
| sortino_ratio | -0.4711 |
| max_drawdown | 0.4394 |
| cagr | -0.1951 |
| net_avg_win | 69.6516 |
| net_avg_loss | -89.7713 |
| avg_hold_time_bars | 6.8837 |
| exposure | 0.1445 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
