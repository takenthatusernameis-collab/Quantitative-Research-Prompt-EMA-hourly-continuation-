# EMA Hourly Continuation — LSK/USDT P89_200

**Symbol:** LSK/USDT  |  **P_fast:** 89  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 371 |
| net_profit_factor | 0.6292 |
| net_win_rate | 0.4771 |
| gross_profit_factor | 0.9555 |
| gross_win_rate | 0.4852 |
| sharpe_ratio | -2.8695 |
| sortino_ratio | -0.7784 |
| max_drawdown | 0.6305 |
| cagr | -0.3105 |
| net_avg_win | 58.1832 |
| net_avg_loss | -84.3699 |
| avg_hold_time_bars | 13.9488 |
| exposure | 0.2352 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
