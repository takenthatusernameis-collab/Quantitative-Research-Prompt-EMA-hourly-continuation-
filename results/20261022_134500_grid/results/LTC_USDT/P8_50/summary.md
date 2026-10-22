# EMA Hourly Continuation — LTC/USDT P8_50

**Symbol:** LTC/USDT  |  **P_fast:** 8  |  **P_slow:** 50

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 1184 |
| net_profit_factor | 0.3575 |
| net_win_rate | 0.4257 |
| gross_profit_factor | 0.7888 |
| gross_win_rate | 0.4527 |
| sharpe_ratio | -9.9114 |
| sortino_ratio | -4.7921 |
| max_drawdown | 0.9979 |
| cagr | -0.9140 |
| net_avg_win | 11.0159 |
| net_avg_loss | -22.8396 |
| avg_hold_time_bars | 7.9071 |
| exposure | 0.4255 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
