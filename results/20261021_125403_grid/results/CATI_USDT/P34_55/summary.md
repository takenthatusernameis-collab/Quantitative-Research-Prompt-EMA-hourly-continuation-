# EMA Hourly Continuation — CATI/USDT P34_55

**Symbol:** CATI/USDT  |  **P_fast:** 34  |  **P_slow:** 55

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 243 |
| net_profit_factor | 0.5604 |
| net_win_rate | 0.4198 |
| gross_profit_factor | 0.7589 |
| gross_win_rate | 0.4239 |
| sharpe_ratio | -3.3619 |
| sortino_ratio | -0.8161 |
| max_drawdown | 0.5556 |
| cagr | -0.3169 |
| net_avg_win | 68.4620 |
| net_avg_loss | -88.3742 |
| avg_hold_time_bars | 6.5514 |
| exposure | 0.0873 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
