# EMA Hourly Continuation — UNI/USDT P26_200

**Symbol:** UNI/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 409 |
| net_profit_factor | 0.6078 |
| net_win_rate | 0.4645 |
| gross_profit_factor | 0.8729 |
| gross_win_rate | 0.4694 |
| sharpe_ratio | -3.2036 |
| sortino_ratio | -0.9052 |
| max_drawdown | 0.6711 |
| cagr | -0.3553 |
| net_avg_win | 54.4846 |
| net_avg_loss | -77.7701 |
| avg_hold_time_bars | 29.0685 |
| exposure | 0.5404 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
