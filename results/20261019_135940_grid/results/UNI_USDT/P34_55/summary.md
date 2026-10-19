# EMA Hourly Continuation — UNI/USDT P34_55

**Symbol:** UNI/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 924 |
| net_profit_factor | 0.3546 |
| net_win_rate | 0.4188 |
| gross_profit_factor | 0.7381 |
| gross_win_rate | 0.4307 |
| sharpe_ratio | -9.1427 |
| sortino_ratio | -3.9404 |
| max_drawdown | 0.9932 |
| cagr | -0.8622 |
| net_avg_win | 14.0962 |
| net_avg_loss | -28.6523 |
| avg_hold_time_bars | 2.9697 |
| exposure | 0.1247 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
