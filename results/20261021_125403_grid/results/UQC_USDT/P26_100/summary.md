# EMA Hourly Continuation — UQC/USDT P26_100

**Symbol:** UQC/USDT  |  **P_fast:** 26  |  **P_slow:** 100

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 245 |
| net_profit_factor | 0.3352 |
| net_win_rate | 0.2980 |
| gross_profit_factor | 0.5003 |
| gross_win_rate | 0.3224 |
| sharpe_ratio | -5.7710 |
| sortino_ratio | -1.2575 |
| max_drawdown | 0.8080 |
| cagr | -0.4802 |
| net_avg_win | 55.8180 |
| net_avg_loss | -70.6677 |
| avg_hold_time_bars | 47.7551 |
| exposure | 0.5295 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
