# EMA Hourly Continuation — CTSI/USDT P21_100

**Symbol:** CTSI/USDT  |  **P_fast:** 21  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 551 |
| net_profit_factor | 0.7760 |
| net_win_rate | 0.4828 |
| gross_profit_factor | 0.9903 |
| gross_win_rate | 0.4828 |
| sharpe_ratio | -2.3510 |
| sortino_ratio | -0.7882 |
| max_drawdown | 0.6400 |
| cagr | -0.3033 |
| net_avg_win | 77.6898 |
| net_avg_loss | -93.4414 |
| avg_hold_time_bars | 15.4011 |
| exposure | 0.3857 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
