# EMA Hourly Continuation — CETUS/USDT P26_50

**Symbol:** CETUS/USDT  |  **P_fast:** 26  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 953 |
| net_profit_factor | 0.5221 |
| net_win_rate | 0.4334 |
| gross_profit_factor | 0.8947 |
| gross_win_rate | 0.4502 |
| sharpe_ratio | -7.4112 |
| sortino_ratio | -3.2339 |
| max_drawdown | 0.9816 |
| cagr | -0.7896 |
| net_avg_win | 25.9306 |
| net_avg_loss | -37.9876 |
| avg_hold_time_bars | 3.8363 |
| exposure | 0.1654 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
