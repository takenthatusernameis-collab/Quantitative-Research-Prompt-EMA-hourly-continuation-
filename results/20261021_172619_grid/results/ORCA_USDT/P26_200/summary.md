# EMA Hourly Continuation — ORCA/USDT P26_200

**Symbol:** ORCA/USDT  |  **P_fast:** 26  |  **P_slow:** 200

**Costs:** 10.0 bps taker + 2.0 bps slippage per side

**RR:** 1.0  |  **Fill:** signal-bar close  |  **SL/TP:** 1:1 to EMA_slow

**Sizing:** risk-based, 1.00% of equity per trade (notional cap 10.0x equity)


## Metrics (net of costs)

| Metric | Value |
|---|---|
| trade_count | 326 |
| net_profit_factor | 0.8985 |
| net_win_rate | 0.5307 |
| gross_profit_factor | 1.1084 |
| gross_win_rate | 0.5307 |
| sharpe_ratio | -0.5640 |
| sortino_ratio | -0.1461 |
| max_drawdown | 0.3016 |
| cagr | -0.0689 |
| net_avg_win | 83.9659 |
| net_avg_loss | -105.6629 |
| avg_hold_time_bars | 38.4294 |
| exposure | 0.5695 |

Decision label: rejected


Bulk artifacts: `trades.csv.gz`, `equity.csv.gz` (gzip-compressed CSV). Read with `gzip -dc <file>` or `pandas.read_csv(file, compression="gzip")`.
