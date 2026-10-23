# EMA Hourly Continuation — BIGTIME/USDT P21_89

**Symbol:** BIGTIME/USDT  |  **P_fast:** 21  |  **P_slow:** 89

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 668 |
| net_profit_factor | 0.6907 |
| net_win_rate | 0.4940 |
| gross_profit_factor | 1.0052 |
| gross_win_rate | 0.4985 |
| sharpe_ratio | -3.1326 |
| sortino_ratio | -1.1423 |
| max_drawdown | 0.7552 |
| cagr | -0.4185 |
| net_avg_win | 50.4400 |
| net_avg_loss | -71.2960 |
| avg_hold_time_bars | 13.8937 |
| exposure | 0.4200 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
