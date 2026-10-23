# EMA Hourly Continuation — HNT/USDT P20_200

**Symbol:** HNT/USDT  |  **P_fast:** 20  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 360 |
| net_profit_factor | 0.7381 |
| net_win_rate | 0.4917 |
| gross_profit_factor | 0.9546 |
| gross_win_rate | 0.4917 |
| sharpe_ratio | -1.7414 |
| sortino_ratio | -0.4685 |
| max_drawdown | 0.4440 |
| cagr | -0.1968 |
| net_avg_win | 67.3931 |
| net_avg_loss | -88.3099 |
| avg_hold_time_bars | 40.6444 |
| exposure | 0.6651 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
