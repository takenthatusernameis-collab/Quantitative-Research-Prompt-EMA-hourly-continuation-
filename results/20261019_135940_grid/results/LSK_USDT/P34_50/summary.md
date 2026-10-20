# EMA Hourly Continuation — LSK/USDT P34_50

**Symbol:** LSK/USDT  |  **P_fast:** 34  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 768 |
| net_profit_factor | 0.4097 |
| net_win_rate | 0.4544 |
| gross_profit_factor | 0.9475 |
| gross_win_rate | 0.4805 |
| sharpe_ratio | -7.5925 |
| sortino_ratio | -2.9891 |
| max_drawdown | 0.9774 |
| cagr | -0.7764 |
| net_avg_win | 19.4226 |
| net_avg_loss | -39.4894 |
| avg_hold_time_bars | 3.7513 |
| exposure | 0.1310 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
