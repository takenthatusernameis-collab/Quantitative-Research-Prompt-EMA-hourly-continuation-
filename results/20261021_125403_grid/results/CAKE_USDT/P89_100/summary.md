# EMA Hourly Continuation — CAKE/USDT P89_100

**Symbol:** CAKE/USDT  |  **P_fast:** 89  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 83 |
| net_profit_factor | 0.7895 |
| net_win_rate | 0.5542 |
| gross_profit_factor | 1.2434 |
| gross_win_rate | 0.5542 |
| sharpe_ratio | -0.6637 |
| sortino_ratio | -0.0878 |
| max_drawdown | 0.1835 |
| cagr | -0.0394 |
| net_avg_win | 78.3405 |
| net_avg_loss | -123.3588 |
| avg_hold_time_bars | 5.1446 |
| exposure | 0.0194 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
