# EMA Hourly Continuation — ALT/USDT P8_200

**Symbol:** ALT/USDT  |  **P_fast:** 8  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 358 |
| net_profit_factor | 0.7552 |
| net_win_rate | 0.4777 |
| gross_profit_factor | 0.9080 |
| gross_win_rate | 0.4777 |
| sharpe_ratio | -1.6600 |
| sortino_ratio | -0.4468 |
| max_drawdown | 0.4328 |
| cagr | -0.1871 |
| net_avg_win | 73.1741 |
| net_avg_loss | -88.5993 |
| avg_hold_time_bars | 46.7402 |
| exposure | 0.7606 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
